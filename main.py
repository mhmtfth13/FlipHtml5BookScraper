import requests
from PIL import Image
from io import BytesIO
import os
from concurrent.futures import ThreadPoolExecutor

# Base URL for the images
base_url = "https://online.fliphtml5.com/tsyqb/vxvo/files/large/{}.webp"

# Range of image numbers
start = 1
end = 305
total_images = end - start + 1

# Define standard paper size (A4) dimensions (width x height in pixels at 300 DPI)
A4_WIDTH, A4_HEIGHT = 2480, 3508

def download_image(i):
    url = base_url.format(i)
    response = requests.get(url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.thumbnail((A4_WIDTH, A4_HEIGHT), Image.LANCZOS)
        return img
    else:
        print(f"Failed to download image from {url}")
        return None

# Download images concurrently
images = []
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(download_image, i) for i in range(start, end + 1)]
    
    for i, future in enumerate(futures):
        img = future.result()
        if img:
            images.append(img)
        
        # Calculate and display progress
        progress = ((i + 1) / total_images) * 100
        print(f"Progress: {progress:.2f}%")

# Convert images to PDF
if images:
    # Define the output PDF path
    pdf_path = r"C:\Users\!!DOSYAYOLUNUZ!!\output.pdf"
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    
    # Save images as a PDF
    images[0].save(pdf_path, save_all=True, append_images=images[1:])
    print(f'PDF saved as {pdf_path}')
else:
    print("No images were downloaded.")
