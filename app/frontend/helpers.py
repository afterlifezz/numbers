WORDS = [
    [
        ['', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć'],
        ['dziesięć', 'jedenaście', 'dwanaście', 'trzynaście', 'czternaście', 'piętnaście', 'szesnaście', 'siedemnaście',
         'osiemnaście', 'dziewiętnaście'],
        ['', 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt', 'siedemdziesiąt',
         'osiemdziesiąt', 'dziewięćdziesiąt'],
        ['sto', 'dwieście', 'trzysta', 'czterysta', 'pięćset', 'sześćset', 'siedemset', 'osiemset', 'dziewięćset'],
    ],
    ['tysiąc', 'tysiące', 'tysięcy'],
    ['milion', 'miliony', 'milionów'],
    ['miliard', 'miliardy', 'miliardów'],
    ['bilion', 'biliony', 'bilionów'],
    ['biliard', 'biliardy', 'biliardów'],
    ['trylion', 'tryliony', 'trylionów'],
    ['tryliard', 'tryliardy', 'tryliardów']
]


def split_by_three(str):
    array = []
    count = 0
    while str:
        array.append([int(str[-3:]), count])
        str = str[:-3]
        count = count + 1
    return list(reversed(array))


def under10(num, level, text):
    if num > 0:
        text.append(WORDS[0][0][num])
        if level > 0:
            if num in [2, 3, 4]:
                text.append(WORDS[level][1])
            else:
                text.append(WORDS[level][2])


def under20(num, level, text):
    text.append(WORDS[0][1][num - 10])
    if level > 0:
        text.append(WORDS[level][2])


def under100(num, level, text):
    if num < 10:
        under10(num, level, text)
    elif num < 20:
        under20(num, level, text)
    else:
        text.append(WORDS[0][2][num // 10 - 1])
        rest = num % 10
        if rest:
            under10(rest, level, text)


def under1000(num, level, text):
    text.append(WORDS[0][3][num // 100 - 1])
    rest = num % 100
    if rest > 0:
        under100(rest, level, text)
    elif level > 0:
        text.append(WORDS[level][2])


def to_words(number):
    number_str = str(number)
    text = []

    if len(number) > 24:
        return 'Integer is to large! Max 24 digits!'

    if int(number) == 0:
        return 'zero'

    for num, level in split_by_three(number_str):
        num_str = str(num)
        if num < 10:
            under10(num, level, text)
        elif num < 20:
            under20(num, level, text)
        elif num < 100:
            under100(num, level, text)
        else:
            under1000(num, level, text)

    return f"{' '.join(text)}"
