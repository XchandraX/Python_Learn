# Memiliki banyak metode (built-in methods) siap pakai untuk memproses string

s = " Helo Python "

# Method .upper()
# Mengubah seluruh teks ke huruf kapital
print(s.upper())                        # Output: " HELLO PYTHON "

# method .lower()
# Mengubah seluruh teks ke huruf kecil
print(s.lower())                        # Output: " hello python "

# Method .strip()
# Menghapus spasi di awal dan akhir string
print(s.strip())                        # Output: "Hello Python"

# Method .replace(old,new)
# Mengganti substring tertentu dengan teks baru
print(s.replace("Python", "World"))     # Output: " Hello World "

# Method .split(sep)
# Memecah string menjadi List berdasarkan pemisah
print("a,b,c".split(","))               # Output: ['a', 'b', 'c']

# Method sep.join(list)
# Menggabungkan elemen List menjadi satu String
print("-".join(['a', 'b', 'c']))        # Output: a-b-c

# Method .find(sub)
# Mencari posisi indeks pertama dari substring
print("Python".find("th"))              # Output: 2