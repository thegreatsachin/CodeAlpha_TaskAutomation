# Automated File Mover



This Python script automates the repetitive task of moving all `.jpg` and `.jpeg` image files from a source folder to a destination folder.



## Goal



The purpose of this script is to provide a simple solution for organizing image files by automatically relocating them. This demonstrates basic file system automation using Python.



## Features



*   **Automatic Folder Creation:** If the source or destination folders do not exist, the script creates them.

*   **File Filtering:** Specifically targets files with `.jpg` or `.jpeg` extensions.

*   **Safe Moving:** Uses Python's `shutil` library to safely move files.

*   **User-Friendly Feedback:** Prints the names of the files as they are moved and provides a summary at the end.



## How to Use



1.  Clone or download the repository to your local machine.

2.  Run the script once to create the necessary folders:

```

python file_mover.py

```

3.  A folder named `source_images` will be created. Place all the `.jpg` or `.jpeg` files you want to move into this folder.

4.  Run the script again:

```

python file_mover.py

```

5.  All image files will be moved from `source_images` to a new `destination_images` folder.



## Key Concepts Used



This project utilizes Python's built-in libraries for file system operations:

*   **`os` module:** Used to create directories (`os.makedirs`), check for their existence (`os.path.exists`), and list directory contents (`os.listdir`).

*   **`shutil` module:** Used to perform the file moving operation (`shutil.move`).



