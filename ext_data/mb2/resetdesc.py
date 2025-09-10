import os
import re

def remove_mbch_descriptions(root_dir):
    """
    Recursively searches for .mbch files in the given root directory and its subdirectories.
    For each .mbch file, it finds sections starting with 'description "' and replaces
    all content (including newlines) between the opening quote and its matching closing quote.
    The entire matched block 'description "..."' is replaced with 'description ""'.

    Args:
        root_dir (str): The starting directory to search from.
    """
    print(f"Starting search and modification from: {root_dir}")

    # This pattern matches:
    # 1. The literal string "description"
    # 2. Followed by one or more whitespace characters (`\s+`), which can be spaces, tabs, newlines.
    # 3. Followed by the opening quote `"`
    # 4. Followed by any character (including newlines) zero or more times, non-greedily,
    #    until it encounters the *next* literal closing quote.
    # The `re.DOTALL` flag is crucial for `.` to match newline characters.
    description_pattern = re.compile(r'description\s+".*?"', re.DOTALL)

    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.mbch'):
                file_path = os.path.join(dirpath, filename)
                # print(f"Processing file: {file_path}") # Removed for less verbosity

                try:
                    # Read the entire file content into a single string
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()

                    # Removed debugging prints for less verbosity
                    # print(f"  Raw file content (repr, first 500 chars): {repr(file_content[:500])}...")
                    # found_matches = description_pattern.findall(file_content)
                    # print(f"  Regex found matches: {found_matches}")
                    # if not found_matches and 'description "' in file_content:
                    #     print("  'description \"' was found in the file, but the full regex pattern did NOT find a complete match (e.g., missing closing quote, or unexpected characters).")

                    # Apply the regex substitution to the entire file content.
                    # This will find and replace all occurrences of 'description "..."' with 'description ""'.
                    new_file_content = description_pattern.sub('description ""', file_content)

                    modified = (new_file_content != file_content)

                    # If modifications were made, write the new content back to the file
                    if modified:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_file_content)
                        print(f"Successfully updated: {file_path}")
                    # else: # Removed for less verbosity
                    #     print(f"No changes needed for: {file_path}")

                except UnicodeDecodeError:
                    print(f"Error: Could not decode file {file_path} with UTF-8. The file might be in a different encoding.")
                except IOError as e:
                    print(f"Error reading or writing file {file_path}: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred with file {file_path}: {e}")

# Get the current working directory
current_directory = os.getcwd()

# Call the function to start the process
if __name__ == "__main__":
    remove_mbch_descriptions(current_directory)
    print("\nScript finished.")
    print("Please check your .mbch files for the changes.")
