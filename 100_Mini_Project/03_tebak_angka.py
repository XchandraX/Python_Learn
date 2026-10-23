# Tebak Angka

import random 

angka_rahasia = random.randint(1, 100)
angka_percobaan = 0

print("=== Tebak Angka ===")

while True:
    try:
        angka = int(input("Masukkan Angka: "))
    except ValueError:
        print("Format salah")
        continue

    angka_percobaan += 1
    if angka == angka_rahasia:
        print("Benar")
        break
    elif angka > angka_rahasia:
        print("Angka terlalu besar")
    else:
        print("Angka terlalu kecil")


print("=== Jumlah Percobaan ===")
print(f"{angka_percobaan}x")