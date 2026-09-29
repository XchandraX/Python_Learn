"""
Tuple: Kumpulan data terurut (ordered), namun bersifat immutable
(nilainya tidak dapt diubah setelah didefinisikan).
Didefinisikan menggunakan kurung biasa ().

"""

# Membuat tuple 
koordinat = (-6.175392, 106.827153)
warna_rgb = (255, 0, 0)

# Mengakses elemen berdasarkan indeks
print(koordinat[0]) #Output: -6.175392

# koordinat[0] = -6.200000 <-- ERROR: Tuple tidak bisa diubah!
print(type(koordinat)) # Output: <class 'tuple'>