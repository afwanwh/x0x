char_map = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25,
}

char_map_inv = {y: x for x, y in char_map.iteritems()}


def encrypt_shift(key, text):
    text.lower()
    chiptxt = ''
    for _chr in text:
        calc = (char_map[_chr] + int(key)) % 26
        chiptxt += char_map_inv[calc]
    return chiptxt


def decrypt_shift(key, text):
    text.lower()
    pltxt = ''
    for _chr in text:
        calc = (char_map[_chr] - int(key)) % 26
        pltxt += char_map_inv[calc]
    return pltxt