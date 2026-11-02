import os
import shutil
import sys

from page_generator import generate_pages_recursive
from utils import copy_files_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main() -> None:
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        if not basepath.endswith('/'):
                basepath += '/'

    dest_dir_path = "./docs"

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dest_dir_path)

    print("Generating pages...")
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath)
    
    print("Static site generation finished.")

main()