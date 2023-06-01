from random import randint
def ferma(n):
    k=True
    if n==4:
        return False
    elif n==2 or n==3 or n==5:
        return True
    for i in range(5):
        a=randint(2,n-1)
    
        if (a**(n-1))%n!=1:
            k=False
            break
    else:
        False
    return k
        
l=[]
for i in range(2,2000):
    if ferma(i):
        l.append(i)

l1=[]
for i in range(2,2000):
    if ferma(i):
        l1.append(i)



print('There is wrong number:')
for i in l:
    if i not in l1:
        print(i, end=' ')
        
for i in l1:
    if i not in l:
        print(i, end=' ')
print('')
print("Результаты бывают разными, чем большее количество раз мы меняем наше число а, тем вероятнее, что не произойдет ошибка. Тест Ферма хорош своей скоростью, но он не является необходимым условием простоты. Например есть псевдопростые числа, и если а взаимно просто с n во всех случаях, то тест Ферма выведет, что они просты, когда это не так")
