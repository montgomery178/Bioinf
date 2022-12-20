import itertools

class Fib:
    """По объектам этого класса можно итерироваться и получать 300 Фибоначчи (сколько угодно на самом деле)"""

    class _Fib_iter:
        """Внутренний класс — итератор"""

        def __init__(self):
            self.i = 1
            self.fib1 = 1
            self.fib2 = 0

        def __next__(self):
            if self.i == 1:
                self.i += 1
                return 1
            else:
                m = self.fib1 + self.fib2
                self.fib1, self.fib2 = self.fib2, m
                self.i += 1
                return self.fib1 + self.fib2

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib._Fib_iter()


fib = Fib()
num = int(input()) # Принимает количество чисел которые мы хотим вывести, хотя можно обойтись и без этого и заранее написать количество в цикле ниже
# Просто for — работает!
for i, f in zip(
        itertools.count(1),
        itertools.islice(fib,num)
):
    print(i, f)
