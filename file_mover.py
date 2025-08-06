import os
import shutil

def move_jpg_files():
    """
    Automates moving all .jpg files from a source folder to a destination folder.
    """
    # Define the source and destination folder names.
    # The script will look for these folders in the same directory where it runs.
    source_folder = 'source_images'
    destination_folder = 'destination_images'

    # --- Setup: Create folders if they don't exist ---
    # Create the source folder if it's missing, and prompt the user to add files.
    if not os.path.exists(source_folder):
        os.makedirs(source_folder)
        print(f"Created folder: '{source_folder}'")
        print(f"Please add some .jpg files to the '{source_folder}' folder and run the script again.")
        return # Exit the script so the user can add files.

    # Create the destination folder if it's missing.
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created folder: '{destination_folder}'")

    # --- Main Logic: Find and move files ---
    # Get a list of all files in the source folder.
    try:
        files = os.listdir(source_folder)
    except FileNotFoundError:
        print(f"Error: The source folder '{source_folder}' was not found.")
        return
        
    moved_count = 0
    # Loop through all the files.
    for file_name in files:
        # Check if the file ends with .jpg or .jpeg (case-insensitive).
        if file_name.lower().endswith(('.jpg', '.jpeg')):
            # Create the full path for the source and destination.
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)
            
            # Move the file.
            shutil.move(source_path, destination_path)
            print(f"Moved: {file_name}")
            moved_count += 1
            
    if moved_count == 0:
        print(f"No .jpg files were found to move in '{source_folder}'.")
    else:
        print(f"\nProcess complete. Moved {moved_count} file(s) to '{destination_folder}'.")

# Run the script
if __name__ == "__main__":
    move_jpg_files()
