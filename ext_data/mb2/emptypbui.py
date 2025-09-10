import re
import os

def modify_mbch_file(filepath):
    """
    Modifies a .mbch file by adding custom build properties if 'isCustomBuild'
    is not found anywhere in the file content, and a 'ClassInfo {}' block exists.

    Args:
        filepath (str): The path to the .mbch file to process.
    """
    # The block of text to be inserted.
    # IMPORTANT: No leading whitespace for indentation as per the requirement.
    INSERTION_TEXT = """isCustomBuild	1
mbPoints	0
hasCustomSpec	3
isOnlyOneSpec	1
customSpecName_1	""
customSpecIcon_1	"gfx/sup_builds/null/sup_empty"
customSpecDesc_1	""
customSpecName_2	""
customSpecIcon_2	"gfx/sup_builds/null/sup_empty"
customSpecDesc_2	""
customSpecName_3	""
customSpecIcon_3	"gfx/sup_builds/null/sup_empty"
customSpecDesc_3	""
c_att_skill_0	MB_ATT_INVALID
c_att_names_0	""
c_att_ranks_0	-1"""

    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found at '{filepath}'")
        return

    try:
        # Read the entire content of the file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # First, check if 'isCustomBuild' exists anywhere in the entire file content.
        if "isCustomBuild" not in content:
            print(f"'{filepath}': 'isCustomBuild' not found anywhere in the file. Checking for 'ClassInfo' block...")

            # Regex to find the ClassInfo block.
            # Group 1: (ClassInfo\s*\{) captures "ClassInfo {" (with optional whitespace before and after 'ClassInfo', and before '{').
            # Group 2: (.*?) captures the content inside the braces (non-greedily).
            # Group 3: (\}\s*) captures the closing "}" (with optional whitespace after it).
            # re.DOTALL ensures '.' matches newline characters.
            match = re.search(r'(ClassInfo\s*\{)(.*?)(\}\s*)', content, re.DOTALL)

            if match:
                class_info_prefix = match.group(1)   # e.g., "ClassInfo\n{" or "ClassInfo {"
                inner_text_original = match.group(2) # Content between { and }, preserving its original whitespace
                class_info_suffix = match.group(3)   # e.g., "}" or "}\n"

                print(f"'{filepath}': 'ClassInfo' block found. Adding new properties.")

                # Prepare the content before insertion:
                # If the original inner_text is not empty and the last non-whitespace character
                # is not already followed by a newline, add one. This ensures new content
                # always starts on a fresh line after existing properties.
                content_before_insertion = inner_text_original
                if content_before_insertion.strip() and not content_before_insertion.endswith('\n'):
                    content_before_insertion += "\n"
                # If inner_text_original is empty or only whitespace, no extra newline is needed here
                # because INSERTION_TEXT itself will provide the first line of content.

                # Construct the full new ClassInfo block.
                # We use class_info_prefix directly to preserve the original "ClassInfo {" formatting.
                # The INSERTION_TEXT is placed without leading indentation.
                # A newline `\n` is explicitly added after INSERTION_TEXT to ensure the closing brace
                # starts on a new line and maintains proper formatting.
                new_class_info_block = (
                    f"{class_info_prefix}"
                    f"{content_before_insertion}"  # Original inner content, preserved with potential newline
                    f"{INSERTION_TEXT}\n"          # New properties, no indent, followed by a newline
                    f"{class_info_suffix}"
                )

                # Replace the entire original ClassInfo block (as matched by `match.group(0)`)
                # with our newly constructed block.
                new_content = content.replace(match.group(0), new_class_info_block)

                # Write the updated content back to the file
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"'{filepath}': File updated successfully.")
            else:
                print(f"'{filepath}': 'isCustomBuild' not found in file, but 'ClassInfo' block structure not found. No changes made.")
        else:
            print(f"'{filepath}': 'isCustomBuild' already found anywhere in the file. No changes made.")

    except Exception as e:
        print(f"An error occurred while processing '{filepath}': {e}")

def process_all_mbch_files(root_dir):
    """
    Walks through the specified root directory and its subdirectories
    to find and modify all .mbch files.

    Args:
        root_dir (str): The starting directory to scan.
    """
    print(f"\n--- Scanning and processing .mbch files in '{root_dir}' and its subdirectories ---")
    found_files = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".mbch"):
                full_path = os.path.join(dirpath, filename)
                print(f"\nProcessing file: {full_path}")
                modify_mbch_file(full_path)
                found_files += 1
    if found_files == 0:
        print(f"No .mbch files found in '{root_dir}' or its subdirectories.")
    else:
        print(f"\n--- Finished processing {found_files} .mbch files. ---")


# --- Main execution ---
if __name__ == "__main__":
    # This will automatically process all .mbch files in the current directory
    # and all its subdirectories. No need to uncomment anything.
    process_all_mbch_files(os.getcwd())
