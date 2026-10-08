# Bubble Sort (Metode Gelembung)
"""
Bubble Sort adalah algoritma pengurutan paling sederhana, tetpai juga paling lambat.

Cara Kerja:

1. Bandingkan dua elemen yang bersebelahan (mulai dari elemen ke-1 dan ke-2).

2. Jika elemen pertama lebih besar dari elemen kedua. tukar posisi (swap) keduanya.

3. Geser ke pasangan berikutnya (elemen ke-2 dan ke-3) lakukan perbandingkan lagi.

4. Ulangi proses ini sampai ke ujung list. Di akhir iterasi pertama, angka terbesar pasti akan "menggelembung" (Bubble Up) ke posisi paling akhir.

5. Ulangi seluruh proses dari awal berulang-ulang sampai tidak ada lagi pertukaran yang terjadi.

Kompleksitas Waktu: O(n²) - Sangat lambat untuk data berjumlah besar karena menggunakan nested loop (perulangan di dalam perulangan).
"""

def bubble_sort(arr):
    n = len(arr)
    # Loop sebanyak jumlah elemen
    for i in range(n):
        sudah_urut = True

        # Loop untuk membandingkan elemen bersebelahan
        # (n - i - 1) karena elemen terakhir sudah pasti berada di posisi benar
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Tukar posisi menggunakan car Pythonic
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sudah_urut = False

        # Optimasi: Jika dalam satu putaran penuh tidak ada pertukaran,
        # bearti data sudah urut, hentikan loop.
        if sudah_urut:
            break

    return arr

# Contoh Pneggunaan
angka = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(angka))
# Output: [11, 12, 22, 25, 34, 64, 90]