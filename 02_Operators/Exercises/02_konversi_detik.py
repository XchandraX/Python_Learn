total_detik = int(input("Masukkan Total Detik: "))

jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60


print(f"{jam} jam, {menit} menit, {detik} detik")