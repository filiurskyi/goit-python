CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
cyr = list(CYRILLIC_SYMBOLS)

for cy, tr in zip(cyr, TRANSLATION):
    TRANS[ord(cy)] = tr
    TRANS[ord(cy.upper())] = tr.upper()


def translate(name):
    '''Takes string, checks if cyrillic, and then translliterates it

    name -- str
    '''
    return name.translate(TRANS)


def normalize(name):
    '''input is WindowPath obj
    assume that extension is str after last "."
    '''
    # extract file extension as ext and file name es fname
    fname = list(name.stem)
    ext = name.suffix

    # iterate through every char in file name and replace unknown chars with "_"
    for char in fname:
        if not char.isalpha():
            fname[fname.index(char)] = "_"
    normalized_name = translate("".join(fname)) + ext
    return normalized_name
