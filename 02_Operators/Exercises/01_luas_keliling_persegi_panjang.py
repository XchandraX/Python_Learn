print("Program hitung Luas dan Keliling Persegi Panjang.\n")

panjang = int(input("Masukkan panjang persegi panjang: "))
lebar = int(input("Masukkan lebar persegi panjang: "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print(f"""
Luas dari Persegi Panjang ini adalah: {luas}\n
Keliling dari Persegi Panjang ini adalah: {keliling}
""")