def PSCH(a, b, c):
    i = 0
    k = 0
    listok = []
    while i < c:
        k = (a * k + b) % c
        i += 1
        listok.append(k)
    return listok


def lag_Fibonacci(a, b, listok):
    aa = a - 1
    bb = b - 1
    while aa < 10:
        k = listok[bb] - listok[aa]
        if k < 0:
            o = k + 1
            listok.append(o)
        else:
            listok.append(k)
        aa += 1
        bb += 1
    return listok

def Factor(n):
   Ans = []
   d = 2
   while d * d <= n:
       if n % d == 0:
           Ans.append(d)
           n //= d
       else:
           d += 1
   if n > 1:
       Ans.append(n)
   return Ans


if __name__ == "__main__":
    print("Задание 1.1")
    print(sorted(set(PSCH(5, 7, 17)[:10])))
    a = set(PSCH(5, 7, 17))
    print("период линейного конгруэнтного генератора ПСЧ = ", len(a))
    print(sorted(set(PSCH(6, 3, 23)[:10])))
    b = set(PSCH(6, 3, 23))
    print("период линейного конгруэнтного генератора ПСЧ  = ", len(b))

    print("Задание 1.2")
    listik1 = [0.6, 0.3, 0.5]
    print(lag_Fibonacci(3, 1, listik1))
    listik2 = [0.9, 0.3, 0.5, 0.9]
    print(lag_Fibonacci(4, 2, listik2))

    print("Задание 1.3")
    listok123 = [3, 8, 55, 14, 12, 50, 38, 53, 52]
    listok231 = []
    i = 1
    k1 = 0
    k2 = 1
    while i < len(listok123):
         lo = int(listok123[k2]) - int(listok123[k1])
         listok231.append(lo)
         i += 1
         k1 += 1
         k2 += 1
    print(len(listok231))

    ii = 1
    kk1 = 0
    kk3 = 2
    kk2 = 1
    listok333 = []
    while ii < len(listok231):
        lp = abs(int(listok231[kk3])* int(listok231[kk1]) - (int(listok231[kk2]) ** 2))
        listok333.append(lp)
        ii += 1
        kk1 += 1
        kk2 += 1
    print(listok333)

    print("Задание 1.3")
    listok123 = [3, 8, 55, 14, 12, 50, 38, 53, 52]
    listok231 = []
    i = 1
    k1 = 0
    k2 = 1
    while i < len(listok123):
        lo = int(listok123[k2]) - int(listok123[k1])
        listok231.append(lo)
        i += 1
        k1 += 1
        k2 += 1

    ii = 1
    kk1 = 0
    kk3 = 2
    kk2 = 1
    listok333 = []
    while ii < len(listok231) and kk3 < len(listok231):
        lp = abs(int(listok231[kk3]) * int(listok231[kk1]) - (int(listok231[kk2]) ** 2))
        listok333.append(lp)
        ii += 1
        kk1 += 1
        kk2 += 1
        kk3 += 1

    listU = []
    listUK = []
    for lis in listok333:
        listU.append(Factor(lis))
    for lk in listU:
        for l in lk:
            listUK.append(l)
    new_list = sorted(set(listUK))

    jo = 0
    for k in new_list:
        for lis1 in listU:
            for li in lis1:
                if li % k == 0:
                    jo = k
    print("c = ", jo)



    print("ЗАдание 4")
    p = 11
    q = 19
    x = 3
    i = 0
    while i<11:
         x0 = (x ** 2) % (p*q)
         x = x0
         i += 1
    print(x0)






