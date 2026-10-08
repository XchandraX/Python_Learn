# Head (Tumpukan Prioritas) - Prinsip Nilai Ekstrem
"""
Head bukanlah antrean berdasarkan waktu kedatangan, melainkan struktur data berbasis pohon (tree)
yang selalu memprioritaskan nilai terkecil (Min-Heap) atau nilai terbesar (Max-Heap) di posisi teratas.

Jika Kita memasukkan dat asecara acak ke dalam Heap, elemen dengan prioritas tertinggi akan selalu "mengapung" ke posisi pertama.

- Penerapan Utama: Menjadwalkan tugas berdasarkan tingkat urgensi (misal: antrean pasien UGD di rumah sakit), atau mencari rute terpendek peta (Algoritma Dijkstra).
- Implementasi di Python: Menggunakan modul bawaan `heapq`. Python secara default menerapkan Min-Heap (angka terkecil menjadi prioritas utama).
"""

# Contoh Pneggunaan Heap di Python
import heapq

# Membuat list acak
tugas = [5, 1, 8, 3]

# Mengubah list biasa menjadi struktur Min-Heap (O(n))
heapq.heapify(tugas)
print(tugas)    # Output: [1, 3, 8, 5] (Angka 1 otomatis berada di indeks 0)

# Memasukkan elemen baru (O(log n))
heapq.heappush(tugas, 2)

# Mengambil elemen dengan prioritas tertinggi (paling kecil) (O(log n))
print(f"Dikerjakan pertama: {heapq.heappop(tugas)}")    # Output: 1
print(f"Dikerjakan kedua: {heapq.heappop(tugas)}")    # Output: 2