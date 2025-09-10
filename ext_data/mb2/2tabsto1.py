import os
import glob

def convert_tabs_in_mbch_files(directory_path):
    """
    Converts occurrences of two tabs to one tab in all .mbch files
    within the specified directory and its subdirectories.

    Args:
        directory_path (str): The path to the directory containing .mbch files.
    """
    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' not found.")
        return

    # Construct the search pattern for .mbch files, including subdirectories (**)
    search_pattern = os.path.join(directory_path, "**", "*.mbch")
    # Use recursive=True to search through subdirectories
    mbch_files = glob.glob(search_pattern, recursive=True)

    if not mbch_files:
        print(f"No .mbch files found in '{directory_path}' or its subdirectories.")
        return

    print(f"Found {len(mbch_files)} .mbch files. Processing...")

    for file_path in mbch_files:
        print(f"Processing: {file_path}")
        try:
            # Read the original content
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()

            # Perform the replacement: two tabs to one tab
            modified_content = original_content.replace('\t\t', '\t')

            # Write the modified content back to the same file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)

            print(f"Successfully processed '{os.path.basename(file_path)}'.")

        except Exception as e:
            print(f"Error processing '{os.path.basename(file_path)}': {e}")

if __name__ == "__main__":
    # Ask the user for the directory path
    input_directory = input("Please enter the path to the directory containing your .mbch files: ")
    convert_tabs_in_mbch_files(input_directory)
    print("Tab conversion process completed.")
