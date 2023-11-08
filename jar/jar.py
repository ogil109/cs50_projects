class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return "🍪" * int(self.size)


    def deposit(self, n):
        if n <= 0 or n + self.size > self.capacity:
            raise ValueError
        self.size += n


    def withdraw(self, n):
        if n <= 0 or n > self.size:
            raise ValueError
        self.size -= n


    # Getter for capacity
    @property
    def capacity(self):
        return self._capacity


    # Setter for capacity
    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError
        self._capacity = capacity


    # Getter for size
    @property
    def size(self):
        return self._size


    # Setter for size
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError
        self._size = size