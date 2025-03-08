import os
import shutil
from rembg import remove
from PIL import Image

def remove_background_from_directory(input_dir, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Supported image file formats
    image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}
    
    # Process each file in the directory
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        
        # Check if it's a file and has a valid image extension
        if os.path.isfile(file_path) and os.path.splitext(filename)[1].lower() in image_extensions:
            try:
                with Image.open(file_path) as img:
                    output = remove(img)  # Remove background
                    output_path = os.path.join(output_dir, filename)
                    output.save(output_path)
                    print(f"Processed: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    input_directory = r"E:\Assets\4 Color Game\Chess"  # Use raw string (r"...")
    output_directory = r"E:\Assets\4 Color Game\Chess\Removed_BG"  # Use raw string (r"...")

    remove_background_from_directory(input_directory, output_directory)
    print("Background removal completed.")

