import os

def create_tarfile(file_name, folder_path):
    """Create tar.gz file"""
    try: 
        with tarfile.open(file_name, "w:gz") as tar:
            tar.add(folder_path, arcname=os.path.basename(folder_path))
    except:
        raise Exception("Something went wrong")

def create_folder(path):
    """Create folder"""
    try:
        os.mkdir(path)
    except:
        raise Exception("Something went wrong")

def create_file(file_path):
    """Create file"""
    try:
        with open(file_path, "w") as f:
            f.write("New file example\n")
    except:
        raise Exception("Something went wrong")
