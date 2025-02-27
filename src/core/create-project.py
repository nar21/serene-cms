import os
import argparse
from distutils.dir_util import copy_tree


def main():
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument("--name", help="Name of the project", type=str)
    parser.add_argument(
        "--path", help="Directory path where project will be initialized", type=str
    )
    args = parser.parse_args()

    src_dir = "core/skeleton"
    dest_dir = args.path

    if os.path.isdir(dest_dir):
        print("Destination directory exists ✔")
    else:
        confirm_dest_create = input(
            "Destination directory does not exist ✖. Create now? (y/n): "
        )
        if confirm_dest_create.lower() == "y":
            os.makedirs(dest_dir)
        else:
            exit(0)

    confirm_init = input(
        f"Project will be initialized at {dest_dir}. Continue? (y/n): "
    )
    if confirm_init.lower() != "y":
        exit(0)

    if len(os.listdir(dest_dir)) > 0:
        raise Exception(f'Destination directory "{dest_dir}" is not empty. Exiting.')

    # Call function to copy directory skeleton
    copy_tree(src_dir, dest_dir)


if __name__ == "__main__":
    main()
