#!/usr/bin/env python3
"""
Portfolio Update Script
Prepares the data, builds the React portfolio, and moves the files to the root directory for GitHub Pages deployment.
"""
import subprocess
import shutil
import os

def main():
    """Main function"""
    print("📊 Preparing portfolio data...")
    subprocess.run(["python3", "prepare_data.py"], check=True)
    print("✅ Portfolio data prepared successfully.")

    print("🚀 Building React portfolio...")
    subprocess.run(["npm", "run", "build"], cwd="react-portfolio", check=True)
    print("✅ React portfolio built successfully.")

    print("📁 Copying build files to the root directory...")

    source_dir = "react-portfolio/build"
    dest_dir = "."

    # Clean up the old _site directory if it exists
    if os.path.exists("_site"):
        print("  - Removing old `_site` directory.")
        shutil.rmtree("_site")

    # Copy files from the build directory to the root directory
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        dest_item = os.path.join(dest_dir, item)

        # If the destination item exists, remove it to ensure a clean copy
        if os.path.lexists(dest_item):
            if os.path.isdir(dest_item):
                shutil.rmtree(dest_item)
            else:
                os.remove(dest_item)

        # Copy the new item
        if os.path.isdir(source_item):
            shutil.copytree(source_item, dest_item)
        else:
            shutil.copy2(source_item, dest_item)

    print("✅ Build files copied to the root directory.")
    print("🎉 Portfolio update complete!")

if __name__ == "__main__":
    main()
