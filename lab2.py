users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']
files = ['объект1', 'объект2', 'объект3', 'объект4']
roots = ['read', 'write', 'grant', 'super']

files_preview = {files[0]: [{users[0]: [(roots[0], roots[0])]}, {users[1]: [(roots[0])]}, {users[2]: [(roots[2])]},
                            {users[3]: [(roots[3])]},
                            {users[4]: [{roots[1]}]}, {users[5]: [{roots[1]}]}],
                 files[1]: [{users[0]: [(roots[0], roots[0])]}, {users[1]: [(roots[0])]}, {users[2]: [(roots[2])]},
                            {users[3]: [(roots[3])]},
                            {users[4]: [{roots[1]}]}, {users[5]: [{roots[1]}]}],
                 files[2]: [{users[0]: [(roots[0], roots[0])]}, {users[1]: [(roots[0])]}, {users[2]: [(roots[2])]},
                            {users[3]: [(roots[3])]},
                            {users[4]: [{roots[1]}]}, {users[5]: [{roots[1]}]}],
                 files[3]: [{users[0]: [(roots[0], roots[0])]}, {users[1]: [(roots[0])]}, {users[2]: [(roots[2])]},
                            {users[3]: [(roots[3])]},
                            {users[4]: [{roots[1]}]}, {users[5]: [{roots[1]}]}],
                 }
print(files_preview)


def str_p(s1, s2):
    return s1 + "," + s2


while True:
    a = input("введите пользователя:")
    if a != 'quit':
        for user in users:
            if a == user:
                print("Идентификация прошла успешно")
                print("Ваши права:")

                for key, val in dict.items(files_preview):
                    for x in val:
                        for key1, val1 in dict.items(x):
                            if a == key1:
                                print(key, ":", val1)
                                break

        while True:
            b = input("Жду указаний:")
            if b == 'read' or b == 'write' or b == 'super' or b == 'grant':
                c = input("Над каким объектом производится операция:")
                if c in dict.keys(files_preview):

                    for keyys1, valls1 in dict.items(files_preview):
                        for y in valls1:
                            if c == keyys1:
                                for keyys2, valls2 in dict.items(y):
                                    if a == keyys2:
                                        if b == valls2:
                                            if valls2 == 'read' or valls2 == 'write':
                                                print("операция прошла")
                                            elif valls2 == 'grant' or valls2 == 'super':
                                                d = input("")


                                        else:
                                            print("операция не прошла")

                                    break


                else:
                    print("n")
            elif b == 'quit':
                break
    else:
        break

