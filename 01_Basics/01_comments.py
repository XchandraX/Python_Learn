# ini adalah komentar satu baris untuk menjelaskan kode di bawahnya
harga = 10000

"""
Ini adalah contoh komentar
lebih dari satu baris (Multi-line)
"""

def hitung_pajak(pendapatan: float) -> float:
    """
    Menghitung jumlah pajak tahunan sebesar 10%.

    Args:
        pendapatan (float): Total pendapatan kotor dalam setahun.

    Returns:
        float: Nominal pajak yang harus dibayar.
    """
    return pendapatan * 0.10

# Docstring bisa dipanggil atau dibaca oleh program menggunakan atribut __doc__
print(hitung_pajak.__doc__)
print(hitung_pajak(50))

# Atau menggunakan fungsi bawaan help() untuk melihat dokumentasi rapi
# help(hitung_pajak)