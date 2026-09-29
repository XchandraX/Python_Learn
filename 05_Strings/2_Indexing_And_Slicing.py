# Setiap karakter dalam string memiliki posisi angka yg disebut Indeks.
# dimulai dari 0 untuk karakter pertama, atau negatif(-1) untuk mengakses dari belakang.

kata = "PYTHON"

# Indexing (Mengakses 1 Karakter)
print("Indexing:")
print(kata[0])  # Output: P (Karakter pertama)
print(kata[-1]) # Output: N (Karakter terakhir)

# Slicing (Mengambil Substring -> kata[start:end:step])
print("\nSlicing:")
print(kata[0:4])    # Output: PYTH (indeks 0 hingga 3, indeks 4 tidak termasuk)
print(kata[:3])     # Output: PYT (dari awal hingga indeks 2)
print(kata[2:])     # Output: THON (dari indeks 2 hingga akhir)
print(kata[::-1])   # Output: NOHTYP (membalikkan string)

