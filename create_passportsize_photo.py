import sys
import os

"""   this file is using photoidmagick package """

def run_shell_command(file_name):
   command = f"photoidmagick -f {file_name} -s 827x1063 --allow-oblique-face"
   response= os.system(command)
   if response == 0:
      print ('passport size ',file_name, ' created')
   else:
      print ('error occurred')



if __name__ == "__main__":
    # Check if a file argument is provided
    if len(sys.argv) != 2:
        print("Usage: python create_passportsize_photo.py /path/to/your/file")
        sys.exit(1)

    # Get the target file from the command-line argument
    target_file = sys.argv[1]

    # Call the function to remove background
    run_shell_command(target_file)
