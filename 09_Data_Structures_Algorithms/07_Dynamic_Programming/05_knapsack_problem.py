def knapsack_01(kapasitas_maks, berat, nilai, jumlah_barang):
    dp = [[0 for x in range(kapasitas_maks + 1)] for y in range(jumlah_barang + 1)]

    for i in range(1, jumlah_barang + 1):
        for w in range(1, kapasitas_maks + 1):

            if berat[i-1] <= w:
                ambil = nilai[i-1] + dp[i-1][w - berat[i-1]]
                tidak_ambil = dp[i-1][w]
                dp[i][w] = max(ambil, tidak_ambil)

            else:
                dp[i][w] = dp[i-1][w]

    return dp[jumlah_barang][kapasitas_maks]

# --- Mari Kita Uji ---
nilai_barang = [60, 100, 120]   # Nilai jual ($)
berat_barang = [10, 20, 30]     # Berat (Kg)
kapasitas_ransel = 50           # Ransel Maksimal 50 kg
n = len(nilai_barang)

hasil_optimal = knapsack_01(kapasitas_ransel, berat_barang, nilai_barang, n)
print(f"Nilai maksimum yang bisa dibawa: ${hasil_optimal}")
# Output: Nilai maksimum yang bisa dibawa: $220 (Kombinasi barang ke-2 dan ke-3)

# Kompleksitas Performa

"""
- Waktu: O(n * W) di mana n adalah jumlah barang dan W adalah kapasitas maksimal ransel.
ini sangat cepat dibandingkan rekursi naif O(2^n)

- Ruang: O(n * W)
"""