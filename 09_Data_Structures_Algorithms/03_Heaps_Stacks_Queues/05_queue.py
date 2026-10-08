from collections import deque

class Queue:
    def __init__(self):
        # Membuat wadah deque kosong
        self.antrean = deque()

    def enqueue(self, data):
        # Menambahkan data ke posisi saling kanan (belakang)
        self.antrean.append(data)
        print(f"Masuk antrean: {data}")

    def dequeue(self):
        # Menghapus dan mengambil data dari ujung paling kiri (depan)
        if self.is_empty():
            return "Antrean kosong!!"
        return self.antrean.popleft()

    def front(self):
        # Melihat elemen terdeapn (indeks 0) tanpa menghapus datanya
        if self.is_empty():
            return "Antrean kosong!!"
        return self.antrean[0]

    def is_empty(self):
        return len(self.antrean) == 0


# --- Cara Pengguna ---
pelanggan = Queue()

# 3 pelanggan masuk ke dalam antrean
pelanggan.enqueue("Andi")
pelanggan.enqueue("Budi")
pelanggan.enqueue("Siti")

print(f"\nGiliran saat ini (Front): {pelanggan.front()}")   # Output: Andi
print(f"Selesai dilayani (Dequeue): {pelanggan.dequeue()}") # Output: Andi
print(f"Selesai dilayani (Dequeue): {pelanggan.dequeue()}") # Output: Budi

# Mengecek sisa antrean
print(f"Giliran selanjutnya: {pelanggan.front()}")          # Output: Siti