from functools import reduce

users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']
files = ['объект1', 'объект2', 'объект3', 'объект4']
roots = ['read', 'write', 'grant', 'super']

files_preview = {
    files[0]: [
        {users[0]: [roots[2]]},
        {users[1]: [roots[3]]},
        {users[2]: [roots[0], roots[1]]},
        {users[3]: [roots[0], roots[1]]},
        {users[4]: [roots[0], roots[1]]},
        {users[5]: [roots[0], roots[1]]}
    ],
    files[1]: [{users[0]: [roots[2], roots[1]]},
               {users[1]: [roots[3], roots[1]]},
               {users[2]: [roots[0], roots[1]]},
               {users[3]: [roots[0], roots[1]]},
               {users[4]: [roots[0], roots[1]]},
               {users[5]: [roots[0], roots[1]]}],
    files[2]: [{users[0]: [roots[0], roots[1]]},
               {users[1]: [roots[0], roots[1]]},
               {users[2]: [roots[0], roots[1]]},
               {users[3]: [roots[0], roots[1]]},
               {users[4]: [roots[0], roots[1]]},
               {users[5]: [roots[0], roots[1]]}],
    files[3]: [{users[0]: [roots[0], roots[1]]},
               {users[1]: [roots[0], roots[1]]},
               {users[2]: [roots[0], roots[1]]},
               {users[3]: [roots[0], roots[1]]},
               {users[4]: [roots[0], roots[1]]},
               {users[5]: [roots[0], roots[1]]}]
}
print(files_preview)


def str_p(s1, s2):
    return s1 + ", " + s2


while True:
    a = input("введите пользователя:")
    if a != 'quit':
        for user in users:
            if a == user:
                print("Идентификация прошла успешно")
                print("Ваши права:")
                for key, val in dict.items(files_preview):
                    for ax in val:
                        for keys, vals in dict.items(ax):
                            if a == keys:
                                print(key)
                                for vals1 in vals:
                                    print(vals1)
    elif a == 'quit':
        break
    while True:
        b = input("Жду указаний:")
        if b == 'read' or b == 'write' or b == 'super' or b == 'grant':
            c = input("Над каким объектом производится операция:")
            if c in dict.keys(files_preview):
                for keyys1, valls1 in dict.items(files_preview):
                    if c == keyys1:
                        print(keyys1)
                        for y in valls1:
                            for usors, rootos in dict.items(y):
                                if a == usors:
                                    print(usors)
                                    for rootos1 in rootos:
                                        if b == rootos1:
                                            if rootos1 == 'read' or rootos1 == 'write':
                                                print("действие выполнено")
                                            elif rootos1 == 'grant':
                                                aa = input("какому пользователю передать права текущего объекта? ")
                                                bb = input("какие права?")
                                                cc = bb.split(",")
                                                for keyys1, valls1 in dict.items(files_preview):
                                                    if c == keyys1:
                                                        for y in valls1:
                                                            for usors, rootos in dict.items(y):
                                                                if aa == usors and 'super' not in rootos:
                                                                    if 'super' in cc:
                                                                        print("недостаточно прав")
                                                                        break
                                                                    if all((lambda r: r in roots)(r) for r in cc):
                                                                        rootos.clear()
                                                                        rootos.extend(cc)
                                                                        print("права добавлены")
                                                                    else:
                                                                        print("таких прав нет")
                                            elif rootos1 == 'super':
                                                aa = input("какому пользователю назначить права над текущим объектом? ")
                                                bb = input("какие права? ")
                                                cc = bb.split(", ")
                                                for keyys1, valls1 in dict.items(files_preview):
                                                    if c == keyys1:
                                                        for y in valls1:
                                                            for usors, rootos in dict.items(y):
                                                                if aa == usors:
                                                                    if all((lambda r: r in roots)(r) for r in cc):
                                                                        rootos.clear()
                                                                        rootos.extend(cc)
                                                                        print("права добавлены")
                                                                    else:
                                                                        print("таких прав нет")
                                        else:
                                            print("этот пользователь в данном объекте не имеет таких прав ")
                                            break
        elif b == 'quit':
            break



