"""
Tuple: Kumpulan data terurut (ordered), namun bersifat immutable
(nilainya tidak dapt diubah setelah didefinisikan).
Didefinisikan menggunakan kurung biasa ().

"""

# Membuat tuple

warna = ("Merah", "Hijau", "Biru")

# PERHATIAN: Tuple dengan 1 elemen WAJIB memiliki koma di akhir
tuple_satu = ("Apel", )

print(warna[0])

# warna[0] = "Kuning"
# TypeError: 'tuple' object does not support item assignment

# warna.append("Hitam")
# AttributError: 'tuple' object has no attribute 'append'

def user_info():
    return "Siti", "admin", "siti@mail.com"

nama, role, emial = user_info()

print(nama)
print(role)

angka =(1, 2, 3, 4, 5, 6, 7)
a, b, *sisanya = angka

print(a)
print(sisanya)

lokasi = {
    (-6.1, 106.8): "Jakarta",
    (-7.2, 112.7): "Surabaya"
}

if lokasi[(-6.1, 106.8)]:
    print(f"Saya sedang di Jakarta")

print(lokasi)