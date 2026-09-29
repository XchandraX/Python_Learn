"""
While loop digunakan ketika Anda tidak tahu past berapa kali kode harus diulang.
tetapi Anda memiliki suatu kondisi logika yang menentukan kapan perulangan harus terus berjalan
dan kapan harus berhenti
"""

# Sintaks Dasar
"""
while kondisi_bernilai_true
"""
    # Blok kode yang dijalankan

# Contoh Penggunaan:
stok_barang = 5 

while stok_barang > 0:
    print(f"Barang terjual! Sisa stok: {stok_barang}")
    stok_barang -=1 # Sangat penting: Perbarui kondisi agar loop tidak berjalan tanpa akhir

print("Barang hasil!")
