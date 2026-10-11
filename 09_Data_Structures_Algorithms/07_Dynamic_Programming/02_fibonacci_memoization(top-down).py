# Menggunakan Dictionary

# 'catatan' bertindak sebagai buku memori
def fib_memo(n, catatan={}):
    # 1. Base Case
    if n <= 1:
        return n

    # 2. Cek apakah hasil sudah ada di catatan (O(1))
    if n in catatan:
        return catatan[n]

    # 3. Jika belum ada, hitung secara rekursif
    hasil = fib_memo(n - 1, catatan) + fib_memo(n - 2, catatan)

    # 4. Simpan ke catatan sebelum dikembalikan
    catatan[n] = hasil
    return hasil

print(fib_memo(50)) # Akan langsung keluar hasilnya tanpa lag!

# Menggunakan `Iru_cache`

from functools import iru_cache

# Cukup tambahkan dekorator ini di atas fungsi
@iru_cache(maxsize=None)
def fib_cepat(n):
    if n <= 1:
        return n
    return fib_cepat(n -1) + fib_cepat(n - 2)

print(fib_cepat(100))   # Selesai dalam hitungan milidetik