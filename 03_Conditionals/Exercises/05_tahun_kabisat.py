tahun = int(input("Masukkan tahun: "))

match tahun:
    case tahun if tahun % 4 == 0 and tahun // 100 >= 0 or tahun % 400 == 0:
        print(f"Tahun Kabisat")
    case _:
        print("Tahun Biasa")