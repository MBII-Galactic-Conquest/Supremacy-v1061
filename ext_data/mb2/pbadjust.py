import re
import sys
import os
import glob
import configparser # Import the configparser module

# Global variable for block_size_for_start, loaded from config.
# This variable is primarily for config.ini generation and loading, but its value
# does not directly drive the re-numbering logic in calculate_new_block_number in this version,
# as dynamic block sizes/gaps from //PBADJUST take precedence.
CONFIGURED_BLOCK_SIZE = 12 # Default to 12, for 0-11 blocks then jump to 15.

# Global variables to dynamically store block size and gap size parsed from //PBADJUST comments.
# These are initialized with the default values used in the absence of a PBADJUST comment.
_dynamic_block_size_in_sequence = 12  # Default: 0-11 is 12 items (0-indexed, so 12 total items)
_dynamic_gap_size = 3                 # Default: 12 (logical index) + 3 = 15 (new number)

def load_configuration():
    """
    Loads configuration from config.ini, specifically the block_size_before_jump.
    Sets the global CONFIGURED_BLOCK_SIZE.
    If config.ini does not exist, it will be created with default settings.
    This function's CONFIGURED_BLOCK_SIZE serves as a system-wide default,
    but it can be overridden on a per-file basis by the //PBADJUST comment.
    """
    global CONFIGURED_BLOCK_SIZE
    config = configparser.ConfigParser()
    config_file_path = 'config.ini'

    # Check if config.ini exists. If not, create it with default values.
    if not os.path.exists(config_file_path):
        print(f"config.ini not found. Creating with default settings.")
        # Default value for the config file is 12, to align with the 0-11 block size
        config['SETTINGS'] = {'block_size_before_jump': str(CONFIGURED_BLOCK_SIZE)}
        try:
            with open(config_file_path, 'w') as configfile:
                config.write(configfile)
            print(f"Default config.ini created at {os.path.abspath(config_file_path)}")
        except IOError as e:
            print(f"Error creating config.ini: {e}. Please ensure write permissions in the current directory.")
            # Continue to use default CONFIGURED_BLOCK_SIZE if creation failed

    # Now attempt to read the configuration (either newly created or existing)
    try:
        config.read(config_file_path)
        if 'SETTINGS' in config and 'block_size_before_jump' in config['SETTINGS']:
            configured_value = int(config['SETTINGS']['block_size_before_jump'])
            if configured_value > 0: # Ensure it's a positive integer
                # Update CONFIGURED_BLOCK_SIZE if a valid value is found in config
                CONFIGURED_BLOCK_SIZE = configured_value
                print(f"Configuration loaded: block_size_before_jump = {CONFIGURED_BLOCK_SIZE}")
            else:
                print(f"Warning: 'block_size_before_jump' in config.ini must be a positive integer. Using default value {CONFIGURED_BLOCK_SIZE}.")
        else:
            print(f"Warning: 'SETTINGS' section or 'block_size_before_jump' key not found in {config_file_path}. Using default value {CONFIGURED_BLOCK_SIZE}.")
    except configparser.Error as e:
        print(f"Error reading config.ini: {e}. Using default value {CONFIGURED_BLOCK_SIZE}.")
    except ValueError:
        print(f"Error: 'block_size_before_jump' in config.ini is not a valid integer. Using default value {CONFIGURED_BLOCK_SIZE}.")


