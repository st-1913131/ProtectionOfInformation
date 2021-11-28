import random

g = random.randint(0, 1000)
n = random.randint(0, 1000)

print("Public: \tg =", g)
print("Public: \tn =", n)

Alice_num = random.randint(0, 1000)
Bob_num = random.randint(0, 1000)

print("Private: \tAlice's number =", Alice_num)
print("Private: \tBob's number =", Bob_num)

Alice_key1 = (g ** Alice_num) % n
Bob_key1 = (g ** Bob_num) % n

print("Private: \tAlice's key1 =", Alice_key1)
print("Private: \tBob's key1 =", Bob_key1)

Alice_key_final = Bob_key1 ** Alice_num % n
Bob_key_final = Alice_key1 ** Bob_num % n

print("Public: \tAlice's key final =", Alice_key_final)
print("Public: \tBob's key final =", Bob_key_final)

if Alice_key_final == Bob_key_final:
    print("\t\t Success!")
else:
    print("Fail!")