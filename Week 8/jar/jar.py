class Jar:
    def __init__(self, capacity=12):
        if type(capacity) == int and capacity >= 0 :
            self._capacity = capacity
        else:
            raise ValueError
        self.cookies = 0

    def __str__(self):
        return "🍪"*self.cookies

    def deposit(self, n):
        if self.cookies + n > self._capacity:
            raise ValueError
        else:
            self.cookies = self.cookies + n

    def withdraw(self, n):
        if self.cookies - n < 0:
            raise ValueError
        else:
            self.cookies = self.cookies - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

def main():
    j = Jar()
    print(j)

if __name__ == "__main__":
    main()