karyawan = {
    "id": 100,
    "nama": "Budi Santoso",
    "departemen": "IT",
    "gaji": 7500000,
    "aktif": True
}

print(karyawan["nama"])
print(karyawan.get("departemen"))
karyawan["gaji"] = 8000000
karyawan["kota"] = "Kunignan"
del karyawan["aktif"]

for key, value in karyawan.items():
    print(f"{key.capitalize()}: {value}")