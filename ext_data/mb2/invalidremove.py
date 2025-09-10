import os
import re

def process_mbch_files(directory):
    """
    Searches for .mbch files in the given directory and its subdirectories.
    For each .mbch file, it finds and deletes specific blocks of three lines
    that indicate an 'invalid' attribute entry.

    An 'invalid' block is defined as three consecutive lines matching:
    1. c_att_skill_XX  MB_ATT_INVALID
    2. c_att_names_XX  ""
    3. c_att_ranks_XX  -1
    where 'XX' is the same numerical index for all three lines.

    Args:
        directory (str): The path to the directory to start searching from.
    """

    # Regular expressions to match and capture the numerical index (XX)
    # The \s*$ at the end ensures that it matches the line exactly,
    # allowing for optional trailing whitespace.
    skill_pattern = re.compile(r'c_att_skill_(\d+)\s+MB_ATT_INVALID\s*$')
    names_pattern = re.compile(r'c_att_names_(\d+)\s+""\s*$')
    ranks_pattern = re.compile(r'c_att_ranks_(\d+)\s+-1\s*$')

    print(f"Starting scan for .mbch files in: {os.path.abspath(directory)}\n")

    # Walk through the directory tree
    for root, _, files in os.walk(directory):
        for file_name in files:
            # Check if the file is an .mbch file
            if file_name.lower().endswith('.mbch'):
                file_path = os.path.join(root, file_name)
                print(f"  Processing file: {file_path}")

                try:
                    # Read all lines from the file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()

                    new_lines = [] # List to store lines that are NOT deleted
                    i = 0 # Index to iterate through lines

                    # Process lines to identify and skip invalid blocks
                    while i < len(lines):
                        current_line = lines[i]
                        
                        # Attempt to match the first line of an invalid block (skill line)
                        match_skill = skill_pattern.match(current_line)
                        
                        if match_skill:
                            # Extract the numerical index from the skill line
                            num = match_skill.group(1)
                            
                            # Check if the next two lines exist and match their respective patterns
                            # with the SAME numerical index.
                            match_names = names_pattern.match(lines[i+1]) if i + 1 < len(lines) else None
                            match_ranks = ranks_pattern.match(lines[i+2]) if i + 2 < len(lines) else None

                            if (match_names and match_names.group(1) == num and
                                match_ranks and match_ranks.group(1) == num):
                                # If all three lines match the pattern and have the same number,
                                # then this is an invalid block.
                                print(f"    - Found and deleting invalid block (c_att_skill_{num}) at line {i+1}")
                                i += 3 # Skip these three lines by advancing the index by 3
                                continue # Continue to the next iteration to process the line after the skipped block
                            
                        # If the current line is not part of a valid invalid block, keep it
                        new_lines.append(current_line)
                        i += 1 # Move to the next line

                    # Write the modified content (excluding deleted blocks) back to the file.
                    # This effectively 'closes the gap' as the lines are simply not written.
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.writelines(new_lines)
                    print(f"  Finished processing {file_name}. Changes saved.\n")

                except Exception as e:
                    # Catch and report any errors during file processing
                    print(f"  ERROR processing {file_path}: {e}\n")

    print("Script finished scanning all .mbch files.")

# --- How to run the script ---
# You can specify the directory to start the scan from.
# '.' refers to the current directory where the script is executed.
if __name__ == "__main__":
    # To run, simply call the function with the starting directory.
    # For example, to process files in the current directory and all subdirectories:
    process_mbch_files('.') 

    # If you want to specify a different directory:
    # process_mbch_files('/path/to/your/folder')
