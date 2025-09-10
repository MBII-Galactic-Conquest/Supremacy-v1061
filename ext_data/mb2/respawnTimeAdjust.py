import os
import re

def update_respawn_time_in_mbch_files(root_directory):
    """
    Traverses the specified root_directory and its subdirectories to find .mbch files.
    For each .mbch file, it updates or adds the 'respawnCustomTime' setting to '10000'.
    It ensures the line is placed within the first ClassInfo{} block and uses a tab
    between 'respawnCustomTime' and its value, without any leading indentation.

    Args:
        root_directory (str): The starting directory to search for .mbch files.
    """
    print(f"Starting to process .mbch files in: {root_directory}")

    # Regex to find the respawnCustomTime line, accommodating various whitespace (spaces or tabs)
    # and any existing value after 'respawnCustomTime'.
    respawn_pattern = re.compile(r"^\s*respawnCustomTime[\s\t]+.*$", re.IGNORECASE)
    
    # The new line to ensure is in the file, with a tab character
    new_respawn_line_content = "respawnCustomTime\t10000"

    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.lower().endswith(".mbch"):
                filepath = os.path.join(dirpath, filename)
                print(f"Processing file: {filepath}")

                lines = []
                respawn_time_found = False
                file_modified = False

                try:
                    # Read the file content
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = f.readlines()

                    # First pass: Check if respawnCustomTime already exists and update if necessary
                    for i, line in enumerate(lines):
                        if respawn_pattern.match(line):
                            # Compare stripped line to ignore leading/trailing whitespace during comparison
                            if line.strip() != new_respawn_line_content:
                                # When updating, ensure no leading whitespace is present
                                lines[i] = new_respawn_line_content + "\n"
                                file_modified = True
                                print(f"  - Updated 'respawnCustomTime' in line {i+1} to '{new_respawn_line_content}'.")
                            respawn_time_found = True
                            break # Assume only one respawnCustomTime line for simplicity

                    # If respawnCustomTime was not found, add it inside the first ClassInfo{} block
                    if not respawn_time_found:
                        class_info_block_start_index = -1
                        
                        # Find the start of the ClassInfo block.
                        # It can be "ClassInfo {" on one line, or "ClassInfo" on one line and "{" on the next.
                        for i, line in enumerate(lines):
                            if "ClassInfo" in line:
                                if "{" in line: # Case: "ClassInfo {" on the same line
                                    class_info_block_start_index = i
                                    break
                                elif i + 1 < len(lines) and "{" in lines[i+1]: # Case: "ClassInfo" then "{" on next line
                                    class_info_block_start_index = i + 1 # Point to the line with "{"
                                    break

                        if class_info_block_start_index != -1:
                            # Now, starting from after the opening brace, find the corresponding closing brace
                            brace_level = 1 # We've accounted for the ClassInfo opening brace
                            insert_at_index = -1 
                            
                            for i in range(class_info_block_start_index + 1, len(lines)):
                                line = lines[i]
                                # Count braces to find the true closing brace of the current ClassInfo block
                                brace_level += line.count("{")
                                brace_level -= line.count("}")

                                if brace_level == 0: # Found the closing brace for the ClassInfo block
                                    insert_at_index = i # Insert *before* this closing brace
                                    break
                            
                            if insert_at_index != -1:
                                # No indentation for the new line, as requested
                                lines.insert(insert_at_index, new_respawn_line_content + "\n")
                                file_modified = True
                                print(f"  - Added '{new_respawn_line_content}' inside the first ClassInfo{{}} block with no leading indentation.")
                            else:
                                # Fallback: ClassInfo opening brace found, but no matching closing brace within the file
                                # Add to the very end of the file in this rare case.
                                lines.append(new_respawn_line_content + "\n")
                                file_modified = True
                                print(f"  - Added '{new_respawn_line_content}' to the end of the file (ClassInfo{{}} opening brace found, but no matching closing brace).")
                        else:
                            # Fallback: No ClassInfo block (or its opening brace) was found at all
                            # Add to the very end of the file.
                            lines.append(new_respawn_line_content + "\n")
                            file_modified = True
                            print(f"  - Added '{new_respawn_line_content}' to the end of the file (ClassInfo{{}} block not found).")
                    
                    # If any modifications were made, write the content back to the file
                    if file_modified:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        print(f"  - File saved successfully.")
                    else:
                        print(f"  - No changes needed for this file.")

                except IOError as e:
                    print(f"  - Error reading or writing file {filepath}: {e}")
                except Exception as e:
                    print(f"  - An unexpected error occurred with file {filepath}: {e}")

    print("\nProcessing complete.")

if __name__ == "__main__":
    current_directory = os.getcwd()
    update_respawn_time_in_mbch_files(current_directory)
