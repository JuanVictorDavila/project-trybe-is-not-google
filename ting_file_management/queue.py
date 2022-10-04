class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return self.size()

    def size(self):
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.append(value)
        

    def dequeue(self):
        """Aqui irá sua implementação"""
        if self.size() != 0:
            return self._data.pop(0)
        else:
            return None

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index > (self.size() - 1):
            raise IndexError("Index Inválido")
        if self.size() == 0:
            return None
        else:
            return self._data[index]
