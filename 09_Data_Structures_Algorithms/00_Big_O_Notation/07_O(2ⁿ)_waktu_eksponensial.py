# O(2ⁿ) - Waktu Eksponensial (Disaster)
"""
Algoritma paling tidak efisien. Waktu eksekusi berlipat ganda setiap kali jumlah data bertambah SATU.
Algoritma dengan O(2ⁿ) akan membuat komputer terhenti (hang) bahkan hnaya dengan n = 50. 
Sering terjadi pada fungsi rekursif yang menghitung nilai yang sama berulang-ulang tanpa menyimpannya.
"""

# O(2ⁿ) - Rekursi Naif tanpa Memoization
def fibonacci(n):
    if n <= 1:
        return n
    # Memanggil dirinya sendiri DUA KALi pada setiap langkah
    return fibonacci(n-1) + (fibonacci(n - 2))