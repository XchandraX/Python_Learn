class StackList:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        print(f"Push: {data}")

    def pop(self):
        if self.is_empty():
            return "Stack kosong!"
        return self.stack.pop()

    def peek(self):
        if self.if_empty():
            return "Stack kosong!"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

# --- Cara Penggunaan ---
tumpukan = StackList()
tumpukan.push("Buku A")
tumpukan.push("Buku B")
tumpukan.push("Buku C")

print(f"Elemen teratas (Peek): {tumpukan.peek()}")
print(f"Diambil (Pop): {tumpukan.pop()} ")
print(f"Diambil (Pop): {tumpukan.pop()} ")
print(f"Diambil (Pop): {tumpukan.pop()} ")