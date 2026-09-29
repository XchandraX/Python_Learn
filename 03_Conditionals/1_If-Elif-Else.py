"""
Metode percabangan yang paling umum digunakan untuk mengevaluasi ekspresi
logi atau perbandingan nilai.

Aturan Utama Sintaks:
- Menggunakan titik dua (:) di akhir setiap baris kondisi.
- Indentasi(spasi/tab) wajib digunakan untuk menentukan blok kode mana yg akan dieksekusi.
"""

nilai = 75

if nilai >= 85:
    print("Predikat: A (Sangat Baik)")
elif nilai >= 70:
    print("Predikat: B (Baik)")
elif nilai >= 60:
    print("Predikat: C (Cukup)")
else:
    print("Predikat: D (Tidak Lulus)")

"""
Penjelasan Komponen:
- if: Kondisi pertama yang selalu diperiksa di awal.
- elif (Else-if): Periksa kondisi ini jika kondisi if atau elif di atasnya
bernilai False. Anda dapat menambahkan beberapa elif sesuai kebutuhan.
- else: Blok opsional yg akan diesksekusi jika semua kondisi if dan elif sebelumnya bernilai False.
"""
