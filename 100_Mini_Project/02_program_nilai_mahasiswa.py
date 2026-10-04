# TODO
# Membuat Program Nilai Mahasiswa

dataMahasiswa = []

#########################
# PENGULANGAN INPUT
#########################

while True:
    # Masukkan Nama mahasisaw atau ketik selesai / end
    nama = input("Masukkan Nama Mahasiswa (atau ketik 'selesai'/'end' untuk selesai): ")

    # Jika input nama, selesai atau end, berhentikan looping
    if nama.lower() in ["selesai","end"]:
        print("Input selesai, TerimaKasih")
        break

    # Masukkan nilai, jika nilai valid, looping
    try:
        nilai = int(input("Masukkan Nilai Mahasiswa: "))
    except ValueError:
        print("Masukkan Angka yang valid")
        print("-----------------------")
        continue

    # Jika nilai "n" jadikan grade "n"
    if nilai >= 85:
        grade = "A"
    elif nilai >= 75:
        grade = "B"
    elif nilai >= 70:
        grade = "C"
    elif nilai >= 60:
        grade = "D"
    else:
        grade = "E"

    # Buat Dictionary
    mahasiswa_baru = {
        "nama": nama.capitalize(),
        "nilai": nilai,
        "grade": grade,
    }

    # Masukkan Dictionary kedalam list
    dataMahasiswa.append(mahasiswa_baru)

    # Jika data masuk tanpa hambatan, kasih tau user
    print(f"Data {nama} berhasil dicatat")
    print("-----------------------")

#########################
# PENGULANGAN INPUT (END)
#########################


#########################
# HASIL
#########################

print("=========================")
print("      DATA MAHASISWA     ")
print("=========================")

total_nilai = 0

for mhs in dataMahasiswa:
    print(f"Nama     : {mhs['nama']}")
    print(f"Nilai    : {mhs['nilai']}")
    print(f"{mhs['nama']} Mendapatkan {mhs['grade']}")
    total_nilai += mhs["nilai"]
    print("")

if len(dataMahasiswa) > 0:
    rata_rata = total_nilai / len(dataMahasiswa)
    print(f"Rata-rata nilai: {rata_rata:.1f}")
else:
    print("Tidak ada data mahasiswa yag dimasukkan.")
print("=========================")

#########################
# HASIL (END)
#########################