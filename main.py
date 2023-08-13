import sys
from pathlib import Path
import normalize
import json


def classify(file_name):
    '''Return file classification

    extension -- str input filename
    type -- str output classification of file

    returns None if extension is unknown
    '''
    file = 'extensions.json'
    with open(file, "r") as f:
        types = json.loads(f.read())
    for type, extensions in types.items():
        for extension in extensions:
            if str(file_name).endswith(extension):
                return type
    return None


def parse_folder(path):
    '''Parsing folder index recursively

    path -- str name of folder
    '''
    for item in path.iterdir():
        if item.is_dir():
            print("Folder found:".ljust(25), item)
            parse_folder(item)
        else:
            print("File found:".ljust(25),  item)
            print("Classified as".ljust(25), classify(item))


if __name__ == '__main__':
    for p in sys.argv[1:]:
        path = Path(p)
        print("Starting to sort folder:".ljust(25), path)
        parse_folder(path)
