# Global
garis = "\n\n --------------------- \n\n"
import random
# 1. FizBuzz - Cetak angka 1 sampai 20. Tapi kalau kelipatan 
# 3 cetak "Fizz", kelipatan 5 cetak "Buzz",
# kelipatan 3 dan 5 cetak "FizzBuzz."

"""
Pertama, Tentukan mengunakan Sintax yg digunakan

Kedua, bikin logika agar setiap kelipatan 3, 5 dan 3 and 5

Ketiga, pake for if dan range(1, 21)
""" 

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print(garis)

# 2. Buat fungsi cek_ganjil_genap(angka) yang me-return string "Ganjil" 
# atau "Genap" - For utnuk angka 1 sampai 10

"""
Pertama, Buat fungsi

Kedua, bikin logika agar setiap ganjil dan genap

Ketiga, pake for if dan range(1, 11)
""" 

def cek_ganjil_genap(angka):
    if angka % 2 == 1:
        return "Ganjil"
    else:
        return "Genap"

for i in range(1, 11):
    hasil = cek_ganjil_genap(i)
    print(i, hasil)

print(garis)

# 3. Buat program tebak angka sederhana pakai while: 
# komputer punya anka rehasia (misal angka_rahasia = 7), 
# users terus menebak sampai benar, program kasih tau 
# "Terlalu besar" / "Terlalu kecil" / "Benar!".

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