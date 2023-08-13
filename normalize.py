CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
cyr = [x for x in CYRILLIC_SYMBOLS]

for cy, tr in zip(cyr, TRANSLATION):
    TRANS[ord(cy)] = tr
    TRANS[ord(cy.upper())] = tr.upper()


def translate(name):
    return name.translate(TRANS)
