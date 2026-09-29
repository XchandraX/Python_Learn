"""
SET

"""

## Membuat Set

# Duplikat akan otomatis dihilangkan
angka = {1, 2, 3, 4, 5, 5, 6}
print(angka)

# Membuat set dari tipe data lain (Misal: List ke Set)
huruf = set(["a", "b", "c", "c"])
print(huruf)
print(type(huruf))

# PERHATIAN: Membuat set kosong WAJIB menggunakan set()
# Menggunakan {} akan membuat Dictionary kosong, bukan Set!
set_kosong = set()

## Menambah and Menghapus Elemen

keranjanag = {"Apel", "Mangga"}
print(keranjanag)
# Menambah elemen
keranjanag.add("Jeruk")
print(keranjanag)

# Menghapus elemen (Menghasilkan error jika elemen tidak ada)
keranjanag.remove("Apel")
print(keranjanag)

# Menghapus elemen dengan aman (tidak error jika elemen tidak ada)
keranjanag.discard("Pisang")
print(keranjanag)

## Operasi Matematika Himpunan

grup_a = {1, 2, 3, 4}
grup_b = {3, 4, 5, 6}

# 1. Union / Gabuangan (|)
# Menggabungkan semau elemen dari kedua set tanpa duplikat
print(grup_a | grup_b)  # Output: {1, 2, 3, 4, 5, 6}

# 2. Intersection / Irisan (&)
# Mengambil elemen yang hanya ada di KEDUA set
print(grup_a & grup_b)   # Output: {3, 4}

# 3. Difference / Selisih (-)
# Mengambil elemen yang ada di grup_a, TAPI TIDAK ADA di grup_b
print(grup_a - grup_b)  # Output: {1, 2}

# Mengambil elemen yang ada di grup_b, TAPI TIDAK ADA di grup_a
print(grup_b - grup_a)  # Output: {5, 6}

# 4. Symetric Difference (^)
# Megambil elemen yang unik di masing-masing set (irisan dibuang)
print(grup_a ^ grup_b)  # Output: {1, 2, 5, 6}