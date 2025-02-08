import os
import difflib
from tabulate import tabulate # type: ignore

def get_current_directory():
    """Returns the current working directory."""
    cwd = os.getcwd()
    print(f"📂 Current Directory: {cwd}")
    return cwd

def read_file(filepath):
    """Reads the content of a file and returns it as a list of lines."""
    try:
        with open(filepath, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"❌ Error: File not found -> {filepath}")
        return []

def compare_files(precheck_data, postcheck_data):
    """Compares two file contents and returns old (-) and new (+) changes."""
    diff = list(difflib.ndiff(precheck_data, postcheck_data))

    old_changes = [line[2:].strip() for line in diff if line.startswith("- ")]  # Removed
    new_changes = [line[2:].strip() for line in diff if line.startswith("+ ")]  # Added

    return old_changes, new_changes

def format_and_print_table(old_changes, new_changes):
    """Formats and prints the differences in table format."""
    max_len = max(len(old_changes), len(new_changes))

    # Ensure both lists have equal length
    old_changes.extend([""] * (max_len - len(old_changes)))
    new_changes.extend([""] * (max_len - len(new_changes)))

    changes = list(zip(new_changes, old_changes))

    if any(new_changes) or any(old_changes):
        print("\n❌ Changes detected! Showing differences...\n")
        table_headers = ["New Changes (+)", "Old Changes (-)"]
        print(tabulate(changes, headers=table_headers, tablefmt="grid"))
    else:
        print("\n✅ No differences found between precheck and postcheck outputs.")

def main():
    cwd = get_current_directory()

    # Define file paths
    precheck_file = os.path.join(cwd, "precheck_outputs.txt")
    postcheck_file = os.path.join(cwd, "postcheck_outputs.txt")

    # Read file contents
    precheck_data = read_file(precheck_file)
    postcheck_data = read_file(postcheck_file)

    if not precheck_data or not postcheck_data:
        print("❌ Comparison failed due to missing files.")
        return

    # Compare files and get changes
    old_changes, new_changes = compare_files(precheck_data, postcheck_data)

    # Print formatted table
    format_and_print_table(old_changes, new_changes)

if __name__ == "__main__":
    main()


#############################################################################################################
"""
without Function comparision
"""
# import os
# import difflib
# from tabulate import tabulate

# # Step 1: Get current working directory dynamically
# cwd = os.getcwd()
# print(f"📂 Current Directory: {cwd}")

# # Step 2: Define file paths dynamically
# precheck_file = os.path.join(cwd, "precheck_outputs.txt")
# postcheck_file = os.path.join(cwd, "postcheck_outputs.txt")

# # Step 3: Read file contents
# with open(precheck_file, "r") as pre:
#     precheck_data = pre.readlines()

# with open(postcheck_file, "r") as post:
#     postcheck_data = post.readlines()

# # Step 4: Compare the two files using difflib
# diff = list(difflib.ndiff(precheck_data, postcheck_data))

# # Step 5: Separate changes into old (`-`) and new (`+`) lists
# old_changes = []
# new_changes = []

# for line in diff:
#     if line.startswith("- "):  # Removed from pre-check
#         old_changes.append(line[2:].strip())
#     elif line.startswith("+ "):  # Added in post-check
#         new_changes.append(line[2:].strip())

# # Ensure both lists are of the same length for tabulate alignment
# max_len = max(len(old_changes), len(new_changes))

# # Fill shorter list with empty strings
# old_changes.extend([""] * (max_len - len(old_changes)))
# new_changes.extend([""] * (max_len - len(new_changes)))

# # Combine both sides into a table
# changes = list(zip(new_changes, old_changes))

# # Step 6: Print table
# if any(new_changes) or any(old_changes):
#     print("\n❌ Changes detected! Showing differences...\n")
#     table_headers = ["New Changes (+)", "Old Changes (-)"]
#     print(tabulate(changes, headers=table_headers, tablefmt="grid"))
# else:
#     print("\n✅ No differences found between precheck and postcheck outputs.")
