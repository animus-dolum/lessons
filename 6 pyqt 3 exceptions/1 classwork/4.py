def check(s):
    b = [
        "qwe",
        "wer",
        "ert",
        "rty",
        "tyu",
        "yui",
        "uio",
        "iop",
        "asd",
        "sdf",
        "dfg",
        "fgh",
        "ghj",
        "hjk",
        "jkl",
        "zxc",
        "xcv",
        "cvb",
        "vbn",
        "bnm",
        "йцу",
        "цук",
        "уке",
        "кен",
        "енг",
        "нгш",
        "гшщ",
        "шщз",
        "щзх",
        "зхъ",
        "фыв",
        "ыва",
        "вап",
        "апр",
        "про",
        "рол",
        "олд",
        "лдж",
        "джэ",
        "ячс",
        "чсм",
        "сми",
        "мит",
        "ить",
        "тьб",
        "ьбю",
        "жэё",
    ]
    if (
        len(s) > 8
        and s.lower != s
        and s.upper() != s
        and "1" in [str(int(x.isdigit())) for x in s]
        and "1"
        not in "".join(
            list(
                map(
                    lambda x: "".join(x).replace("0", ""),
                    [
                        [
                            str(int(s[i:i + 3].lower() in b[j]))
                            for i in range(len(s) - 2)
                        ]
                        for j in range(len(b))
                    ],
                )
            )
        )
    ):
        return "ok"
    else:
        return "error"


p = input()
print(check(p))
