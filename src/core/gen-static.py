from jinja2 import Template
import yaml
import os
from pathlib import Path
from slugify import slugify
import argparse


def generate_static_files(project_path: str):
    print(str(Path(project_path).resolve()))

    content_path = str(Path(project_path + "/content").resolve())
    static_target_path = str(Path(project_path + "/static").resolve())
    print(content_path, static_target_path)
    settings = yaml.safe_load(open(project_path + "/settings.yaml").read())

    for root, dirs, files in os.walk(content_path):
        source_path = root.split(os.sep)
        print("source_path: " + str(source_path))
        source_dir_str = root
        current_file = source_dir_str + "/index.yaml"
        print("source: " + current_file)
        if not os.path.exists(current_file):
            print("Does not exist: " + current_file + ". Skipping.")
            continue

        print("Parsing " + current_file)
        data = yaml.safe_load(open(current_file).read())
        if data.get("settings"):
            raise Exception(
                'Exception: "settings" cannot be set at the root of input yaml.'
            )

        data["page_slug"] = slugify(data["title"])  # if data["title"] else None

        target_dir_str = str(
            Path(
                os.path.join(
                    static_target_path, os.path.relpath(source_dir_str, content_path)
                )
            ).resolve()
        )

        data["page_url"] = settings["SITE_URL"] + "/" + "/".join(source_path[1:])
        data["settings"] = settings

        if not os.path.exists(target_dir_str):
            target_dir_obj = Path(target_dir_str)
            target_dir_obj.mkdir(parents=True, exist_ok=True)

        template = Template(open(project_path + "/templates/generic.html").read())
        output = template.render(data)
        target_file = target_dir_str + "/index.html"
        print("target: " + target_file)
        print("\n")
        open(target_file, "w").write(output)


def main():
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument(
        "--path", help="Directory path where project will be initialized", type=str
    )
    args = parser.parse_args()

    generate_static_files(args.path)


if __name__ == "__main__":
    main()
