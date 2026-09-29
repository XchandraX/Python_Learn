# membandingkan apaakh dua variable menunjuk ke object yang sama
# di memori

"""
`is`: Mengembalikan `True` jika kedua variabel 
merujuk ke obejct memori yg sama

`is not`: Mengembalikan `True` jika kedua variabel tidak merujuk 
ke object memori yg sama
"""

a = [1, 2, 3]
b = [1, 2, 3]
c = a 

print(a == b)       # Output: True (nilainya sama)
print(a is b)       # Output: False (object di memorinya berbeda)
print(a is c)       # Output: True (merujuk ke object memori yg sama)
print(a is not b)   # Output: True (merujuk ke oject memori yg berbeda)

