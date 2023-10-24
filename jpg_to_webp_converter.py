from PIL import Image
import glob
import os

jpg_files = glob.glob("*.jpg")

for jpg_file in jpg_files:
    image = Image.open(jpg_file)
    image = image.convert('RGB')
    webp_file = os.path.splitext(jpg_file)[0] + '.webp'
    image.save(webp_file, 'webp', optimize=True, quality=10)

print(f"Conversion completed for {len(jpg_files)} JPEG files.")
