def data_karyawan(**info):
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")

data_karyawan(nama="Andi", divisi="Keuangan", lokasi="Jakarta")