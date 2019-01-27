import random

import time

print("Вариант 12")


# def gen_code():
#     abc = "qwertyuiop[]as34567890dfghjklzxcvbnm,./1234567890-=QWERTYUIOP{}ASDFG34567890HJKL:ZXCVBNM"
#     password = ""
#     for i in range(10):
#         password += abc[random.randint(0, len(abc))]
#     print(password)
#
# gen_code()
# print("////////////////////////////////////////////")


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


while True:
    num_pass = input("введите количество символов")
    lol = int(num_pass)
    kek = easy_pass(lol)
    print(kek)
