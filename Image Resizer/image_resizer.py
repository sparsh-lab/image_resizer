import os
from PIL import Image

# ===== CONFIGURATION =====
input_folder = 'images/'              # Folder containing original images
output_folder = 'resized_images/'     # Folder to save resized images
new_size = (800, 600)                 # Desired size (width, height)
output_format = 'JPEG'               # Choose from: 'JPEG', 'PNG', etc.

# ===== CREATE OUTPUT FOLDER IF NEEDED =====
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ===== BATCH PROCESSING IMAGES =====
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.' + output_format.lower())

        with Image.open(input_path) as img:
            resized_img = img.resize(new_size)
            resized_img.save(output_path, output_format)

print("✅ All images have been resized and saved.")
