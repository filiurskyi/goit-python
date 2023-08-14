import sys
from pathlib import Path
from normalize import normalize
import json


def classify(file_name, file='extensions.json'):
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
            if file_name.suffix in extensions:
                return type
    return None


def log_unknown_ext():
    '''log unknown extensions'''
    pass


def filename_to_str(filename):
    '''convert and split path obj to string tuple'''
    return (str(filename.stem), str(filename.suffix))


def rename_files():
    '''rename files and folders'''

    pass


def parse_folder(path, root_path, verbose=0):
    '''Parsing folder index recursively and making major decisions

    path -- str name of folder
    '''

    ljust = 15
    infotext = ">>> Starting to sort folder:"
    if verbose:
        print(infotext, path)
    counter = 0
    for file_path in path.iterdir():
        counter += 1
        if file_path.is_dir():
            if verbose:
                print("> Found folder:".ljust(ljust), file_path)
            if file_path in ["archives", "video", "audio", "documents", "images"]:
                continue
            else:
                if verbose:
                    print(infotext, path)
                parse_folder(file_path, root_path, verbose)
        else:  # from here all file operations
            file_type = classify(file_path)
            normalized_name = normalize(filename_to_str(file_path))

            if verbose:
                print("File found:".ljust(ljust),  file_path)
                print("Classified as:".ljust(ljust), classify(file_path))
                print("Classified as: ".ljust(ljust), file_type)
                print("Normalized name is".ljust(ljust), normalized_name)

            if file_type:  # handler for known types
                destination_folder = Path(root_path / file_type)
                destination_folder.mkdir(parents=True, exist_ok=True)

                try:
                    file_path.resolve().rename(
                        f"{root_path}\{file_type}\{normalized_name}")
                    print(f"file move ok : ".ljust(ljust),
                          f"{root_path}\{file_type}\{normalized_name}")

                except OSError:
                    file_path.resolve().rename(
                        f"{root_path}\{file_type}\{counter}_{normalized_name}")
                    if verbose:
                        print(f"file move ok (d) : ".ljust(ljust),
                              f"{root_path}\{file_type}\{counter}_{normalized_name}")

                except:
                    if verbose:
                        print(f"file move failed : ".ljust(ljust),
                              f"{file_type}\{normalized_name}")
            else:
                print(f"not moving anything".rjust(ljust))


# main loop
if __name__ == '__main__':
    for p in sys.argv[1:]:
        path = Path(p)
        parse_folder(path, path, verbose=0)
