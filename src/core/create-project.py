import os
import argparse
from distutils.dir_util import copy_tree

def main():
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument("--name", help="Name of the project", type=str)
    parser.add_argument("--path", help="Directory path where project will be initialized", type=str)
    args = parser.parse_args()

    src_dir = "core/skeleton"
    dest_dir = args.path

    confirm_init = input(f"Project will be initialized at {dest_dir}. Continue? (y/n): ")
    if confirm_init.lower() != "y":
        exit(0)


    if len(os.listdir(dest_dir)) > 0:
        raise Exception(f"Destination directory \"{dest_dir}\" is not empty. Exiting.")

    # Call function to copy directory skeleton
    copy_tree(src_dir, dest_dir)


if __name__ == "__main__":
    main()
