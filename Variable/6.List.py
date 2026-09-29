"""
List: Kumpulan data terurut (ordered), nilainya bisa diubah(mutable),
dan mengizinkan adanya elemen duplikat. 

Didefinisikan menggunakan kurung siku [].
"""

# Membuat list
buah = ["apel", "pisang", "mangga"]

print(buah)         # Output: ['apel', 'pisang', 'mangaa']

# Memodifikasi dan menambah elemen
buah[0] = "jeruk"       # Mengubah 'apel' menjadi 'jeruk'
buah.append("anggur")   # Menambah elemen di akhir list

print(buah)         # Output: ['jeruk', 'pisang', 'mangaa', 'anggur']
print(type(buah))   # Output: <class 'list'>