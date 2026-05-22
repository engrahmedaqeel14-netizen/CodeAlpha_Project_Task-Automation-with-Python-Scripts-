"""
Task 1: Move all .jpg files from source folder to destination folder.
Concepts: os, shutil, file handling
"""
import os
import shutil
from datetime import datetime

def move_jpg_files(source_folder, dest_folder):
    result = {"moved": [], "errors": [], "skipped": []}
    if not os.path.exists(source_folder):
        raise FileNotFoundError(f"Source folder not found: {source_folder}")
    os.makedirs(dest_folder, exist_ok=True)
    all_files = os.listdir(source_folder)
    jpg_files = [f for f in all_files if f.lower().endswith(('.jpg', '.jpeg'))]
    if not jpg_files:
        print("  No .jpg files found in source folder.")
        return result
    for filename in jpg_files:
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(dest_folder, filename)
        if os.path.exists(dst_path):
            name, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}{ext}"
            dst_path = os.path.join(dest_folder, filename)
            result["skipped"].append(f"Renamed duplicate: {filename}")
        try:
            shutil.move(src_path, dst_path)
            result["moved"].append(filename)
            print(f"  Moved: {filename}")
        except Exception as e:
            result["errors"].append(f"{filename}: {str(e)}")
            print(f"  Error moving {filename}: {e}")
    print(f"\n  Summary: {len(result['moved'])} moved, {len(result['errors'])} errors")
    return result

if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src = os.path.join(base, "sample_data", "images")
    dst = os.path.join(base, "output", "moved_images")
    print("=" * 50)
    print("  JPG FILE MOVER")
    print("=" * 50)
    print(f"  Source : {src}")
    print(f"  Dest   : {dst}\n")
    result = move_jpg_files(src, dst)
