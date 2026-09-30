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
