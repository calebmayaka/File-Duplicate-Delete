import os
import hashlib

def hash_file(file_path):
    """Generate and return the hash value of a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buffer = file.read(65536)  # Read file in 64kb chunks
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = file.read(65536)
    return hasher.hexdigest()

def find_duplicate_files(folder):
    """Find and return a dictionary containing duplicate files."""
    file_hash_dict = {}
    duplicate_files = {}

    for dirpath, _, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = hash_file(file_path)

            if file_hash in file_hash_dict:
                duplicate_files.setdefault(file_hash, []).append(file_path)
            else:
                file_hash_dict[file_hash] = file_path

    
    return {key: value for key, value in duplicate_files.items() if len(value) > 1}


def delete_duplicate_files(duplicate_files):
    """Delete duplicate files except for the first occurrence."""
    for files_list in duplicate_files.values():
        for file_path in files_list[1:]:
            os.remove(file_path)
            print(f"Deleted: {file_path}")

# Replace 'folder_path' with the path of your folder containing duplicate files
folder_path = 'path_to_your_folder'

duplicate_files = find_duplicate_files(folder_path)
delete_duplicate_files(duplicate_files)
