from textwrap import wrap
# slovar1 = {'А': {'В': '^'}, 'Б': {'И': '@'}, 'В': {'О': ')'}, 'Г': {'А': '+'}, 'Д': {'Щ': '<'}, 'Е': {'П': '>'},
#            'Ж': {'К': 'Ɐ'}, 'З': {'Б': '♦'}, 'И': {'Ъ': '*'}, 'К': {' ': '♥'}, 'Л': {'Р': '♠'}, 'М': {'Т': '№'},
#            'Н': {'Ц': '#'}, 'О': {'.': '-'}, 'П': {'Ж': '='}, 'Р': {'Г': '('}, 'С': {'Л': '?'}, 'Т': {'Х': '%'},
#            'У': {'С': '⊗'}, 'Ф': {'Ь': '!'}, 'Х': {'Ч': '&'}, 'Ц': {'З': '®'}, 'Ч': {'М': 'Σ'}, 'Ш': {'У': '▽'},
#            'Щ': {'Д': 'Ⲩ'}, 'Ъ': {'Э': 'κ'}, 'Ы': {'Н': '⊕'}, 'Ь': {'Ю': '×'}, 'Э': {'Ы': 'ω'}, 'Ю': {'Ш': '$'},
#            'Я': {'Е': '⧍'}, ' ': {'Ф': '∞'}, '.': {'Я': '♣'}, }
#
#
# ////////////////////////////////////////////
# Задани 1(1)
# def sh_1_sh_2_zamena(slovo,slovar):
#     str1 = ""
#     for st in slovo:
#         for key, val in dict.items(slovar):
#             for key1, val1 in dict.items(val):
#                 if ord(key1) == ord(st):
#                     str1 += key
#                 elif ord(val1) == ord(st):
#                     str1 += key
#     return str1
#
#
# ///////////////////////////////////////////
# Задание 1(
# def generate_key(word, key):
#     gen_key = ""
#     while len(word) > len(gen_key):
#         for st in key:
#             if len(word) > len(gen_key):
#                 gen_key += st
#     return gen_key
#
#
# def hash_vijner(word, key, slovar):
#     gen_key = generate_key(word, key)
#     str1 = []
#     for kk in gen_key:
#             str1.append(slovar.index(kk))
#     str2 = []
#     for lo in word:
#             str2.append(slovar.index(lo))
#     x = ''
#     for i in range(0, len(str2)):
#         y = (str1[i] + str2[i]) % len(slovar)
#         x += (slovar[y])
#     return x
#
# //////////////////////////////////////////
# Задание 1(4,5)
# def de_hash_vijner(word, key, slovar):
#     gen_key = generate_key(word, key)
#     str1 = []
#     for kk in gen_key:
#         if kk in slovar:
#             str1.append(slovar.index(kk))
#     str2 = []
#     for lo in word:
#         if lo in slovar:
#             str2.append(slovar.index(lo))
#     x = ''
#     for i in range(0, len(str2)):
#         y = (str2[i] - str1[i] + len(slovar)) % len(slovar)
#         x += (slovar[y])
#     return x
#
#
# ////////////////////////////////////////////////////////////////
# Задание 2(6,7)
# def x_16(str):
#     a = bin((int(str, 16)))
#     return a
#
#
# def x_2(str):
#     a = bin((int(str, 2)))
#
#     return a
#
#
# def x_2_in_x_16(str):
#     a = int(str, 2)
#     b = hex(a)
#     return b[2:]
#
#
# def koks(str1, str2):
#     n1 = int(str1, 2)
#     n2 = int(str2, 2)
#     bit_or = n1 + n2
#     kek = bin(bit_or)
#     return kek[2:]
#
# def key_de_koks(str1, str2):
#     n1 = int(str1, 2)
#     n2 = int(str2, 2)
#     bit_or = n1 - n2
#     kek = bin(bit_or)
#     return kek[2:]
#
# /////////////////////////////////////////////////////////
# ЗАдание 3(8)
# def my_bust(word,key):
#     stroka = ""
#     for k in key:
#         for i,j in enumerate(word):
#             if i+1 == int(k):
#                 stroka += j
#     return stroka
#
# def method_perstanovka(word,key):
#     word1 = word[:len(key)]
#     word2 = word[len(key):]
#
#     lol = my_bust(word1,key)
#     lol2 = my_bust(word2,key)
#
#     return lol + lol2

#

# задание 3(9) дешифровка строки по ключу
# def de_method_perestanovka(word, key):
#     st1 = []
#     st2 = []
#     st3 = {}
#     st4 = ""
#     for lo in word:
#         for ko in key:
#             if word.index(lo) == key.index(ko):
#                 st3[ko] = lo
#     for key1, val1 in sorted(dict.items(st3)):
#         st4 += val1
#     return st4


# Задание 3(10)
# расшифровка ключа
# def search_d(word1, word2):
#     word1_1 = word1[:5]
#     word1_2 = word2[:5]
#     # print(word1_1)
#     str2 = []
#     for i, j in enumerate(word1_1):
#         for k_1, w_s in enumerate(word1_2):
#             if j == w_s:
#                 stroch = k_1+1
#                 str2.append(stroch)
#     lool = ""
#     for st in str2:
#             lool += str(st)
#     return lool

