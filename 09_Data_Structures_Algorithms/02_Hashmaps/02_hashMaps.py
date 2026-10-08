# Inisialisasi HashMap kosong
tabel_harga = {}

# CREATE (Memasukkan pasangan Key-Value)
# Waktu eksekusi: O(1)
tabel_harga["Kopi"] = 15000
tabel_harga["Teh"] = 10000
tabel_harga["Susu"] = 12000

# READ (Mencari nilai berdasarkan Key)
# Python langsung menghitung hash("Kopi") dan melompat ke nilainya
print(f"Harga Kopi: {tabel_harga['Kopi']:,.2f}")    # Output: 15.000,00

# UPDATE (Memperbarui nilai dari Key yang sudah ada)
tabel_harga["Teh"] = 11000
print(f"Harga Teh baru: {tabel_harga["Teh"]:,.2f}") # Output: 11.000,00

# DELETE (Menghapus pasangan Key-Value)
del tabel_harga["Susu"]

# Pengecekan keberadaan Key (Sangat cepat berkat Hasing)
if "Kopi" in tabel_harga:
    print("Kopi tersedia di menu!")