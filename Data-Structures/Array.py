class Array:

    def __init__(self, initialSize):
        self._a = [None] * initialSize
        self._nitems = 0

    def insert(self, item):
        self._a[self._nitems] = item
        self._nitems += 1

    def search(self, item):
        for i in range(self._nitems):
            if self._a[i] == item:
                print(f"{self._a[i]} is found at location {i}")
                return self._a[i]
        return None

    def delete(self, item):
        for j in range(self._nitems):
            if self._a[j] == item:
                for k in range(j, self._nitems):
                    self._a[k] = self._a[k + 1]
                self._nitems -= 1

    def traverse(self):
        for j in range(self._nitems):
            return self._a[j]


result = Array(5)
result.insert(1)
result.insert(2)
result.insert(3)
print(result.search(2))
