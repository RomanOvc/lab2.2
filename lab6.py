slovar1 = {'А': {'В': '^'}, 'Б': {'И': '@'}, 'В': {'О': ')'}, 'Г': {'А': '+'}, 'Д': {'Щ': '<'}, 'Е': {'П': '>'},
           'Ж': {'К': 'Ɐ'}, 'З': {'Б': '♦'}, 'И': {'Ъ': '*'}, 'К': {' ': '♥'}, 'Л': {'Р': '♠'}, 'М': {'Т': '№'},
           'Н': {'Ц': '#'}, 'О': {'.': '-'}, 'П': {'Ж': '='}, 'Р': {'Г': '('}, 'С': {'Л': '?'}, 'Т': {'Х': '%'},
           'У': {'С': '⊗'}, 'Ф': {'Ь': '!'}, 'Х': {'Ч': '&'}, 'Ц': {'З': '®'}, 'Ч': {'М': 'Σ'}, 'Ш': {'У': '▽'},
           'Щ': {'Д': 'Ⲩ'}, 'Ъ': {'Э': 'κ'}, 'Ы': {'Н': '⊕'}, 'Ь': {'Ю': '×'}, 'Э': {'Ы': 'ω'}, 'Ю': {'Ш': '$'},
           'Я': {'Е': '⧍'}, ' ': {'Ф': '∞'}, '.': {'Я': '♣'}, }



def sh_1_sh_2_zamena(slovo,slovar):
    str1 = ""
    for st in slovo:
        for key, val in dict.items(slovar):
            for key1, val1 in dict.items(val):
                if ord(key1) == ord(st):
                    str1 += key
                elif ord(val1) == ord(st):
                    str1 += key
    return str1

def generate_key(word, key):
    gen_key = ""
    while len(word) > len(gen_key):
        for st in key:
            if len(word) > len(gen_key):
                gen_key += st
    return gen_key


def hash_vijner(word, key, slovar):
    gen_key = generate_key(word, key)
    str1 = []
    for kk in gen_key:
            str1.append(slovar.index(kk))
    str2 = []
    for lo in word:
            str2.append(slovar.index(lo))
    x = ''
    for i in range(0, len(str2)):
        y = (str1[i] + str2[i]) % len(slovar)
        x += (slovar[y])
    return x


def de_hash_vijner(word, key, slovar):
    gen_key = generate_key(word, key)
    str1 = []
    for kk in gen_key:
        if kk in slovar:
            str1.append(slovar.index(kk))
    str2 = []
    for lo in word:
        if lo in slovar:
            str2.append(slovar.index(lo))
    x = ''
    for i in range(0, len(str2)):
        y = (str2[i] - str1[i] + len(slovar)) % len(slovar)
        x += (slovar[y])
    return x





if __name__ == "__main__":
    print("ЗАдание 1")
    str12 = "И.РЮУ.ЪФОБГНО"
    str123 = "▽*!(∞♦^№>#⊕"
    print(sh_1_sh_2_zamena(str12, slovar1))
    print(sh_1_sh_2_zamena(str123,slovar1))
    print()
    print()
    print("Шифр Вижнера.Зашифровал")
    slovar1 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    slovar1_1 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"
    print("Расшифровать слова с помощью ключа ОРЕХ")
    key1 = "ОРЕХ"
    word = "ШВМБУЖНЯ"

    cryped = hash_vijner(word, key1, slovar1)

    print(cryped)

    decrypted = de_hash_vijner(word, key1, slovar1_1)

    print(decrypted)

