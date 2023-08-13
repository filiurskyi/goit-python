import sys
from pathlib import Path
from normalize import normalize
import json
import shutil


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


def parse_folder(path):
    '''Parsing folder index recursively and making major decisions

    path -- str name of folder
    '''

    ljust = 15
    infotext = ">>> Starting to sort folder:"
    print(infotext, path)
    for file_path in path.iterdir():
        if file_path.is_dir():
            print("> Found folder:".ljust(ljust), file_path)
            if file_path in ["archives", "video", "audio", "documents", "images"]:
                continue
            else:
                print(infotext, path)
                parse_folder(file_path)
        else:  # from here all file operations
            print("File found:".ljust(ljust),  file_path)
            print("Classified as:".ljust(ljust), classify(file_path))

            file_type = classify(file_path)
            normalized_name = normalize(file_path)

            print(f"Classified as: ".ljust(ljust), file_type)
            print(f"Normalized name is".ljust(ljust), normalized_name)

            if file_type:  # handler for known types
                shutil.move(file_path, f"{file_type}/{normalized_name}")
                pass
            else:
                pass


# main loop
if __name__ == '__main__':
    for p in sys.argv[1:]:
        path = Path(p)
        parse_folder(path)
        print(p)
