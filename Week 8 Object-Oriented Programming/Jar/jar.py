class Jar:
    def __init__(self, capacity=12):
        self._size = 0
        if not self._is_positive_integer(capacity):
            raise ValueError("Capacity must be a positive integer")
        else:
            self._capacity = capacity

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not self._is_positive_integer(n):
            raise ValueError("Must deposit a positive integer amount of cookies")
        if self._size + n > self.capacity:
            raise ValueError("Exceed capacity")
        else:
            self._size += n

    def withdraw(self, n):
        if not self._is_positive_integer(n):
            raise ValueError("Must withdraw a positive integer amount of cookies")
        if self._size < n:
            raise ValueError("Not enough cookies")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not self._is_positive_integer(capacity):
            raise ValueError("Capacity must be a positive integer")
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not self._is_positive_integer(size):
            raise ValueError
        else:
            self._size = size

    # Helper function
    def _is_positive_integer(self, input):
        try:
            return (input.is_integer() and input >= 0)
        except Exception:
            return False
