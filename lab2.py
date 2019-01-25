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
    return s1 + "," + s2


# aa = input("введите строку: ")
# bb = aa.split(", ")
# print(bb)
#
# for b in bb:
#     if b in roots:
#         print(b)
#     else:
#         print("n")


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
                                                cc = bb.split(", ")
                                                for keyys1, valls1 in dict.items(files_preview):
                                                    if c == keyys1:
                                                        for y in valls1:
                                                            for usors, rootos in dict.items(y):
                                                                if aa == usors:
                                                                    print(usors)
                                                                    if bb in roots:
                                                                        if bb == 'grant' or bb == 'read' or\
                                                                                bb == 'write':
                                                                            rootos.clear()
                                                                            rootos.append(bb)
                                                                            print("права переданы")
                                                                            print(rootos)
                                                                        else:
                                                                            print("недостаточно прав")
                                                                    else:
                                                                        print("такие права невозможно передать")

                                            elif rootos1 == 'super':
                                                aa = input("какому пользователю назначить права над текущим объектом? ")
                                                bb = input("какие права? ")
                                                cc = bb.split(", ")
                                                for keyys1, valls1 in dict.items(files_preview):
                                                    if c == keyys1:
                                                        for y in valls1:
                                                            for usors, rootos in dict.items(y):
                                                                if aa == usors:
                                                                    print(usors)
                                                                    if bb in roots:
                                                                        if bb != 'super':
                                                                            rootos.clear()
                                                                            rootos.append(bb)
                                                                            print("права переданы")
                                                                            print(rootos)
                                                                        else:
                                                                            print("таких прав нет")
                                                                    else:
                                                                        print("такие права невозможно передать")


                                        else:
                                            print("этот пользователь в данном ")
                                            break

                    # else:
                    #     print("у этого пользователя нет таких прав над текущим объектом. Повторите попытку")
                    #     break

        elif b == 'quit':
            break
    break
            #          else:
            #             print("n")
            #             # for keyys1, valls1 in dict.items(files_preview):
            #             #     print(keyys1)
            #             #     for y in valls1:
            #             #         if c == keyys1:
            #             #             for keyys2, valls2 in dict.items(y):
            #             #                 if a == keyys2:
            #             #                     if b == valls2:
            #             #                         if valls2 == 'read' or valls2 == 'write':
            #             #                             print("операция прошла")
            #             #                         elif valls2 == 'grant' or valls2 == 'super':
            #             #                             d = input("")
            #
            #                             #
            #                             #     else:
            #                             #         print("операция не прошла")
            #                             #
            #                             # break
            #
            #
            #
            #     elif b == 'quit':
            #         break

