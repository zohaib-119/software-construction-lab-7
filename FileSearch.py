import os

def search_file(directory, target_file):
    """Recursively searches for the target file in the given directory."""
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print(f"Invalid directory: {directory}")
        return False

    for root, _, files in os.walk(directory):
        if target_file in files:
            print(f"File found: {os.path.join(root, target_file)}")
            return True
    return False
