import random


def easy_pass(n_pass):
    str = ""
    n = 0
    while n < n_pass:
        list1 = []
        s1 = random.randint(97, 122)
        s2 = random.randint(65, 90)
        s3 = random.randint(33, 39)
        s4 = random.randint(48, 57)
        list1.append(chr(s1))
        list1.append(chr(s2))
        list1.append(chr(s3))
        list1.append(chr(s4))
        str += random.choice(list1)
        n += 1
    return str


def bust(str1):
    list_33_39 = []
    list_48_57 = []
    list_65_90 = []
    list_97_122 = []
    check = 0
    for st in str1:
        if ord(st) >= 33 and ord(st) <= 39:
            list_33_39.append(st)
        elif ord(st) >= 48 and ord(st) <= 57:
            list_48_57.append(st)
        elif ord(st) >= 65 and ord(st) <= 90:
            list_65_90.append(st)
        elif ord(st) >= 97 and ord(st) <= 122:
            list_97_122.append(st)
    if len(list_33_39) >= 1:
        check += 7
    if len(list_48_57) >= 1:
        check += 10
    if len(list_65_90) >= 1:
        check += 26
    if len(list_97_122) >= 1:
        check += 26
    return check


def down_border():
    return 100 * 10 * 10000000


def power_pass(check2, n_pass1):
    return check2 ** n_pass1


if __name__ == "__main__":
    print("Вариант 12")
    num_pass = random.randint(0, 10)
    lol = int(num_pass)
    kek = easy_pass(lol)
    pepe = bust(kek)
    sk = down_border()
    sp = power_pass(pepe, num_pass)
    print("Сгенерированный пароль: ", kek)
    print("Нижняя граница числа всевозможных паролей: ", sk)
    print("Сила словаря для пароля: ", sp)
    if sk <= sp:
        print("Пароль устойчив. Количество символов в пароле ", num_pass)
    else:
        print("Пароль не устойчив. Количество символов в пароле ", num_pass)

