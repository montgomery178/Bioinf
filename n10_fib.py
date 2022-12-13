import itertools

class Fib:    
    """По объектам этого класса можно итерироваться и получать 6 чисел Фибоначчи"""

    class _Fib_iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.i = 1
            l=[1,0]
            self.fibs = l
        
        def __next__(self):
            j = self.i
            self.fibs.append(self.fibs[-1]+self.fibs[-2])
            self.fibs=self.fibs[1:]
            self.i += 1
            return self.fibs[-1]            

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib._Fib_iter()
fib = Fib()

# Просто for — работает!
for i, f in zip(
    itertools.count(1),
    itertools.islice(fib, 300)
):
    print(i, f)
