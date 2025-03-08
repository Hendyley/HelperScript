import os
import shutil

def convert_to_txt(source_path, destination_path):
    # Walk through the directory tree
    for root, dirs, files in os.walk(source_path):
        # Create the corresponding directory structure in the destination folder
        relative_path = os.path.relpath(root, source_path)
        dest_dir = os.path.join(destination_path, relative_path)
        os.makedirs(dest_dir, exist_ok=True)
        
        for file in files:
            # Check if the file is not a directory
            if not os.path.isdir(os.path.join(root, file)):
                # Split the file name and extension
                filename, file_extension = os.path.splitext(file)
                # If the file is not already a .txt file
                if file_extension != '.txt':
                    # Rename the file to .txt extension
                    new_file_name = filename + '.txt'
                    # Copy the file to the destination folder
                    shutil.copy(os.path.join(root, file), os.path.join(dest_dir, new_file_name))
                    print(f"Converted '{file}' to '{new_file_name}'")

# Get source and destination paths from the user
source_path = r"E:\Project\Android\MDPAndroidController\MDPAndroidController\app\src\main\res"
destination_path = r"C:\Users\Hendy\OneDrive\Desktop\trash\MDP_Android_submission\res"

# Call the function to convert files to .txt
convert_to_txt(source_path, destination_path)
