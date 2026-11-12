#!/usr/bin/env python3
"""
FABFaddons Shopify Online Store 2.0 Theme Packager
Packages the root Shopify theme folders into FABFaddons-Premium-Shopify-Theme.zip
"""
import os
import zipfile

THEME_DIRS = ['assets', 'config', 'layout', 'locales', 'sections', 'snippets', 'templates']
OUTPUT_ZIPS = [
    'FABFaddons-Premium-Shopify-Theme.zip',
    'public/FABFaddons-Premium-Shopify-Theme.zip',
    'FABFaddons-Shopify-Theme.zip',
    'public/FABFaddons-Shopify-Theme.zip'
]

def build_zip():
    os.makedirs('public', exist_ok=True)
    
    for zip_path in OUTPUT_ZIPS:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for theme_dir in THEME_DIRS:
                if not os.path.isdir(theme_dir):
                    print(f"Warning: {theme_dir} directory missing!")
                    continue
                for root, _, files in os.walk(theme_dir):
                    for file in sorted(files):
                        full_path = os.path.join(root, file)
                        arcname = os.path.relpath(full_path, '.')
                        zf.write(full_path, arcname)
                        
        # Test integrity
        with zipfile.ZipFile(zip_path, 'r') as test_zf:
            bad_file = test_zf.testzip()
            if bad_file:
                raise RuntimeError(f"Corrupted file in {zip_path}: {bad_file}")
            file_list = test_zf.namelist()
            print(f"Validated {zip_path}: {len(file_list)} files, {os.path.getsize(zip_path)} bytes")

if __name__ == '__main__':
    build_zip()
