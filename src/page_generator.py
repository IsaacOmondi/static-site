import os

from markdown_blocks import markdown_to_html_node
from utils import extract_title


def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)



def generate_pages_recursive(current_content_path, template_path, current_dest_path, basepath):
    print(f"Processing directory: {current_content_path}")

    if not os.path.exists(current_content_path):
        print(f"Error: Content directory not found at {current_content_path}")
        return

    dir_contents = os.listdir(current_content_path)

    os.makedirs(current_dest_path, exist_ok=True)

    for item_name in dir_contents:
        src_item_path = os.path.join(current_content_path, item_name)
        dest_item_path_base = os.path.join(current_dest_path, item_name)

        if os.path.isfile(src_item_path):
            if item_name.endswith(".md"):
                dest_html_path = dest_item_path_base[:-3] + ".html"
                generate_page(src_item_path, template_path, dest_html_path, basepath)

        elif os.path.isdir(src_item_path):
            generate_pages_recursive(src_item_path, template_path, dest_item_path_base, basepath)

