# Implementasi Binary Tree
"""
  Kita menggunakan pendekatan berbasis `Class` yang mirip dengan Linked List. 
Bedanya, jika Linked List menggunakaan penunjuk `next`, Binary Tree menggunakan penunjuk `left` dan `right`.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None    # Pointer ke anak kiri
        self.right = None   # Pointer ke anak kanan

# Membuat Root
root = Node("Direktur Utama")

# Menambahkan anak tingkat 1
root.left = Node("Manajer IT")
root.right = Node("Manajer HRD")

# Menambahkan cucu tingkat 2 (Anak dari Manajer It)
root.left.left = Node("Staf IT 1")
root.left.right = Node("Staf IT 2")

# Sekarang strukturnya menjadi:
#               [Direktur Utama]
#               /               \
#           [Manajer IT]     [Manajer HRD]
#           /         \
#   [Staf IT 1]     [Staf IT 2]



# Cara Menelusuri Binary Tree
"""
Karena strukturnya tidak linier, kita tidak bisa sekadar menggunakan perulangan `for` biasa.
Kita menggunakan konsep Rekursi (fungsi yang memanggil dirinya sendiri) untuk menelusuri setiap cabang.

Salah satu metode yang populer adlaah In-order Traversal (Kiri-> Induk -> Kanan)
"""


def telusuri_in_order(node):
    if node is not None:
        # Kunjungi seluruh cabang kiri terlebih dahulu
        telusuri_in_order(node.left)

        # Cetak data dari node saa tini
        print(node.data)

        # Terakhir, kunjungi cabang kanan
        telusuri_in_order(node.right)

print("Hasil Penelusuran In-order:")
telusuri_in_order(root)

# Ouptut:
# Staf IT 1
# Manajer IT
# Staf IT 2
# Direktur Utama
# Manajer HRD