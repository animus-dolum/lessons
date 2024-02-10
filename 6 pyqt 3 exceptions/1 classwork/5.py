class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_password(password):
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
    if len(password) < 9:
        raise LengthError
    elif password.lower() == password or password.upper() == password:
        raise LetterError
    elif "1" not in [str(int(x.isdigit())) for x in password]:
        raise DigitError
    elif "1" in "".join(
        list(
            map(
                lambda x: "".join(x).replace("0", ""),
                [
                    [
                        str(int(password[i:i + 3].lower() in b[j]))
                        for i in range(len(password) - 2)
                    ]
                    for j in range(len(b))
                ],
            )
        )
    ):
        raise SequenceError
    else:
        return "ok"