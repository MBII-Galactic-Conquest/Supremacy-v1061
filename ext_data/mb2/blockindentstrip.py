import os

def remove_block_indentation(filepath):
    """
    Removes one level of tab indentation within blocks ({...}) in a .mbch file.

    Args:
        filepath (str): The path to the .mbch file.
    """
    print(f"Processing file: {filepath}")
    lines = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    modified_lines = []
    in_block = False

    for line in lines:
        stripped_line = line.strip()

        # Check for block start
        if stripped_line.startswith('{'):
            in_block = True
            modified_lines.append(line) # Keep the '{' line as is
        # Check for block end
        elif stripped_line.startswith('}'):
            # If we were in a block and the '}' line starts with a tab, remove it
            if in_block and line.startswith('\t'):
                modified_lines.append(line[1:]) # Remove one leading tab
            else:
                modified_lines.append(line)
            in_block = False
        # Process lines within a block
        elif in_block:
            # If the line starts with a tab, remove it
            if line.startswith('\t'):
                modified_lines.append(line[1:]) # Remove one leading tab
            else:
                modified_lines.append(line) # Keep line as is if no tab or not in block
        # Lines outside blocks
        else:
            modified_lines.append(line)

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(modified_lines)
        print(f"Successfully modified: {filepath}")
    except Exception as e:
        print(f"Error writing to {filepath}: {e}")

def process_directory(root_dir):
    """
    Walks through the directory and its subdirectories to find and process .mbch files.

    Args:
        root_dir (str): The starting directory to search from.
    """
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.mbch'):
                filepath = os.path.join(dirpath, filename)
                remove_block_indentation(filepath)

if __name__ == "__main__":
    # Get the current working directory where the script is run
    current_directory = os.getcwd()
    print(f"Starting to process .mbch files in: {current_directory} and its subdirectories.")
    process_directory(current_directory)
    print("Processing complete.")