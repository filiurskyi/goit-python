import sys
from pathlib import Path
from normalize import normalize
from threading import Thread
import json
import shutil


def classify(file_name, file="extensions.json"):
    """Return file classification

    file_name -- str input filename
    file -- json with file types and extensions

    returns str output classification of file
    returns None if extension is unknown
    """
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
    """log unknown extensions

    ext -- str with extension name"""
    if not ext in unknown_extensions:
        unknown_extensions.append(ext)


def filename_to_str(filename):
    """convert and split path obj to string tuple"""
    return (str(filename.stem), str(filename.suffix))


def rename_files(path):
    """rename files and folders"""
    name = filename_to_str(path)[0]
    ext = filename_to_str(path)[1]
    if not classify(path):
        return path
    normalized_name = normalize(name)
    counter = 0
    new_path = path.parent / f"{normalized_name}{ext}"
    try:
        path.resolve().rename(new_path)
        return new_path
    except OSError:
        while new_path.exists():
            char = counter * "_"
            new_path = path.parent / f"{normalized_name}_{char}{ext}"
            counter += 1
        path.resolve().rename(new_path)
        return new_path
    except:
        print("error while renaming", new_path)


def filetypes():
    return ["archives", "video", "audio", "documents", "images"]


def unpack(archive_path, extract_to):
    shutil.unpack_archive(archive_path, extract_to)


def process_iffolder(path, root_path):
    is_empty = not any(path.iterdir())
    if not path.stem in filetypes():
        if is_empty:
            path.rmdir()
        else:
            parse_main(path, root_path)


def process_iffile(path, root_path):
    filetype = classify(path)
    if filetype == "archives":
        print("found filetype", filetype, path)
        unpack_target = root_path / "archives" / path.stem
        unpack(path, unpack_target)
    else:
        move(path, root_path, filetype)


def move(path, root_path, filetype):
    if filetype:  # handler for known types
        destination_folder = Path(root_path / filetype)
        destination_folder.mkdir(parents=True, exist_ok=True)
        new_path = root_path / f"{filetype}\{path.name}"
        counter = 1
        try:
            path.resolve().rename(new_path)
        except FileExistsError:
            while new_path.exists():
                char = counter * "_"
                new_path = root_path / f"{filetype}\{path.stem}{char}{path.suffix}"
                counter += 1
            path.resolve().rename(new_path)
        except:
            print(f"file move failed : {path.name}")
    else:  # unknown files will not be moved
        # print(f"Error, not moving {path}")
        pass


def parse_main(path, root_path):
    """Parsing folder index recursively and making major decisions
    path -- str name of folder
    """
    # print(f"path is {path}")
    try:
        for file_path in path.iterdir():
            filename_normalized = rename_files(file_path)
            if filename_normalized.is_dir():
                multithread(process_iffolder, (filename_normalized, root_path))
            else:  # from here all file operations
                multithread(process_iffile, (filename_normalized, root_path))
    except FileNotFoundError:
        print("Folder not found")


def multithread(func, args: tuple):
    th = Thread(target=func, args=args)
    th.start()


def main_prog():
    for p in sys.argv[1:]:
        path = Path(p)
        parse_main(path, path)
        print(f"Unknown extensions are:", " ".join(unknown_extensions))


# main loop
if __name__ == "__main__":
    unknown_extensions = []
    main_prog()