#def my_bust(word, key):
#     stroka = ""
#     for k in key:
#         for i, j in enumerate(word):
#             if i + 1 == int(k):
#                 stroka += j
#     return stroka
#
#
# def method_perstanovka_5_5(word, key):
#     word_a_1 = word_1[:len(key_p)]
#     word_a_2 = word_1[len(key_p):len(key_p) + len(key_p)]
#     word_a_3 = word_1[len(key_p) + len(key_p): len(key_p) + len(key_p) + len(key_p)]
#     word_a_4 = word_1[len(key_p) + len(key_p) + len(key_p): len(key_p) + len(key_p) + len(key_p) + len(key_p)]
#     word_a_5 = word_1[
#                len(key_p) + len(key_p) + len(key_p) + len(key_p): len(key_p) + len(key_p) + len(key_p) + len(
#                    key_p) + len(
#                    key_p)]
#
#     lol = my_bust(word_a_1, key_p)
#     lol2 = my_bust(word_a_2, key_p)
#     lol3 = my_bust(word_a_3, key_p)
#     lol4 = my_bust(word_a_4, key_p)
#     lol5 = my_bust(word_a_5, key_p)
#
#     return lol + lol2 + lol3 + lol4 + lol5


# def last_fun(word,slovar):
#     listik = wrap(word,3)
#     str3 = []
#     for symbol in listik:
#         for key, val in dict.items(slovar):
#             for va in val:
#                 if symbol == va:
#                     str3.append(key)
#     str4 = ""
#     for stu in str3:
#         str4 += stu
#     return str4
#

# if __name__ == "__main__":
#     print("ЗАдание 1")
#     str12 = "И.РЮУ.ЪФОБГНО"
#     str123 = "▽*!(∞♦^№>#⊕"
#     print(sh_1_sh_2_zamena(str12, slovar1))
#     print(sh_1_sh_2_zamena(str123, slovar1))
#     print()
#     print()


#     print("Шифр Вижнера.Зашифровал")
#     slovar1 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
#     slovar1_1 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"
#     print("Расшифровать слова с помощью ключа ОРЕХ")
#     key1 = "ОРЕХ"
#     word = "ШВМБУЖНЯ"
#
#     cryped = hash_vijner(word, key1, slovar1)
#
#     print(cryped)
#
#     decrypted = de_hash_vijner(word, key1, slovar1_1)
#
#     print(decrypted)
#
# print("Задание 2(6)")
# strok1 = "A5"
# strok2 = "01110111"
# xe = koks(x_16(strok1), x_2(strok2))
# print(x_2_in_x_16(xe))


# print("Задание 2(7)")
# before_strok = "74"
# key_g = "9A"
# xe = key_de_koks(x_16(key_g), x_16(before_strok))
# print(x_2_in_x_16(xe))


# print("Задание3(8)")
# perst = "ЖЁЛТЫЙ_ОГОНЬ"
# key_warg = "436215"
# print(method_perstanovka(perst,key_warg))
# perst1 = "МЫ_НАСТУПАЕМ"
# key_warg1 = "436215"
# print(method_perstanovka(perst1,key_warg1))


#
# print("Задание 3(9)")
# word_1 = "СЛПИЬНАЕ"
# key_1 = "64275813"
# word_2 = "РОИАГДВН"
# key_2 = "64275813"
# print(de_method_perestanovka(word_1,key_1))
# print(de_method_perestanovka(word_2,key_2))


# print("задание 3(10)")
# word_s = "МОЙ ПАРОЛЬ"
# word_d = "ЙПМ ООЬАЛР"
# print("Ключ d = ",search_d(word_s,word_d))
# word_k = "СИГНАЛ БОЙ"
# word_j = "НИСАГО ЛЯБ"
# print("Ключ d =",search_d(word_k,word_j))


# print("Задание 3(11)")
# key_p = "41235"
# word_1 = "ШИРОКОПОЛОСНЫЙ УСИЛИТЕЛЬ"
# word_2  = "ПЕРЕДАЧА ИЗОБРАЖЕНИЯ"
# print(method_perstanovka_5_5(word_1, key_p))
# print(method_perstanovka_5_5(word_2, key_p))



# word1 = "353214764134136759136762849754128212350354035767106216753211"
# word2 = "351 761756130532128759353134758105757213101752352763211762"
# # listik = []
# # listik = word.split(" ")
# slovar4 = {'А': ['760', '128', '350', '201'], 'Б': ['101'], 'В': ['210','106'], 'Г': ['351'],
#           'Д': ['129'],'Е': ['761', '130','802','352'], 'Ж': ['102'],'З': ['753'],'И': ['762','211','131'],
#           'К': ['754','764'],'Л': ['132','354'],'М': ['755','742'],'Н': ['763','756','212'],
#           'О': ['757','213','765','133','353'],'П': ['743','766'],
#           'Р': ['134','532'],'С': ['800','767','105'],'Т': ['759','135','214'],'У': ['544'],'Ф': ['560'],'Х': ['768'],
#           'Ц': ['545'],'Ч': ['215'],'Ш': ['103'],'Щ': ['752'],'Ъ': ['561'],
#           'Ы': ['136'],'Ь': ['562'],'Э': ['750'],'Ю': ['570'],'Я': ['216','104'], ' ':['751','769','758','801','849','035']}
#
# print(last_fun(word1,slovar4))
# print(last_fun(word2,slovar4))


