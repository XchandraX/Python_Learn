# O(logn n) - Waktu Logaritmik (Good)
"""
Sangat efisien untuk data besar. Algortma membelah jumlah data menjadi setengah pada setiap langkah operasi. 
Jika Kita memiliki 1.000.000 data, algoritma ini maksimal hanya butuh sekitar 20 langkah untuk menemukan jawabannya.
"""

# konsep O(log n) pada Binary Search (asumsi data sudah urut)
def binary_search(arr, target):
    kiri, kanan = 0, len(arr) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if arr[tengah] == target:
            return tengah
        elif arr[tengah] < target:
            kiri = tengah + 1   # Buang setengah data kiri
        else:
            kanan = tengah - 1  # Buang setangah dara kanan
    return -1

print(binary_search([2, 4, 5, 6, 8, 43, 6], 8))