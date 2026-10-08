# Faktorial dari 5 (ditulis 5!) adalah 5 * 4 * 3 * 2 * 1.

def hitung_faktorial(n):
    # Base Case: Jika n adalah 1 atau 0, faktorialnya adalah 1
    if n <= 1:
        return 1

    # REcursive Case: n dikalikan dengan faktorial dari n - 1
    else:
        return n * hitung_faktorial(n-1)

print(hitung_faktorial(5))  # Output: 120

# Cara Kerja di Balik layar:
# 1. `hitung_faktor(5)` mengembalikan `5 * hitung_faktorial(4)`
# 2. `hitung_faktor(4)` mengembalikan `4 * hitung_faktorial(3)`
# 3. Proses berlanjut sampai `hitung_faktorial(1)`
# 4. `hitung_faktor(1)` mengenai Base Case dan mengembalikan `1`.
# 5. Semua nilai kemudain dikalikan mundur: `1 * 2 * 3 * 4 * 5 = 120`