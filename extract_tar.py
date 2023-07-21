import tarfile
import os
import argparse

def extract_tar(tar_file_path, destination_folder):
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Extract the .tar file
    with tarfile.open(tar_file_path, 'r') as tar:
        tar.extractall(destination_folder)

        # Print the list of extracted files
        extracted_files = tar.getnames()
        print("Extracted files:")
        print(extracted_files)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract files from a .tar archive.")
    parser.add_argument("tar_file_path", help="Path to the .tar file.")
    parser.add_argument("destination_folder", help="Destination folder where the files will be extracted.")
    args = parser.parse_args()

    extract_tar(args.tar_file_path, args.destination_folder)
