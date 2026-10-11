def kembalian_minimum(koin_tersedia, target):
    dp = [float('inf')] * (target + 1)

    dp[0] = 0

    for i in range(1, target + 1):
        for koin in koin_tersedia:
            if koin <= i:
                dp[i] = min(dp[i], dp[i, koin] + 1)

    if dp[target] == float('inf'):
        return -1

    return dp[target]

# --- Mari Kita Uji ---
koin = [1, 3, 4]
target_kembalian = 6

hasil = kembalian_minimum(koin, target_kembalian)
print(f"Koin minimum untuk {target_kembalian} adalah: {hasil} koin")
# Output: Koin minimum untuk 6 adalah: 2 koin

# Kompleksitas Performa
"""
- Waktu (Time Complexity): O(target x jumlah koin),
Algoritma melakukan dua perulangan (nested loop); satu untuk menelusuri dari 1 hingga target,
dan satu lagi untuk setiap jenis koin.

- Ruang (Space Complexity): O(target). Kita membutuhkan memori sebesar target + 1 untuk menyimpan tabel dp.
"""