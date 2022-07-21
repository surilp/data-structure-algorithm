class Bitset:

    def __init__(self, size: int):
        self.bit = [0] * size
        self.ct = 0
        self.size = size
        self.fl = False

    def fix(self, idx: int) -> None:
        value = self.bit[idx] + self.fl
        if value in [0, 2]:
            self.bit[idx] = 1 - self.bit[idx]
            self.ct += 1

    def unfix(self, idx: int) -> None:
        value = self.bit[idx] + self.fl
        if value in [1]:
            self.bit[idx] = 1 - self.bit[idx]
            self.ct -= 1

    def flip(self) -> None:
        self.fl = not self.fl
        self.ct = self.size - self.ct

    def all(self) -> bool:
        return self.ct == self.size

    def one(self) -> bool:
        return self.ct >= 1

    def count(self) -> int:
        return self.ct

    def toString(self) -> str:
        result = ''
        for num in self.bit:
            num = num if not self.fl else 1 - num
            result += str(num)
        return result


b = Bitset(5)
b.fix(3)
b.fix(1)
b.flip()
print(b.all())
b.unfix(0)
b.flip()
print(b.one())
b.count()
print(b.toString())

b = Bitset(2)
b.flip()
