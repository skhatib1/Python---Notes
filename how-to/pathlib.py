import sys
from pathlib import Path

# - Add to a path
directory_path = Path("/home/user/directory/")
file_name = "myFile.txt"
file_path = directory_path/file_name

# - Open file in a path (path must be a type str)
openFile = open(str(file_path), "a")

# - Write text to file
openFile.write("test123")

# - Close file
openFile.close()

# - Create an empty file
file_path.touch()


# - Returns True, if path exists
file_path.exists()
directory_path.exists()

# - Returns True if it is a file
file_path.is_file()

# - Returns True if it is a directory
directory_path.is_dir()
