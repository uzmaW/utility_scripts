import os
import sys
import zipfile

def unzip_files_in_directory(directory):
    # Iterate over all files and subdirectories in the given directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file has a .zip extension
            if file.endswith(".zip"):
                # Construct the full path to the zip file
                zip_file_path = os.path.join(root, file)

                # Specify the directory where the contents will be extracted
                extract_to_directory = os.path.join(root, file.replace(".zip", ""))

                # Create the extraction directory if it doesn't exist
                if not os.path.exists(extract_to_directory):
                    os.makedirs(extract_to_directory)

                # Unzip the file
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_to_directory)
                
                print(f"Unzipped {zip_file_path} to {extract_to_directory}")

# Specify the directory containing the nested zip files
#target_directory = "/path/to/your/directory"
#
# Call the function to unzip files in the specified directory
#unzip_files_in_directory(target_directory)
#
if __name__ == "__main__":
    # Check if a directory argument is provided
    if len(sys.argv) != 2:
        print("Usage: python unzip.py /path/to/your/directory")
        sys.exit(1)

    # Get the target directory from the command-line argument
    target_directory = sys.argv[1]

    # Call the function to unzip files in the specified directory
    unzip_files_in_directory(target_directory)
