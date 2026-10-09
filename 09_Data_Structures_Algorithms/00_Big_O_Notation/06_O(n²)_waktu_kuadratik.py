# O(n²) - Waktu Kuadratik (Horrible)
"""
Waktu eksekusi berlipat ganda secara kuadrat. Jika data bertambah 10 kali lipat.
waktunya bertambah 100 kali lipat. Biasanya ditandai dengan adanya perulangan di dalam perulangan (nested loops).
Sangat berbahaya dan lambat jika jumlah data mencapai ribuan.
"""

data = [1, 2, 3, 4, 5]

# O(n^2) - Nested Loop (Looping di dalam Looping)
for i in data:
    for j in data:
        print(f"Pasangan: {i}, {j}")