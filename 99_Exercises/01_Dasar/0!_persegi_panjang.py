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

