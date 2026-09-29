"""
List: Kumpulan data terurut (ordered), nilainya bisa diubah(mutable),
dan mengizinkan adanya elemen duplikat. 

Didefinisikan menggunakan kurung siku [].
"""

# 1. Membuat List (bisa berisi tipe data campuran)
keranjang = ["Apel", 42, 3.14, True]

# 2. Mengakses Elemen (Indeks dimulai dari 0)
print(keranjang[0])     # Output: Apel
print(keranjang[-1])    # Output: True (Mengakses dari belakang)
print(keranjang[1])     # Output: 42

# 3. Mengubah Elemen (Mutable)
keranjang[1] = 99   # Mengubah angka 42 menjadi 99
print(keranjang[1])

# 4. Menambah Elemen
keranjang.append("Mangga")      # Menambahkan ke akhir list
keranjang.insert(1, "Pisang")   # Menyisipkan di posisi indeks i
print(keranjang[-1])
print(keranjang[1])
print(len(keranjang))

# 5. Menghapus Elemen
keranjang.remove(3.14)              # Menghapus elemen berdasarkan nilai
item_terakhir = keranjang.pop(0)    # Menghapus dan mengambil elemen terakhir
print(keranjang)
print(item_terakhir)

print(len(keranjang))