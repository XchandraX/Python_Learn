# Merge Sort (Metode Pecah & Gabung)
"""
Merge Sort adalah algoritma yang jauh lebih cerdas dan cepat.
Ia menggunakan strategi Divide and Conquer (Bagi dan Taklukkan) 
serta memanfaatkan konsep Rekursi

Cara Kerja:

1. Divide (Pecah): Belah list menjadi dua bagian (kiri dan kanan) secara terus-menerus sampai
    setiap list  hanya berisi 1 elemen. (List dengan 1 elemen sudah pasti terurut, bukan?)

2. Conquer & Combine (Gabung): Gabungkan kembali list-list kecil tersebuth secara perlahan sambil
    mengurutkannya, membandingkan elemen terdepan dari list kiri dan list kanan

3. Terus lakukan penggabungan ke atas hingga terbentuk kembali satu list utuh yang sudah terurut.

Kompleksitas Waktu: O(n log n) - Jauh lebih cepat dan efisien dibandingkan Bubble Sort, sehingga sangat aman digunakan untuk ribuan data.
"""

def merge_sort(arr):
    # Base Case: Jika array hanya 1 elemen, langsung kembalikan
    if len(arr) <= 1:
        return arr

    # Pecah Arry menjadi dua
    tengah = len(arr) // 2
    kiri = arr[:tengah]
    kanan = arr[tengah:]

    # Rekursi: Pecah terus sampai tinggal 1 elemen
    kiri = merge_sort(kiri)
    kanan = merge_sort(kanan)

    # Gabungkan kembali sambil diurutkan
    return gabung(kiri, kanan)

# Fungsi bantuan (Helper) untuk menggabungkan dua array yang sudha terurut
def gabung(kiri, kanan):
    hasil = []
    i = j = 0

    # Selama kedua list masih punya elemen
    while i < len(kiri) and j < len(kanan):
        if kiri[i] < kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1

    # Masukkan sisa elemen jika salah satu list sudah habi
    hasil.extend(kiri[i:])
    hasil.extend(kanan[j:])

    return hasil

# Contoh Penggunaan
angka = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(angka))
# Output: [3, 9, 10, 27, 38, 43, 82]