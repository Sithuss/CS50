class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return f"🍪" * self.size


    def deposit(self, n):
        if not n:
            raise ValueError("invalid input")
        if n < 0:
            raise ValueError("Invalid input")
        if n > self.capacity:
            raise ValueError("Jar exceeded limited amount")
        if n > n + self.size:
            raise ValueError("cookie exceeded limited amount")
        self.size = self.size + n



    def withdraw(self, n):
        if not n:
            raise ValueError("Invalid input")
        if n < 0:
            raise ValueError("Invalid input")
        if n > self.size:
            raise ValueError("amount exceeded")
        self.size = self.size - n


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity Error")
        self._capacity = capacity

    @property
    def size(self):
        return self._size 

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Jar exceeded limited amount")
        self._size = size
