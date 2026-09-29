# Gloabl
garis = "\n\n --------------------- \n\n"

# i. Buatkan program yang minta input panjang dan lebar persegi panjang,
#lalu hitung dan cetak luasnya.


"""
pertama kita cari rumus luas dari persegi panjang
panjang x lebar

kedua harus bikin input untuk mengambil data panjang dan lebar

ketiga, bikin variable hasil, jangan lupa pake int() untuk mengubah dari string jadi integer

keempat, tampilan ke user hasil dari luas persegi panjang
"""

print("Program untuk mencari Luas dari persegi panjang\n")

panjang = input("Berikan panjang dari persegi panjang = ")
lebar = input("Berikan lebar dari persegi panjang = ")

hasil_luas = int(panjang) * int(lebar)

print(f"Hasil dari Luas persegi panjang adalah = {hasil_luas}")


print(garis)
# 2. Buat program konversi suhu dari Celsius ke Fahrenheit 
# (F = C * 9/5 + 32), input dari user

"""
Pertama, kita bikin input untuk mengambil data celsius 

kedua, bikin variable untuk konversi dari nilai C ke F

ketiga, tampilan hasi nila knonversi ini ke user
"""

print("Program konversi suhu dari C ke F\n")

celsius = input("Masukkan input dari Celsius = ")

konversi = float(celsius) * 9/5 + 32

print(f"Hasil dari konversi dari C {celsius} ke fahrenheit adalah {konversi}")


print(garis)

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