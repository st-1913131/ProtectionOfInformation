import ceasar as c
import re
from collections import Counter
import string


def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])


def input_key():
    print("Введите ключ:")
    func_key = input().lower()
    while (not (c.is_unique(func_key))) or (len(func_key) > 32 or len(func_key) < 0) or not c.isContainsRussianLetters(func_key):
        print("Неправильный ключ, повторите ввод")
        func_key = input().lower()
    return func_key


def input_index():
    print("Введите индекс сдвига:")
    func_index = input()
    while not func_index.isdigit() or (int(func_index) > 32 or int(func_index) < 0):
        print("Неправильный индекс, повторите ввод")
        func_index = input()
    return func_index


def input_message():
    print("Введите сообщение:")
    func_message = input().lower()
    return func_message


spec_chars = string.punctuation + '\n\xa0«»\t—… '
spec_chars2 = "!\"#$%&'()*+-./:;<=>?@[\]^_`{|}~" + "\xa0,\xa0"

Alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
FrequencyOfLetters = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё'

while 1:
    print("\n1 - Шифр цезаря с ключом и сдвигом\n2 - Шифр цезаря модифицированный\n3 - Шифрование и дешифрование главвы книги\n0 - Завершение программы\nВведите номер:")
    number = input()
    if number.isdigit():
        number = int(number)

        if number == 1:
            print("~~~~\tШифр цезаря с ключом и сдвигом\t~~~~")
            key = input_key()
            index = input_index()
            message = input_message()
            c.caesar(key, index, message, is_print=True)

        elif number == 2:
            print("~~~~\tШифр цезаря модифицированный\t~~~~")
            key2 = input_key()
            message2 = input_message()
            c.caesar2(key2, message2)

        elif number == 3:
            print("~~~~\tШифрование и дешифрование главы книги\t~~~~")

            with open('texts/WarAndPeaceOriginal.txt', 'rt') as text_original: #открываем файл для чтения
            # with open('texts/war.txt', 'rt', encoding="utf-8") as text_original:
                poem = text_original.read()
                poem = (re.sub('[a-z|A-Z|A-Z|a-z]', '', poem)).lower() # .strip() #удаление нерусских символов


                poem2 = remove_chars_from_text(poem, spec_chars) #удаление специальных символов
                poem2 = remove_chars_from_text(poem, string.digits) #удаление чисел

                bigrams = Counter(re.findall(r'(?=([а-я]{2}))', poem2)).most_common(10) #подсчёт 10 самых популярных биграм в оригинальном тексте
                print("Биграммы в оригинальном тексте: ")
                # print(bigrams)

                list_of_bigrams = str(bigrams)
                list_of_bigrams = remove_chars_from_text(list_of_bigrams, string.digits)
                list_of_bigrams = remove_chars_from_text(list_of_bigrams, spec_chars2).split()
                print(list_of_bigrams)

            key = 'ключ'
            index = 3
            # key = input_key()
            # index = input_index()
            # c.caesar(key, index, poem2, is_print = False)

            with open('texts/WarAndPeaceEncrypted.txt', 'w') as text_encrypted:
                # запись в файл зашифрованного цезарем текста
                text_encrypted.write(c.caesar(key, index, poem, is_print=False)) #poem2

            new_text = c.caesar(key, index, poem, is_print=False) #poem2

            letters_decr = Counter("".join([ch for ch in new_text if ch in Alphabet])) #подсчёт букв по популярности
            # print(letters_decr)
            # list_of_letters = list(letters_decr.items())
            # list_of_letters.sort(key=lambda i: i[1])
            # list_of_letters.reverse()
            # print(list_of_letters)

            Message3 = []

            list_of_letters = str(letters_decr)
            # list_of_letters = str(list_of_letters)
            list_of_letters = remove_chars_from_text(list_of_letters, spec_chars)
            list_of_letters = remove_chars_from_text(list_of_letters, string.digits)
            list_of_letters = list_of_letters[7:]
            # print(list_of_letters)

            with open('texts/WarAndPeaceDecrypted.txt', 'wt') as text_decrypted:
            #запись в файл расшифрованного цезарем текста
                for char_new in new_text:
                    try:
                        index_new = list_of_letters.index(char_new)
                        new_char = FrequencyOfLetters[index_new]
                        Message3.append(new_char)
                    except ValueError:
                        Message3.append(char_new)
                text_decrypted.write(''.join(Message3))

            FrequencyOfLettersUpd = FrequencyOfLetters
            FrequencyOfLettersUpd = list(FrequencyOfLettersUpd)

            with open('texts/WarAndPeaceDecrypted.txt', 'rt') as text_decrypted2:
                bigrams_new = text_decrypted2.read()
                # подсчёт 10 популярных биграм в расщиврованном тексте
                bigrams_new = Counter(re.findall(r'(?=([а-я]{2}))', bigrams_new)).most_common(10)
                print("Биграммы в расшифрованном тексте: ")
                # print(bigrams_new)
                list_of_letters3 = str(bigrams_new)
                list_of_letters3 = remove_chars_from_text(list_of_letters3, string.digits)
                list_of_letters3 = remove_chars_from_text(list_of_letters3, spec_chars2).split()
                print(list_of_letters3)


            for a in range(len(list_of_letters3)):
                if list_of_letters3[a] != list_of_bigrams[a]:
                    # for x, y in product(list_of_letters3[a], list_of_bigrams[a]):
                    x = list_of_letters3[a]
                    y = list_of_bigrams[a]
                    # находим и меняем неправильный символ
                    if x[0] != y[0]:
                        index1 = FrequencyOfLetters.index(x[0])
                        FrequencyOfLettersUpd[index1] = y[0]
                        index11 = FrequencyOfLetters.index(y[0])
                        FrequencyOfLettersUpd[index11] = x[0]
                    if x[1] != y[1]:
                        index2 = FrequencyOfLetters.index(x[1])
                        FrequencyOfLettersUpd[index2] = y[1]
                        index22 = FrequencyOfLetters.index(x[1])
                        FrequencyOfLettersUpd[index22] = y[1]
                    # print(list_of_letters3[a])
            print("\nАлфавит до биграммного анализа: ")
            print(list(FrequencyOfLetters))
            print("Алфавит после биграммного анализа:")
            print(FrequencyOfLettersUpd)

            q = open('texts/WarAndPeaceDecrypted.txt', 'r')
            qq = q.read()
            Message4 = []
            with open('texts/WarAndPeaceDecryptedBetter.txt', 'wt') as text_decrypted3:
                # улучшаем расшифровку текста с помощью биграм
                for charr in qq:
                    try:
                        index1 = FrequencyOfLetters.index(charr)
                        index2 = FrequencyOfLettersUpd.index(charr)
                        if index1 != index2:
                            character2 = FrequencyOfLettersUpd[index1]
                            Message4.append(character2)
                        else:
                            Message4.append(charr)
                    except ValueError:
                        Message4.append(charr)

                text_decrypted3.write(''.join(Message4))

            text_original.close()
            text_encrypted.close()
            text_decrypted.close()
            text_decrypted2.close()
            text_decrypted3.close()

        elif number == 0:
            break