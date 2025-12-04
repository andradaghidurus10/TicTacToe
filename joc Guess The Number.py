import random

secret_number = random.randint(1, 100)

print(
"""
+================================+
|    Bine ai venit la joc!       |
|  Ghiceste numarul secret!      |
|  Este intre 1 si 100           |
+================================+
"""
)

while True:
    try:
        nr = int(input("Introdu numarul tau: "))
    except ValueError:
        print("Te rog introdu doar numere întregi!")
        continue

    if nr < secret_number:
        print("Numărul este mai mare! Încearcă din nou.")
    elif nr > secret_number:
        print("Numărul este mai mic! Încearcă din nou.")
    else:
        print("🎉 Felicitări! Ai ghicit numărul!")
        break
