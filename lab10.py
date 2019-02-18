import random


def open_key(a, X, p):
    return (a ** X) % p


if __name__ == "__main__":
    print("Задание 1")
    p = 47
    q = 23
    a = 37
    X = 8
    # y
    open_key1 = open_key(a, X, p)
    print("Открытый ключ", open_key1)

    print("Задание 2")
    podpis = []
    p2 = 47
    q2 = 23
    a2 = 7
    X2 = 8
    k2 = 7
    h2 = 10
    open_key2 = open_key(a2, X2, p2)
    r = ((a2 ** k2) % p2) % q2
    podpis.append(r)
    s = (k2 * h2 + X2 * r) % q2
    podpis.append(s)
    print("Открытый ключ = ", open_key2)
    print("Подпись сообщения состоит из пары чисел =", podpis)

    print("Задание 3")
    P3 = 17
    A3 = 3
    X3 = 11
    key = open_key(A3, X3, P3)
    print("Открытый ключ =", key)

    print("Задание 4")
    digital = []
    P4 = 17
    A4 = 3
    X4 = 3
    k4 = 7
    m4 = 11
    key4 = open_key(A4, X4, P4)
    a = (A4 ** k4) % P4
    b = m4 * ((key4 ** k4) % P4)
    digital.append(a)
    digital.append(b)
    print("Открытый ключ =", key4)
    print("Подпись сообщения состоит из пары чисел =", digital)
