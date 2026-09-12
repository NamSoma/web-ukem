from PIL import Image
import os

try:
    img_path = r'e:\งาน\ลองทำ\union-logo.png'
    backup_path = r'e:\งาน\ลองทำ\union-logo-backup.png'
    
    # Open the image
    img = Image.open(img_path)
    
    # Save a backup just in case
    if not os.path.exists(backup_path):
        img.save(backup_path)
        
    w, h = img.size
    
    # The U logo is on the left. It's roughly a square.
    # We crop a square from the left (0, 0, h*1.1, h) to include a bit of margin if needed, 
    # but a perfect square (h x h) is usually safest for these logos.
    crop_width = int(h * 1.05) # slightly wider than a perfect square just in case
    if crop_width > w:
        crop_width = w
        
    cropped = img.crop((0, 0, crop_width, h))
    
    # Save it back
    cropped.save(img_path)
    print(f"Success! Cropped image to {crop_width}x{h}")
except Exception as e:
    print(f"Error: {e}")