def calculate_new_block_number(block_sequence_index):
    """
    Calculates the new block number based on its sequential order.
    This function now uses the dynamically set _dynamic_block_size_in_sequence
    and _dynamic_gap_size values, which can be overridden by //PBADJUST comments.

    _dynamic_block_size_in_sequence: The number of sequential items in a block
                                     (e.g., if set to 14, items 0-13 form a block).
    _dynamic_gap_size: The size of the jump to add after each complete block.

    Example: If //PBADJUST 13:1 is used:
    - _dynamic_block_size_in_sequence = 13 + 1 = 14 (meaning 0-13 are in one logical block)
    - _dynamic_gap_size = 1

    Logical block sequence:  0-13   | 14-27  | 28-41  | 42-55
    Group Number:            0      | 1      | 2      | 3
    Offset:                  0*1=0  | 1*1=1  | 2*1=2  | 3*1=3
    New Number (Example):
      Logical 0 -> 0 + 0 = 0
      Logical 13 -> 13 + 0 = 13
      Logical 14 -> 14 + 1 = 15 (Start of 2nd block, effectively jumping from expected 14 to 15)
      Logical 27 -> 27 + 1 = 28
      Logical 28 -> 28 + 2 = 30 (Start of 3rd block, effectively jumping from expected 29 to 30)
      Logical 41 -> 41 + 2 = 43
      Logical 42 -> 42 + 3 = 45 (Start of 4th block, effectively jumping from expected 43 to 45)
    This aligns with the desired 15 -> 30 -> 45 pattern for the start of the jumped sequences.
    """
    global _dynamic_block_size_in_sequence, _dynamic_gap_size

    # Ensure dynamic values are positive to prevent division by zero or illogical behavior
    block_size = max(1, _dynamic_block_size_in_sequence)
    gap = max(0, _dynamic_gap_size) # Gap can be 0 if no jump is desired

    group_number = block_sequence_index // block_size
    offset = group_number * gap
    return block_sequence_index + offset

