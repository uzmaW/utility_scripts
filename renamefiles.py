import os

target_dir = "."

for path, dirs, files in os.walk(target_dir):
    for file in files:
        filename, ext = os.path.splitext(file)
        print(filename,ext)