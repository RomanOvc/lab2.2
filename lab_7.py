from textwrap import wrap

slovar = {'000': '011', '001': '101', '010': '000', '011': '111',
          '100': '010', '101': '110', '110': '001', '111': '100'}

def in_2(stroka):
    xx1 = bin(int(stroka, 16))
    xx2 = xx1[2:]
    return xx2


def sdig_right(word, on):
    kek = in_2(word)
    listik = []
    for listok in kek:
        listik.append(listok)
    ii = 0
    while ii < on - 1 and on != 8:
        listik.insert(0, listik[7])
        listik.pop(8)
        ii += 1
    trolo = ""
    for listok1 in listik:
        trolo += listok1
    return trolo

def sdig_right2(word, on):
    kek = in_2(word)
    listik = []
    for listok in kek:
        listik.append(listok)
    ii = 0
    while ii < on - 1 and on != 8:
        listik.insert(0, listik[6])
        listik.pop(7)
        ii += 1
    trolo = ""
    for listok1 in listik:
        trolo += listok1
    return trolo


if __name__ == "__main__":
    print("Задание 1")
    print("Сложение по модулю 2")
    x_1 = int("10101100", 2)
    x_2 = int("11001010", 2)
    x_3 = x_1 ^ x_2
    print(bin(x_3)[2:])

    x_1_1 = int("15", 10)
    x_1_2 = int("10", 10)
    x_1_3 = x_1_1 + x_1_2
    print(x_1_3)

    x_1_1_1 = int("1B5", 16)
    x_1_1_2 = int("37", 16)
    x_1_1_3 = x_1_1_1 + x_1_1_2
    print(hex(x_1_1_3)[2:])

    print("Задание 2")
    print("Сложение по модулю 2^8")
    x2_1_1 = int("10101100", 2)
    x2_1_2 = int("11001010", 2)
    x2_1_3 = x2_1_1 + x2_1_2
    print(bin(x2_1_3)[2:])

    x2_2_1 = int("155", 10)
    x2_2_2 = int("100", 10)
    x2_2_3 = x2_2_1 + x2_2_2
    print(x2_2_3)

    x2_3_1 = int("0B5", 16)
    x2_3_2 = int("37", 16)
    x2_3_3 = x2_3_1 + x2_3_2
    print(hex(x2_3_3)[2:])

    print("Задание 3")
    a = "10101100"
    b = []
    сiuyt = ""
    for aa in a:
        b.append(aa)
    i = 0
    while i < 5:
        b.append(a[i])
        i += 1
        b.pop(0)
    for bbb in b:
        сiuyt += bbb
    print(сiuyt)

    xw2 = "9E"
    print(sdig_right(xw2, 5))
    xw3 = "55"
    print(sdig_right2(xw3,2))


    print("Задание 5")
    xxw1 = "101011001100"
    kek = wrap(xxw1,3)
    new_str = ""
    for ke in kek:
        for key,val in dict.items(slovar):
            if ke == key:
                new_str += val
    print(new_str)


