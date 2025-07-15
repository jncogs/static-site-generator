import os
import shutil

def main():
    create_public_dir()

def create_public_dir():
    cwd = os.getcwd()
    static_path = os.path.join(cwd, "static")
    public_path = os.path.join(cwd, "public")

    print(f"Working dir: {cwd}")
    print(f"Source: {static_path}")
    print(f"Dest: {public_path}")

    if os.path.exists(public_path):
        print(f"Removing {public_path}")
        shutil.rmtree(public_path)
    
    copy_dir_contents(static_path, public_path)
    
def copy_dir_contents(source, dest):
    contents = os.listdir(source)
    if not os.path.exists(dest):
        print(f"Creating directory {dest}")
        os.mkdir(dest)
    for content in contents:
        source_path = os.path.join(source, content)
        dest_path = os.path.join(dest, content)
        if os.path.isfile(source_path):
            print(f"Copying {content} in {source}")
            shutil.copy(source_path, dest_path)
        if os.path.isdir(source_path):
            print(f"Copying directory to {dest_path}")
            copy_dir_contents(source_path, dest_path)

main()