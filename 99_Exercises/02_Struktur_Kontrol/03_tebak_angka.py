
# 3. Buat program tebak angka sederhana pakai while: 
# komputer punya anka rehasia (misal angka_rahasia = 7), 
# users terus menebak sampai benar, program kasih tau 
# "Terlalu besar" / "Terlalu kecil" / "Benar!".

import random

"""
Pertama, bikin variable angka, Izin aku cari di internet agar angka ini bisa random

kedua, kita pake while untuk menembak angka 

Ketiga, kita bikin logikanya:

Jika angka tebak benar, tampilkan kata benar dan selesai
Jika angka tebak terlalu besar, tampilankan kata Terlalu Benar dan ulangin
Jika angka tebak terlalu kecil, tampilankan kata Terlalu Kecil dan ulangin
"""

angka = random.randint(1, 80)
while True:
    try: 
        tebak = float(input("Masukkan angka: "))
        if tebak == angka:
            print("Benar!")
            break
        elif tebak > angka:
            print("Terlalu Besar")
        elif tebak < angka:
            print("Terlalu Kecil")
    except ValueError:
        print("Format salah")