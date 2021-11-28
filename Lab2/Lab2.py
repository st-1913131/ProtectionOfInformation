import random

# Открытые ключи, которыми обладают Элис и Боб

g = random.randint(0, 10000)
n = random.randint(0, 10000)

print("Public: \tg =", g)
print("Public: \tn =", n)

# Закрытые ключи, которыми обладают Элис и Боб

Alice_private_key = random.randint(0, 10000)
Bob_private_key = random.randint(0, 10000)

print("Private: \tAlice`s private key =", Alice_private_key)
print("Private: \tBob`s private key =", Bob_private_key)

# Создание частичного шифровального ключа

Alice_part_key = (g ** Alice_private_key) % n
Bob_part_key = (g ** Bob_private_key) % n

print("Private: \tAlice`s part key =", Alice_part_key)
print("Private: \tBob's part key =", Bob_part_key)

# Создание полного шифровального ключа

Alice_key_final = Bob_part_key ** Alice_private_key % n
Bob_key_final = Alice_part_key ** Bob_private_key % n

print("Public: \tAlice's key final =", Alice_key_final)
print("Public: \tBob's key final =", Bob_key_final)

#Проверка на сходимость

if Alice_key_final == Bob_key_final:
    print("\t\t Numbers converged")
else:
    print("Numbers didn`t converged")