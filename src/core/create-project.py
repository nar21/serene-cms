import os
import argparse
from distutils.dir_util import copy_tree

def copy_skeleton(src, dest):
    """Copy the directory structure (skeleton) from src to dest."""
    # Check if source directory exists
    if not os.path.exists(src):
        print(f"Source directory {src} does not exist.")
        return

    # Create destination directory if it doesn't exist
    if not os.path.exists(dest):
        os.makedirs(dest)
        print(f"Destination directory {dest} created.")

    # Walk through the source directory
    for root, dirs, files in os.walk(src):
        # Get the relative path from source
        relative_path = os.path.relpath(root, src)
        # Create corresponding directories in the destination
        dest_dir = os.path.join(dest, relative_path)

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            print(f"Created directory: {dest_dir}")

        # No need to copy files, just replicate the structure
        # files are skipped to create an empty skeleton


def main():
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument("--name", help="Name of the project", type=str)
    parser.add_argument("--path", help="Directory path where project will be initialized", type=str)
    args = parser.parse_args()

    src_dir = "core/skeleton"
    dest_dir = args.path

    # Call function to copy directory skeleton
    copy_tree(src_dir, dest_dir)


if __name__ == "__main__":
    main()
