kasir = []
total = 0
total_barang = 0

print("=== KASIR SEDERHANA ===")
print("ketik 'selesai' atau 'exit' untuk mengakhiri\n")

def tambah_barang():
    global total, total_barang

    while True:
        # --- Input Nama ---
        nama = input("Nama Barang: ").strip()
        
        if not nama:
            print("Nama barang tidak boleh kosong!\n")
            continue
        
        if nama.lower() in ["exit", "selesai"]:
            break

        # --- Input Harga --- 
        try:
            harga = int(input("Harga Barang: "))
            if harga < 0:
                print("Harga tidak boleh negatif!\n")
                continue
        except ValueError:
            print("Harga harus berupa angka!\n")
            continue

        # --- Input Qty ---
        try:
            qty = int(input("Jumlah Barang: "))
            if qty <= 0:
                print("Jumlah tidak boleh negatif!\n")
                continue
        except ValueError:
            print("Jumlah harus berupa angka!\n")
            continue

        # --- list kasir ---
        subtotal = harga * qty
        kasir.append((nama, harga, qty, subtotal))
        print(f"✓ {nama} x{qty} ditambahkan (Rp {subtotal:,})\n")

        # --- total ---
        total_barang += qty
        total += subtotal 

def hitung_total():
    # --- Daftar barang ---
    for nama, harga, qty, subtotal in kasir:
        print(f"{nama:<15} Rp {harga:>8,} x{qty:<3} = Rp {subtotal:>10,}\n")

    # --- Total barang ---
    print("-" * 30, "+")
    print(f"{'Jumlah item':<15} {total_barang:>10}")
    print(f"{'Total':<15} Rp {total:>10,}")

    if total > 1000000:
        diskon = total * 0.30
        bayar = total - diskon
        print(f"{'Diskon (30%)':<15} Rp {diskon:>10,.0f}")
        print(f"{'Bayar':<15} Rp {bayar:>10,.0f}")
    elif total > 200000:
        diskon = total * 0.15
        bayar = total - diskon
        print(f"{'Diskon (15%)':<15} Rp {diskon:>10,.0f}")
        print(f"{'Bayar':<15} Rp {bayar:>10,.0f}")
    elif total > 100000:
        diskon = total * 0.10
        bayar = total - diskon
        print(f"{'Diskon (10%)':<15} Rp {diskon:>10,.0f}")
        print(f"{'Bayar':<15} Rp {bayar:>10,.0f}")
    else:
        print(f"{'Bayar':<15} Rp {total:>10,}")

def cetak_struk():
    if not kasir:
        print("tidak ada barang yang dibeli.")
        return
    print("\n=== STRUK ===")
    hitung_total()

# --- Jalankan ----
tambah_barang()
cetak_struk()