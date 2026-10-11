# Fibonacci dengan Tabulation
def fib_tabulation(n):
    # Menangani edge case
    if n <= 1:
        return n

    # 1. Siapkan 'tabel; (List) yang diisi dengan angak 0
    # Ukurannya n + 1 karena kita butuh indeks dar i0 sampai n
    dp = [0] * (n + 1)

    # 2. Isi nilai dasar (Base Case) secara manual di bagian paling 'bawah'
    dp[0] = 0
    dp[1] = 1

    # 3. Bergerak naik ke atas menggunakan perulangan biasa
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    # 4. Hasil akhir berada di ujung tabel
    return dp[n]

print(fib_tabulation(10))   # Output: 55


# Space Optimization
def fib_paling_optimal(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        # a dan b saling bergeser ke depan
        a, b = b, a + b

    return b

print(fib_paling_optimal(10))