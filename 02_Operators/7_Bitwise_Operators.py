# Melakukan operasi pada angka dalam level biner (bit demi bit)

"""
& (AND)
| (OR)
^ (XOR)
~ (NOT)
<< (Left Shift)
>> (Right Shift)
"""

a = 6   # Biner: 0000 0110
b = 3   # Biner: 0000 0011

# Bitwise AND (&)
# Membandingkan bit per bit. Bernilai 1 jika KEDUA bit bernilai 1.
# 0110 | 0011 = 0010
print(a & b)    # Output: 2 (Biner: 0010)

# Bitwise OR (|)
# Membandingkan bit per bit. Bernilai 1 jika SALAH SATU bit bernilai 1.
# 0110 | 0011 = 0111
print(a | b)    # Output: 7 (Biner: 0111)

# Bitwise XOR (^)
# Membandingkan bit per bit. Bernilai 1 jika bit BERBEDA.
# 0110 ^ 0011 = 0101
print(a ^ b)    # Output: 5 (Biner: 0101)

# Bitwise NOT (~)
# Membalikkan seluruh bit (0 menjadi 1, 1 menjadi 0)
# Rumus: ~x = -(x + 1)
# ~6 = -(6 + 1) = -7
print(~a)    # Output: 7 (Biner: -0000 0111)
# ~3 = -(3 + 1) = -4
print(~b)    # Output: 4 (Biner: -0000 0100)

# Left Shift (<<)
# Menggeser bit 'a' ke kiri sebanyak 'b' posisi (sama dengan a * (2**b))
# 6 << 3 = 6 * 8 = 48 (Biner: 0011 0000)
print(a << b)   # Output: 48 (Biner: 0011 0000)

# Right Shift (>>)
# Menggeser bit 'a' ke kanann sebanyak 'b' posisi (sama dengan a // (2**b))
# 0110 digeser ke kanan 3 kali menjadi 0000
print(a >> b)   # Output: 0 (Biner: 0000)