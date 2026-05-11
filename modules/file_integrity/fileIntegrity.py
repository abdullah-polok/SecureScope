"""
This module is used to detect changes in files and
helps monitor file integrity and identify unauthorized modifications
Commonly used in system security and forensic analysis

Development steps:
=> Select target file or directory
=> Generate hash values for files
=> Store original hashes securely
=> Recalculate hashes during scans
=> Compare old and new hash values
=> Report modified files
"""
import hashlib

# Function to create hash value of a file
def generate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        # Open file in binary read mode
        file = open(file_path, "rb")
        # Read file data
        data = file.read()
        # Update hash with file data
        sha256_hash.update(data)
        # Close file
        file.close()
        # Return final hash
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print("File not found!")
        return None

input_file_path = input("Enter file path: ")

# generate original hash
original_hash = generate_file_hash(input_file_path)

# print hash value
if original_hash:
    print("Original Hash:", original_hash)
    print(f"Original hash for {input_file_path}: {original_hash}")
    new_hash = generate_file_hash(input_file_path)
    if new_hash:
        print(f"New hash for {input_file_path}: {new_hash}")
        if original_hash == new_hash:
            print("File integrity no changes.")
        else:
            print("File integrity Changes.")