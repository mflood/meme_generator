
from typing import List
import os

def is_image_file(filename):
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def find_files(directory: str) -> List[str]:
    found_files = []
    for root, _, files in os.walk(directory):
        files = [os.path.join(root, f) for f in files]
        found_files.extend(files)
    return found_files

def find_image_files(directory: str) -> List[str]:
    all_files = find_files(directory=directory)
    image_files = [f for f in all_files if is_image_file(f)]
    return image_files

