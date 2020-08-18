class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [list() for i in range(1000)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.map[self.customHashFunction(key)].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.map[self.customHashFunction(key)].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.map[self.customHashFunction(key)]

    def customHashFunction(self, x):
        return x % 1000

#
