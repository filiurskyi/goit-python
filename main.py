import sys
from pathlib import Path
import normalize
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
            if str(file_name).endswith(extension):
                return type
    return None


def parse_folder(path):
    '''Parsing folder index recursively

    path -- str name of folder
    '''
    for item in path.iterdir():
        if item.is_dir():
            print("Folder found:".ljust(15), item)
            parse_folder(item)
        else:
            print("File found:".ljust(15),  item)
            print("Classified as:".ljust(15), classify(item))


if __name__ == '__main__':
    for p in sys.argv[1:]:
        path = Path(p)
        print("Starting to sort folder:", path)
        parse_folder(path)
