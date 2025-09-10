import argparse
import os
import sys # Import sys module to get the current script's filename
import json # Import json module to read the ignore file

def beautify_file(filepath, tab_width=4, remove_all_blank_lines=False):
    """
    Beautifies a single code file by converting leading spaces to tabs for indentation,
    removing trailing whitespace, and compacting newlines.

    Compacting newlines can either mean:
    - Removing consecutive blank lines (leaving at most one blank line) and
      removing leading/trailing blank lines (default behavior).
    - Removing ALL blank lines, making the code as dense as possible (if remove_all_blank_lines is True).

    Args:
        filepath (str): The path to the code file to beautify.
        tab_width (int): The number of spaces that constitute one tab.
        remove_all_blank_lines (bool): If True, all blank lines will be removed.
                                       If False, consecutive blank lines are reduced to one.
    Returns:
        bool: True if the file was processed successfully, False otherwise.
    """
    if not os.path.exists(filepath):
        print(f"Error: File not found at '{filepath}'")
        return False

    try:
        # Read all lines from the input file
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        modified_lines_with_indentation = []
        for line in lines:
            # 1. Remove trailing whitespace from the line
            line = line.rstrip()

            # 2. Determine the number of leading spaces
            first_char_index = len(line) - len(line.lstrip(' '))
            leading_spaces = first_char_index

            # 3. Calculate how many tabs and remaining spaces are needed
            num_tabs = leading_spaces // tab_width
            remaining_spaces = leading_spaces % tab_width

            # 4. Reconstruct the line with tabs and any leftover spaces,
            # followed by the actual code content (after leading spaces)
            code_content = line[first_char_index:]
            new_line = '\t' * num_tabs + ' ' * remaining_spaces + code_content
            modified_lines_with_indentation.append(new_line) # Store without adding newline yet

        # Now, process for newline compaction based on the option
        compacted_lines = []
        if remove_all_blank_lines:
            # Remove all lines that are entirely whitespace or empty
            compacted_lines = [line_content for line_content in modified_lines_with_indentation if line_content.strip()]
        else:
            # Consolidate multiple blank lines into a single one, and remove leading/trailing blanks
            previous_line_was_blank = False
            for line_content in modified_lines_with_indentation:
                is_current_line_blank = not line_content.strip()

                if is_current_line_blank:
                    if not previous_line_was_blank:
                        compacted_lines.append('') # Add a single empty string for a blank line
                    previous_line_was_blank = True
                else:
                    compacted_lines.append(line_content)
                    previous_line_was_blank = False

            # Remove leading blank lines
            while compacted_lines and not compacted_lines[0].strip():
                compacted_lines.pop(0)

            # Remove trailing blank lines
            while compacted_lines and not compacted_lines[-1].strip():
                compacted_lines.pop()

        # Add newlines back for writing to file
        final_lines_to_write = [line + '\n' for line in compacted_lines]

        # Write the modified content back to the original file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(final_lines_to_write)

        print(f"  Processed '{filepath}'")
        return True

    except Exception as e:
        print(f"  An error occurred while processing '{filepath}': {e}")
        return False