def process_mbch_file(filepath):
    """
    Reads an .mbch file, re-numbers specific lines based on the calculated block sequence,
    and writes the changes back to the original file.
    It now supports dynamic adjustment of block size and gap using //PBADJUST comments.
    """
    print(f"Processing file: {filepath}")
    modified_lines = []
    
    # Regex for c_att_ lines: Extremely robust and designed to capture all parts precisely.
    # - (?P<leading_part>.*?) : Non-greedy match for any characters at the start.
    # - c_att_(?P<type_name>skill|names|ranks)_ : Matches 'c_att_', captures type, then '_'.
    # - (?P<num_val>\d+) : Captures the number.
    # - (?P<rest_of_line_content>.*)$ : Captures everything after the number to the end of the line.
    line_pattern = re.compile(r"^(?P<leading_part>.*?)c_att_(?P<type_name>skill|names|ranks)_(?P<num_val>\d+)(?P<rest_of_line_content>.*)$")
    
    # Regex for //PBADJUST comments:
    # - ^\s*//PBADJUST\s* : Matches "//PBADJUST" at the start of the line, with optional leading whitespace.
    # - (?P<block_size_idx>\d+) : Captures the first number (logical index of last item in block).
    #   Example: If you want 14 items per block (0-13), then block_size_idx should be 13.
    # - : : Matches the colon separator.
    # - (?P<gap_size>\d+) : Captures the second number (the gap size).
    #   Example: If you want to jump by 1 after each block of 14, then gap_size should be 1.
    #   So, for the 15 -> 30 -> 45 pattern, use //PBADJUST 13:1
    # - (:\d+)? : Optionally matches a third number, which is ignored for now.
    # - .*$ : Matches any remaining characters to the end of the line.
    pbadjust_pattern = re.compile(r"^\s*//PBADJUST\s*(?P<block_size_idx>\d+):(?P<gap_size>\d+)(?::\d+)?.*$")

    global _dynamic_block_size_in_sequence, _dynamic_gap_size

    # global_item_counter tracks the logical index of each triplet found globally within the current block.
    # This counter resets after each //PBADJUST directive.
    global_item_counter = 0
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if not lines:
            print(f"File {filepath} is empty. No lines to process.")
            return

        i = 0
        while i < len(lines):
            line = lines[i]
            # Strip only trailing newline/carriage return, preserve all other characters including leading/middle whitespace.
            cleaned_line = line.rstrip('\n\r')
            
            pbadjust_match = pbadjust_pattern.match(cleaned_line)
            if pbadjust_match:
                try:
                    # Parse block_size_idx and gap_size from the //PBADJUST comment
                    block_size_idx = int(pbadjust_match.group('block_size_idx'))
                    gap_size = int(pbadjust_match.group('gap_size'))
                    
                    # Update global dynamic settings
                    _dynamic_block_size_in_sequence = block_size_idx + 1 # e.g., 11 means 0-11, so 12 total items
                    _dynamic_gap_size = gap_size
                    
                    # Reset the item counter for the new block defined by PBADJUST
                    global_item_counter = 0
                    
                    print(f"//PBADJUST found: Setting block_size_in_sequence to {_dynamic_block_size_in_sequence} and gap_size to {_dynamic_gap_size}.")
                    
                    # Add the PBADJUST line to the modified list as is
                    modified_lines.append(line)
                    i += 1
                    continue # Move to the next line in the file
                except ValueError:
                    print(f"Warning: Invalid numbers in //PBADJUST comment at original line {i+1} in {filepath}. Using current block/gap sizes.")
                    # If parsing fails, just add the line and continue, using existing dynamic settings
                    modified_lines.append(line)
                    i += 1
                    continue


            match = line_pattern.match(cleaned_line)
            
            if match:
                line_type = match.group('type_name') # Access type via named group
                
                if line_type == "skill":
                    # Calculate new number using current dynamic settings
                    new_num = calculate_new_block_number(global_item_counter)
                    
                    # Process the triplet (skill, names, ranks)
                    # We expect exactly 3 lines forming a triplet for each logical block
                    for j in range(3):
                        if i + j < len(lines):
                            sub_line = lines[i + j]
                            # Strip only trailing newline/carriage return for sub-lines
                            sub_cleaned_line = sub_line.rstrip('\n\r')
                            sub_match = line_pattern.match(sub_cleaned_line) # Use same line_pattern for sub-lines
                            
                            # Ensure sub_match is valid and the type is one of the expected ones
                            if sub_match and sub_match.group('type_name') in ["skill", "names", "ranks"]:
                                # Reconstruct the line using captured parts for perfect fidelity.
                                leading_part = sub_match.group('leading_part')
                                type_part = sub_match.group('type_name')
                                rest_of_line_content = sub_match.group('rest_of_line_content')
                                # Reconstruct as "leading_part + c_att_ + type_part + _ + new_num + rest_of_line_content + newline"
                                modified_lines.append(f"{leading_part}c_att_{type_part}_{new_num}{rest_of_line_content}\n")
                            else:
                                print(f"Warning: Triplet structure broken or unexpected line at original line {i+j+1} in {filepath}. Appending original line and continuing.")
                                modified_lines.append(sub_line)
                                # If the triplet structure is broken, we append the original line
                                # and break from the inner loop to prevent further errors on this triplet.
                                break 
                        else:
                            print(f"Warning: End of file reached while expecting more lines for a triplet at line {i+j+1} in {filepath}. Appending remaining lines as-is.")
                            # If end of file is reached mid-triplet, append the line and break.
                            break
                    
                    # Advance main loop index by the number of lines successfully processed in this triplet.
                    # This is 'j' because it increments for each line in the triplet.
                    i += j + 1
                    global_item_counter += 1 # Increment for the next logical block
                    continue # Continue to the next iteration of the outer while loop
                else:
                    # If a non-skill line matched but wasn't part of a skill-led triplet just processed, add as-is.
                    # This handles cases where 'names' or 'ranks' lines might appear unexpectedly without a preceding 'skill'.
                    modified_lines.append(line)
                    i += 1
            else:
                # If a line does not match any of the patterns (c_att_ or //PBADJUST), add it to the modified list as is.
                modified_lines.append(line)
                i += 1

        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(modified_lines)
        print(f"Successfully processed {filepath}")

    except FileNotFoundError:
        print(f"Error: File not found - {filepath}")
    except Exception as e:
        print(f"An unexpected error occurred while processing {filepath}: {e}")

def main():
    """
    Main function to handle command-line arguments and orchestrate file processing.
    It takes one or more file paths or wildcard patterns as input.
    If no arguments are provided, it defaults to processing all *.mbch files
    in the current directory.
    """
    load_configuration() # Load configuration at the start of main

    if len(sys.argv) < 2:
        file_patterns = ["*.mbch"]
        print("No specific files provided. Processing all '*.mbch' files in the current directory.")
    else:
        file_patterns = sys.argv[1:]

    processed_any_file = False

    for pattern in file_patterns:
        files_to_process = glob.glob(pattern)
        
        if not files_to_process:
            print(f"Warning: No files found matching pattern '{pattern}'. Skipping.")
            continue

        for filepath in files_to_process:
            if os.path.isfile(filepath):
                process_mbch_file(filepath)
                processed_any_file = True
            else:
                print(f"Warning: '{filepath}' is not a valid file and will be skipped.")

    if not processed_any_file:
        print("No .mbch files were processed. Please check your file paths or patterns.")

if __name__ == "__main__":
    main()
