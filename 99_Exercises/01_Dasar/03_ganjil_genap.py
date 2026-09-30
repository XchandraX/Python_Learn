# Buat program cek apakah sebuah angka itu gangil atau genap
# tapi jangan pakai if dulu, coba cari cara paaki operator saja

"""
Pertama, bikin input untuk mengambil data(angka) user

Kedua, data itu di bagi pake operator (%), jika sisa 1 artinya bilangan itu ganjil

Ketiga, bikin variable ganjil dan genap, jika '==' 1 artinya ganjil, jika '==' 0 artinya genap

Keempat, Kasih tau user apakah angka ini ganjil atau genap
"""

print("Program cek ganjil genap\n")

angka = input("Masukkan angka: ")

cek_angka = int(angka) % 2 # jika sisa 1 artinya ganjil, jika habis artinya genap

ganjil = cek_angka == 1
genap = cek_angka == 0


print(f"Angka ini Genap: {genap}")
print(f"Angka ini Ganjil: {ganjil}")