import sys
from pathlib import Path
from normalize import normalize
import json


def classify(file_name, file="extensions.json"):
    '''Return file classification

    file_name -- str input filename
    file -- json with file types and extensions

    returns str output classification of file
    returns None if extension is unknown
    '''
    with open(file, "r") as f:
        types = json.loads(f.read())
    for type, extensions in types.items():
        for extension in extensions:
            ext = file_name.suffix
            if ext in extensions:
                return type
    log_unknown_ext(file_name.suffix)
    return None


def log_unknown_ext(ext):
    '''log unknown extensions

    ext -- str with extension name'''
    if not ext in unknown_extensions:
        unknown_extensions.append(ext)


def filename_to_str(filename):
    '''convert and split path obj to string tuple'''
    return (str(filename.stem), str(filename.suffix))


def rename_files(path, root_path):
    '''rename files and folders'''
    name = filename_to_str(path)[0]
    ext = filename_to_str(path)[1]
    normalized_name = normalize(name)
    counter = 1
    new_path = root_path / f"{normalized_name}{ext}"
    try:
        path.resolve().rename(new_path)
    except OSError:
        while new_path.exists():
            char = counter * "_"
            new_path = root_path / f"{normalized_name}_{char}{ext}"
            counter += 1
        path.resolve().rename(new_path)
    except:
        print("error while renaming")


def filetypes():
    return ["archives", "video", "audio", "documents", "images"]


def process_iffolder(path, root_path):
    is_empty = not any(path.iterdir())
    if not path.stem in filetypes():
        if is_empty:
            path.rmdir()
        else:
            parse_main(path, root_path)


def process_iffile(path, root_path):
    filetype = classify(path)
    print(f"Found following file: {path} with filetype {filetype}")
    move(path, root_path, filetype)


def move(path, root_path, filetype):
    if filetype:  # handler for known types
        destination_folder = Path(root_path / filetype)
        destination_folder.mkdir(parents=True, exist_ok=True)
        try:
            path.resolve().rename(
                f"{root_path}\{filetype}\{path.name}")
        except:
            print(f"file move failed : {filetype}")
    else:
        print(f"Error, not moving {path}")


def parse_main(path, root_path):
    '''Parsing folder index recursively and making major decisions
    path -- str name of folder
    '''
    try:
        path.iterdir()
        for file_path in path.iterdir():
            rename_files(file_path, root_path)
            if file_path.is_dir():
                process_iffolder(file_path, root_path)
            else:  # from here all file operations
                process_iffile(file_path, root_path)
    except FileNotFoundError:
        print("Folder not found")


# main loop
if __name__ == '__main__':
    for p in sys.argv[1:]:
        unknown_extensions = []
        path = Path(p)
        parse_main(path, path)
        print(f"Unknown extensions are:", " ".join(unknown_extensions))
