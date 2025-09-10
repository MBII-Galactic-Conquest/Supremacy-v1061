import os
import json # To handle dictionary storage in a file
import re   # For regular expression-based replacements

def process_mbtc_mbch_files(directory_path):
    """
    Traverses the specified directory, renames .mbtc and .mbch files
    by prepending 'test_' to their names, and updates the file content
    to reflect the new name, including cross-references to .mbch files
    within .mbtc files, using a temporary dictionary file.
    This version prevents 'test_test_' duplication using regex and idempotent renaming.

    Args:
        directory_path (str): The path to the directory to process.
    """
    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' not found.")
        return

    print(f"Starting to process files in: {directory_path}")

    temp_dict_filename = os.path.join(directory_path, "mbch_rename_map.tmp")
    mbch_base_name_map = {} # Stores original_clean_base_name: target_prefixed_base_name for all .mbch files
    
    # Initialize counters for summary
    mbtc_found_count_total = 0
    mbch_found_count_total = 0
    mbtc_processed_count = 0
    mbch_processed_count = 0

    # Phase 1: Process and Rename .mbch files, and store their mapping
    print("\nPhase 1: Processing and renaming .mbch files...")
    mbch_files_to_process = []
    
    # First, collect all .mbch files and prepare their new names (clean and prefixed)
    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith('.mbch'):
                mbch_found_count_total += 1
                old_file_path = os.path.join(root, filename)
                current_base_name, extension = os.path.splitext(filename)

                # Determine the original "clean" base name (without 'test_' if already present)
                original_clean_base_name = current_base_name
                if original_clean_base_name.startswith('test_'):
                    original_clean_base_name = original_clean_base_name[len('test_'):]
                
                # Determine the target prefixed base name
                target_prefixed_base_name = f"test_{original_clean_base_name}"
                new_file_path = os.path.join(root, target_prefixed_base_name + extension)
                
                mbch_files_to_process.append((old_file_path, new_file_path, original_clean_base_name, target_prefixed_base_name))
    
    if not mbch_files_to_process:
        print("  No .mbch files found to process in Phase 1.")
    
    for old_file_path, new_file_path, original_clean_base_name, target_prefixed_base_name in mbch_files_to_process:
        filename = os.path.basename(old_file_path)
        print(f"  Processing .mbch file '{filename}'...")

        try:
            # Read file content
            with open(old_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            modified_content = content
            
            # Replace file's own name in content, preventing test_test_ duplication
            # Only replace if the original_clean_base_name is NOT already preceded by 'test_'
            # Using re.escape to handle special characters in names
            pattern = r'\b(?<!test_)' + re.escape(original_clean_base_name) + r'\b'
            modified_content = re.sub(pattern, target_prefixed_base_name, modified_content)

            # Write to temp file
            temp_file_path = old_file_path + ".tmp"
            with open(temp_file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            
            # Check if rename is actually needed (idempotent rename)
            current_file_base_name = os.path.splitext(os.path.basename(old_file_path))[0]
            if current_file_base_name != target_prefixed_base_name:
                os.remove(old_file_path)
                os.rename(temp_file_path, new_file_path)
                print(f"    - Renamed to '{os.path.basename(new_file_path)}'")
            else:
                # If name is already correct, just replace the old file with the temp file
                os.remove(old_file_path)
                os.rename(temp_file_path, old_file_path) # Rename temp to old_file_path, effectively overwriting
                print(f"    - Filename already correct ('{os.path.basename(old_file_path)}'), content updated.")


            mbch_base_name_map[original_clean_base_name] = target_prefixed_base_name # Store the mapping
            mbch_processed_count += 1
            print(f"    - Content updated to reflect '{target_prefixed_base_name}'.")

        except FileNotFoundError:
            print(f"    Error: File '{old_file_path}' not found. Skipping.")
        except PermissionError:
            print(f"    Error: Permission denied for '{old_file_path}'. Skipping.")
        except Exception as e:
            print(f"    An unexpected error occurred while processing '{old_file_path}': {e}. Skipping.")

    # Save the MBCH map to a temporary file
    try:
        with open(temp_dict_filename, 'w', encoding='utf-8') as f:
            json.dump(mbch_base_name_map, f, indent=4)
        print(f"\n  MBCH rename map saved to '{os.path.basename(temp_dict_filename)}'.")
    except Exception as e:
        print(f"  Error: Could not save MBCH rename map to '{os.path.basename(temp_dict_filename)}': {e}")
        # If saving fails, we might as well proceed with an empty map for MBTC processing
        mbch_base_name_map = {} # Ensure it's empty for safety if saving failed


    # Phase 2: Load MBCH map and process .mbtc files
    print("\nPhase 2: Processing and renaming .mbtc files...")

    # Load the map from the temporary file (even if it was just written in this run, or from a previous run)
    loaded_mbch_map = {}
    if os.path.exists(temp_dict_filename):
        try:
            with open(temp_dict_filename, 'r', encoding='utf-8') as f:
                loaded_mbch_map = json.load(f)
            print(f"  MBCH rename map loaded from '{os.path.basename(temp_dict_filename)}'.")
        except json.JSONDecodeError:
            print(f"  Error: Could not decode JSON from '{os.path.basename(temp_dict_filename)}'. Using empty map.")
        except Exception as e:
            print(f"  Error: Could not load MBCH rename map from '{os.path.basename(temp_dict_filename)}': {e}. Using empty map.")
    else:
        print(f"  No MBCH rename map file '{os.path.basename(temp_dict_filename)}' found. Skipping cross-reference updates for .mbtc files.")

    # Collect all .mbtc files to process
    mbtc_files_to_process = []
    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith('.mbtc'):
                mbtc_found_count_total += 1
                old_file_path = os.path.join(root, filename)
                current_base_name, extension = os.path.splitext(filename)

                # Determine the original "clean" base name (without 'test_' if already present)
                original_clean_base_name = current_base_name
                if original_clean_base_name.startswith('test_'):
                    original_clean_base_name = original_clean_base_name[len('test_'):]
                
                # Determine the target prefixed base name
                target_prefixed_base_name = f"test_{original_clean_base_name}"
                new_file_path = os.path.join(root, target_prefixed_base_name + extension)
                
                mbtc_files_to_process.append((old_file_path, new_file_path, original_clean_base_name, target_prefixed_base_name))

    if not mbtc_files_to_process:
        print("  No .mbtc files found to process in Phase 2.")

    for old_file_path, new_file_path, original_clean_base_name, target_prefixed_base_name in mbtc_files_to_process:
        filename = os.path.basename(old_file_path)
        print(f"  Processing .mbtc file '{filename}'...")
        try:
            # Read the original content of the file
            with open(old_file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            modified_content = content

            # 1. Replace the .mbtc file's own original base name with its new base name within its content.
            # Using regex with negative lookbehind to prevent 'test_test_' duplication
            pattern_self = r'\b(?<!test_)' + re.escape(original_clean_base_name) + r'\b'
            modified_content = re.sub(pattern_self, target_prefixed_base_name, modified_content)

            # 2. Replace references to .mbch files using the loaded map.
            # This now explicitly targets only the base name of the .mbch file,
            # and uses regex with negative lookbehind.
            for orig_mbch_name_clean, new_mbch_name_prefixed in loaded_mbch_map.items():
                pattern_mbch_ref = r'\b(?<!test_)' + re.escape(orig_mbch_name_clean) + r'\b'
                modified_content = re.sub(pattern_mbch_ref, new_mbch_name_prefixed, modified_content)

            # Write to temp, remove old, rename temp or overwrite
            temp_file_path = old_file_path + ".tmp"
            with open(temp_file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)

            # Check if rename is actually needed (idempotent rename)
            current_file_base_name = os.path.splitext(os.path.basename(old_file_path))[0]
            if current_file_base_name != target_prefixed_base_name:
                os.remove(old_file_path)
                os.rename(temp_file_path, new_file_path)
                print(f"    - Renamed to '{os.path.basename(new_file_path)}'")
            else:
                # If name is already correct, just replace the old file with the temp file
                os.remove(old_file_path)
                os.rename(temp_file_path, old_file_path) # Rename temp to old_file_path, effectively overwriting
                print(f"    - Filename already correct ('{os.path.basename(old_file_path)}'), content updated.")

            mbtc_processed_count += 1
            print(f"    - Content updated to reflect '{target_prefixed_base_name}' and .mbch references.")

        except FileNotFoundError:
            print(f"    Error: File '{old_file_path}' not found during processing. Skipping.")
        except PermissionError:
            print(f"    Error: Permission denied for '{old_file_path}'. Skipping.")
        except Exception as e:
            print(f"    An unexpected error occurred while processing '{old_file_path}': {e}. Skipping.")

    # Phase 3: Cleanup
    print("\nPhase 3: Cleaning up temporary files...")
    if os.path.exists(temp_dict_filename):
        try:
            os.remove(temp_dict_filename)
            print(f"  Removed temporary file: '{os.path.basename(temp_dict_filename)}'.")
        except Exception as e:
            print(f"  Error: Could not remove temporary file '{os.path.basename(temp_dict_filename)}': {e}")


    print("\nFile processing complete.")
    print(f"Summary:")
    print(f"  Total files found: (.mbtc: {mbtc_found_count_total}, .mbch: {mbch_found_count_total})")
    print(f"  Files successfully processed: (.mbtc: {mbtc_processed_count}, .mbch: {mbch_processed_count})")

if __name__ == "__main__":
    my_directory = os.getcwd() # Default to the current working directory
    # my_directory = "C:\\Users\\youruser\\Documents\\MyProjectFiles"

    process_mbtc_mbch_files(my_directory)
