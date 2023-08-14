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
    if not path in filetypes():
        if is_empty:
            path.rmdir()
        else:
            parse_main(path, root_path)


def process_iffile(path, root_path):
    filetype = classify(path)

    # MOVE
    # try:
    #     path.resolve().rename(f"{root_path}\{filetype}\{normalized_name}")
    #     print(f"file move ok : ".ljust(ljust), f"{root_path}\{filetype}\{normalized_name}")


def parse_main(path, root_path, verbose=0):
    '''Parsing folder index recursively and making major decisions

    path -- str name of folder
    '''
    for file_path in path.iterdir():
        rename_files(file_path, root_path)
        if file_path.is_dir():
            process_iffolder(file_path, root_path)
        else:  # from here all file operations
            process_iffile(file_path, root_path)

        #     file_type = classify(file_path)
        #     normalized_name = normalize(filename_to_str(file_path))

        #     if file_type:  # handler for known types
        #         destination_folder = Path(root_path / file_type)
        #         destination_folder.mkdir(parents=True, exist_ok=True)

            # try:
            #     file_path.resolve().rename(
            #         f"{root_path}\{file_type}\{normalized_name}")
            #     print(f"file move ok : ".ljust(ljust),
            #           f"{root_path}\{file_type}\{normalized_name}")

        #         except OSError:
        #             file_path.resolve().rename(
        #                 f"{root_path}\{file_type}\{counter}_{normalized_name}")
        #             if verbose:
        #                 print(f"file move ok (d) : ".ljust(ljust),
        #                       f"{root_path}\{file_type}\{counter}_{normalized_name}")

        #         except:
        #             if verbose:
        #                 print(f"file move failed : ".ljust(ljust),
        #                       f"{file_type}\{normalized_name}")
        #     else:
        #         print(f"not moving anything".rjust(ljust))


# main loop
if __name__ == '__main__':
    for p in sys.argv[1:]:
        unknown_extensions = []
        path = Path(p)
        parse_main(path, path, verbose=0)
        print(f"Unknown extensions are:", " ".join(unknown_extensions))
