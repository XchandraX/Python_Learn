# Tebak Angka

import random 

angka_rahasia = random.randint(1, 100)
angka_percobaan = 0

print("=== Tebak Angka ===")

while True:
    try:
        angka = int(input("Masukkan Angka: "))
        if angka == angka_rahasia:
            print("Benar")
            break
        elif angka >= angka_rahasia:
            print("Angka terlalu besar")
        elif angka <= angka_rahasia:
            print("Angka terlalu kecil")
        angka_percobaan += 1
    except ValueError:
        print("Format salah")

print("=== Jumlah Percobaan ===")
print(f"{angka_percobaan}x")