def load_ignore_list(json_filepath):
    """
    Loads a list of filenames to ignore from a JSON file. If the file does not exist,
    it creates it with a placeholder empty list `[]` and prompts the user.

    Args:
        json_filepath (str): The path to the JSON file.
    Returns:
        set: A set of filenames to ignore. Returns an empty set if parsing fails
              even after creation.
    """
    ignore_set = set()
    file_was_created = False

    if not os.path.isfile(json_filepath):
        print(f"Info: Ignore file '{json_filepath}' not found.")
        print(f"Creating it with placeholder content (empty list []).")
        try:
            # Ensure the directory exists before creating the file
            os.makedirs(os.path.dirname(json_filepath) or '.', exist_ok=True)
            with open(json_filepath, 'w', encoding='utf-8') as f:
                json.dump([], f, indent=4) # Write an empty JSON list with pretty print
            file_was_created = True
        except OSError as e:
            print(f"Error: Could not create ignore file '{json_filepath}'. Check path or permissions: {e}")
            # If creation failed, we can't proceed with loading/pausing for this file
            return ignore_set
    
    try:
        with open(json_filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                ignore_set.update(str(item) for item in data)
            else:
                print(f"Warning: Ignore file '{json_filepath}' content is not a list. No additional files will be ignored from this file.")
    except json.JSONDecodeError as e:
        print(f"Error: Could not parse ignore file '{json_filepath}'. Invalid JSON format: {e}. Please correct the file content.")
    except Exception as e:
        print(f"An unexpected error occurred while reading ignore file '{json_filepath}': {e}")
    
    # If the file was just created, prompt the user
    if file_was_created:
        print("\n-----------------------------------------------------------")
        print(f"The ignore file '{json_filepath}' has been created.")
        print("Please modify this file to list the filenames you wish to ignore.")
        print("Once you have modified it, save the file.")
        print("Press Enter to continue processing (without current ignores, if any) or re-run the script to apply your changes.")
        input("Press Enter to continue...")
        print("-----------------------------------------------------------\n")

    return ignore_set


def process_directory_recursively(root_dir, tab_width=4, remove_all_blank_lines=False, ignore_file_path=None):
    """
    Recursively processes all files in a given directory and its subdirectories
    for code beautification, respecting ignore lists.

    Args:
        root_dir (str): The root directory to start processing from.
        tab_width (int): The number of spaces that constitute one tab.
        remove_all_blank_lines (bool): If True, all blank lines will be removed.
                                       If False, consecutive blank lines are reduced to one.
        ignore_file_path (str, optional): Path to a JSON file containing filenames to ignore.
    """
    if not os.path.isdir(root_dir):
        print(f"Error: Directory not found at '{root_dir}'")
        return

    # Get the absolute path of the current script to exclude it from processing
    current_script_path = os.path.abspath(sys.argv[0])

    # Load the ignore list from the specified JSON file
    additional_ignored_filenames = set()
    if ignore_file_path:
        additional_ignored_filenames = load_ignore_list(ignore_file_path)
        # Check if the script itself is in the ignore list (unlikely, but for robustness)
        if current_script_path in additional_ignored_filenames or os.path.basename(current_script_path) in additional_ignored_filenames:
            print(f"Warning: The ignore file '{ignore_file_path}' explicitly lists the beautifier script itself. "
                  "It will still be skipped by default logic.")
            # Ensure the script itself is not accidentally processed even if listed in ignore file
            additional_ignored_filenames.discard(os.path.basename(current_script_path))
            additional_ignored_filenames.discard(current_script_path)


    print(f"Starting code beautification in '{root_dir}' and its subdirectories...")
    print(f"Excluding self: '{current_script_path}'")
    if additional_ignored_filenames:
        print(f"Additionally excluding files specified in '{ignore_file_path}': {', '.join(sorted(list(additional_ignored_filenames)))}")

    processed_count = 0
    failed_count = 0
    skipped_count = 0

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            abs_filepath = os.path.abspath(filepath) # Get absolute path for comparison
            base_filename = os.path.basename(filepath) # Get just the filename for ignore list check

            # Check 1: Skip the script itself
            if abs_filepath == current_script_path:
                print(f"  Skipping own script: '{filepath}'")
                skipped_count += 1
                continue

            # Check 2: Skip files listed in the provided ignore JSON
            if base_filename in additional_ignored_filenames:
                print(f"  Skipping ignored file (from JSON list): '{filepath}'")
                skipped_count += 1
                continue

            # You can add logic here to filter files by extension if needed
            # For example: if filename.endswith(('.py', '.js', '.txt')):
            # For now, it processes all files.
            # You might want to skip certain binary files or archives if they are present
            # e.g., if any(filepath.endswith(ext) for ext in ['.zip', '.tar.gz', '.jpg', '.png', '.bin']):
            #     print(f"  Skipping binary/archive file: '{filepath}'")
            #     skipped_count += 1
            #     continue

            print(f"Checking: {filepath}") # Indicate which file is being checked
            if beautify_file(filepath, tab_width, remove_all_blank_lines):
                processed_count += 1
            else:
                failed_count += 1

    print("\nBeautification complete!")
    print(f"Total files processed: {processed_count}")
    print(f"Files skipped (including self and those from ignore list): {skipped_count}")
    if failed_count > 0:
        print(f"Files with errors during processing: {failed_count}")
    
    compaction_message = "newlines compacted (consecutive reduced to one and leading/trailing removed)."
    if remove_all_blank_lines:
        compaction_message = "all blank newlines removed for maximum compaction."
    
    print(f"Indentation converted to tabs (assuming {tab_width} spaces per tab), trailing whitespace removed, and {compaction_message}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Beautify code by converting leading spaces to tabs and removing trailing whitespace. "
                    "Can process a single file or recursively process files in a directory."
    )
    parser.add_argument(
        "path",
        type=str,
        help="The path to a single code file OR a directory to recursively beautify."
    )
    parser.add_argument(
        "--tab-width",
        type=int,
        default=4,
        help="The number of spaces that constitute one tab. Default is 4."
    )
    parser.add_argument(
        "--no-blank-lines",
        action="store_true",
        help="If set, all blank lines will be removed for maximum code compaction. "
             "By default, consecutive blank lines are reduced to a single one."
    )
    parser.add_argument(
        "--ignore-file",
        type=str,
        help="Path to a JSON file containing a list of filenames (e.g., [\"file1.txt\", \"file2.py\"]) to ignore during processing. "
             "If the file does not exist, it will be created with an empty list."
    )

    args = parser.parse_args()

    # Determine if the provided path is a file or a directory
    if os.path.isfile(args.path):
        # When processing a single file, we still want to skip if it's the script itself.
        # This prevents accidental self-modification if the user explicitly points to it.
        current_script_path = os.path.abspath(sys.argv[0])
        abs_target_path = os.path.abspath(args.path)

        # In single file mode, if an ignore file is specified, we should still load it
        # to ensure the single target file isn't ignored if it's listed.
        additional_ignored_filenames = set()
        if args.ignore_file:
            additional_ignored_filenames = load_ignore_list(args.ignore_file)

        if abs_target_path == current_script_path:
            print(f"Skipping own script: '{args.path}'")
            print("Cannot beautify the script itself when specified as a single file.")
        elif os.path.basename(abs_target_path) in additional_ignored_filenames:
            print(f"Skipping ignored file (from JSON list): '{args.path}'")
            print("Cannot beautify this file as it is listed in the ignore file.")
        else:
            print(f"Processing single file: '{args.path}'")
            beautify_file(args.path, args.tab_width, args.no_blank_lines)
    elif os.path.isdir(args.path):
        process_directory_recursively(args.path, args.tab_width, args.no_blank_lines, args.ignore_file)
    else:
        print(f"Error: Path '{args.path}' is neither a file nor a directory.")
        print("Please provide a valid file path or directory path.")

