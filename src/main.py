import os
import sys
import shutil

from htmlfunctions import markdown_to_html_node
from mdfunctions import extract_title

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    print(basepath)
    create_docs_dir()
    generate_page_recursive("./content", "./template.html", "./docs", basepath)

def create_docs_dir():
    cwd = os.getcwd()
    static_path = os.path.join(cwd, "./static")
    public_path = os.path.join(cwd, "./docs")

    #print(f"Working dir: {cwd}")
    #print(f"Source: {static_path}")
    #print(f"Dest: {public_path}")

    if os.path.exists(public_path):
        #print(f"Removing {public_path}")
        shutil.rmtree(public_path)
    
    copy_dir_contents(static_path, public_path)
    
def copy_dir_contents(source, dest):
    contents = os.listdir(source)
    if not os.path.exists(dest):
        #print(f"Creating directory {dest}")
        os.mkdir(dest)
    for content in contents:
        source_path = os.path.join(source, content)
        dest_path = os.path.join(dest, content)
        if os.path.isfile(source_path):
            #print(f"Copying {content} in {source}")
            shutil.copy(source_path, dest_path)
        if os.path.isdir(source_path):
            #print(f"Copying directory to {dest_path}")
            copy_dir_contents(source_path, dest_path)

def generate_page(from_path, template_path, dest_path, basepath):
    page = None
    print(f"Generating page from {from_path} to {dest_path}, using {template_path}")
    with open(from_path) as file:
        markdown = file.read()
    
    with open(template_path) as file:
        template = file.read()
    
    title = extract_title(markdown)
    html_node = markdown_to_html_node(markdown)
    content = html_node.to_html()

    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", content)
    page = page.replace('href="/', f'href="{basepath}')
    page = page.replace('src="/', f'src="{basepath}')

    if not os.path.exists(os.path.dirname(dest_path)):
        os.mkdir(os.path.dirname(dest_path))
    
    if page:
        with open(dest_path, "w") as file:
            file.write(page)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    directory = os.listdir(dir_path_content)
    for dir in directory:
        if os.path.isfile(os.path.join(dir_path_content, dir)):
            file_path = os.path.join(dir_path_content, dir)
            filename, extension = os.path.splitext(file_path)
            if extension == ".md":
                generate_page(file_path, template_path, os.path.join(dest_dir_path, "index.html"), basepath)
        else:
            if not os.path.exists(os.path.join(dest_dir_path, dir)):
                os.mkdir(os.path.join(dest_dir_path, dir))
            generate_page_recursive(os.path.join(dir_path_content, dir), template_path, os.path.join(dest_dir_path, dir), basepath)

main()