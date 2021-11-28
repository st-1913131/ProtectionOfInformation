Alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def is_unique(s):
    return len(s) == len(set(s))


# def removeDuplicate(str): #удаление дубликатов в строке
#     if (len(str)) < 2:
#         return str
#     result = []
#     for i in str:
#         if i not in result:
#             result.append(i)
#     return ''.join(result)


def removeDuplicateAlphabet(str, alphabet): #удаление ключа из алфавита
    for i in alphabet:
        for j in str:
            if i == j:
                alphabet = alphabet.replace(i, '')
    return alphabet

def isContainsRussianLetters(str_check):
    flag = False
    for i in str_check:
        if ord('а') <= ord(i) <= ord('я'):
            flag = True
        else:
            flag = False
            break

    if flag:
        return True
    else:
        return False


def caesar(key, index, text, is_print = True):
    NewAlphabet = removeDuplicateAlphabet(key, Alphabet)
    NewAlphabet = NewAlphabet[-int(index):] + key + NewAlphabet[:-int(index)]

    message = []
    for character in text:
        try:
            index = Alphabet.index(character)
            character = NewAlphabet[index]
            message.append(character)
        except ValueError:
            message.append(character)

    if is_print:
        print('\nОригинальный алфавит:\t' + Alphabet)
        print('Новый алфавит:\t\t\t' + NewAlphabet)
        print("Зашифрованный текст: " + ''.join(message))

    return ''.join(message) #, NewAlphabet


def new_alph(key_word):
    key_word = list(key_word)
    # print('Old Alphabet:', '\t', Alphabet)
    new_alphabet = []
    counter = 0
    for i in range(len(list(Alphabet))):
        new_alphabet.append(key_word[counter])
        counter += 1
        if counter == len(key_word):
            counter = 0
    # print('New Alphabet:\t', new_alphabet)
    return new_alphabet


def caesar2(key2, text):
    NewAlphabet2 = new_alph(key2)
    # print('New Alphabet:', '\t', NewAlp)

    message = []

    for character in text:
        if character in Alphabet:
            index = Alphabet.index(character)
            new_char = NewAlphabet2[index]
            new_index = Alphabet.index(new_char)
            character2 = Alphabet[((index + new_index) % len(Alphabet))]
            message.append(character2)
        else:
            message.append(character)

    print('\nОригинальный алфавит:\t' + Alphabet)
    print('Новый алфавит:\t\t\t' + ''.join(NewAlphabet2))
    print("Зашифрованный текст: " + ''.join(message))

    return ''.join(message)