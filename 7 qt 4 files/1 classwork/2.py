d = {
    "й": "j",
    "ц": "c",
    "у": "u",
    "к": "k",
    "е": "e",
    "н": "n",
    "г": "g",
    "ш": "sh",
    "щ": "shh",
    "з": "z",
    "х": "h",
    "ъ": "#",
    "ф": "f",
    "ы": "y",
    "в": "v",
    "а": "a",
    "п": "p",
    "р": "r",
    "о": "o",
    "л": "l",
    "д": "d",
    "ж": "zh",
    "э": "je",
    "я": "ya",
    "ч": "ch",
    "с": "s",
    "м": "m",
    "и": "i",
    "т": "t",
    "ь": "'",
    "б": "b",
    "ю": "ju",
    "ё": "jo"
}


with open('cyrillic.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    lst = []
    for x in s:
        print(x)
        if x.lower() in d.keys():
            if x == x.upper():
                lst.append(d[x.lower()].capitalize())
            else:
                lst.append(d[x])
        else:
            lst.append(x)


with open('transliteration.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(lst))
