#!/usr/bin/env python3
"""
Portfolio Update Script
Builds the React portfolio and moves the files to the correct location.
"""
import subprocess
import shutil
import os

def main():
    """Main function"""
    print("🚀 Building React portfolio...")
    subprocess.run(["npm", "run", "build"], cwd="react-portfolio", check=True)
    print("✅ React portfolio built successfully.")

    print("📁 Copying build files to _site...")
    if os.path.exists("_site"):
        shutil.rmtree("_site")
    shutil.copytree("react-portfolio/build", "_site")
    print("✅ Build files copied to _site.")

    print("🎉 Portfolio update complete!")

if __name__ == "__main__":
    main()
