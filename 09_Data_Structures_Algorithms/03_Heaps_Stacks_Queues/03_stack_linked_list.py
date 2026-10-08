class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StactLinkedList:
    def __init__(self):
        self.top = None # Pointer menunuk ke elemen teratas (Head)

    def push(self, data):
        node_baru = Node(data)
        # Jadikan elemen teratas saat ini sebagai 'next' dari node baru
        node_baru.next = self.top
        # Pindahkan pointer top ke node baru
        self.top = node_baru
        print(f"Push: {data}")

    def pop(self):
        if self.is_empty():
            return "Stack kosong!"

        # Simpan data dari elemen teratas untuk dikembalikan
        data_diambil = self.top.data
        # Geser pionter to ke elemen di bawahnya
        self.top = self.top.next
        return data_diambil

    def peek(self):
        if self.is_empty():
            return "Stack kosong!"
        return self.top.data

    def is_empty(self):
        return self.top is None

# --- Cara Penggunaan ---
stack_ll = StactLinkedList
stack_ll.push(10)
stack_ll.push(20)
stack_ll.push(30)

print(f"Elemen teratas (Peek): {stack_ll.peek()}")
print(f"Diambil (Pop): {stack_ll.pop()}")
print(f"Diambil (Pop): {stack_ll.pop()}")
print(f"Diambil (Pop): {stack_ll.pop()}")