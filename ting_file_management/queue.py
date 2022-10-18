class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return self.size()

    def size(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.size() != 0:
            return self._data.pop(0)
        else:
            return None

    def search(self, index):
        if index < 0 or index > (self.size() - 1):
            raise IndexError("Index Inválido")
        if self.size() == 0:
            return None
        else:
            return self._data[index]
