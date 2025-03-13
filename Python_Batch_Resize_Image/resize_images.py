import os
from rembg import remove
from PIL import Image

def remove_background_and_resize(input_dir, output_dir, target_size):
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
                    # output = remove(img)  # Remove background
                    # Resize the image to the target size
                    output = img
                    output = output.resize(target_size)
                    output_path = os.path.join(output_dir, filename)
                    output.save(output_path)
                    print(f"Processed and resized: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

################## Edit this!! 
if __name__ == "__main__":
    input_directory = r""  # Use raw string (r"...")
    output_directory = r""  # Use raw string (r"...")
    target_size = (103, 362)  # Specify your target size here (width, height)

    remove_background_and_resize(input_directory, output_directory, target_size)
    print("Resizing completed.")
