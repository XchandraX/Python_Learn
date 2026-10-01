angka = int(input("Masukkan angka: "))

genap = angka % 2 == 0
ganjil = angka % 2 == 1

print(f"""
Angka ini Genap: {genap}
Angka ini Ganjil: {ganjil}
""")
