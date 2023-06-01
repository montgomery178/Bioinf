def gcd(a:int, b:int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

l = [[93, 53, 4, -7, 1], [612, 342, -5, 9, 18], [1877, 1032, 149, -271, 1], [161, 28, -1, 6, 8], [616, 364, 3, -5, 28]]

print("Проверим алгоритм Евклида. Совершим ошибку в 4 примере массива, чтобы посмотреть на вывод")
print('')
for i in range(len(l)):
    if l[i][-1] == gcd(l[i][0], l[i][1]):
        print(f"Correct: {gcd(l[i][0], l[i][1])}")
    else:
        print(f"Incorrect: Must be: {l[i][-1]}, our result: {gcd(l[i][0], l[i][1])}")

        
        
#"Mypy выводит:Success: no issues found in 1 source file. Это означает, что программа прошла без ошибок как и должно было быть. Теперь сделаем ошибку



def gcd(a:int, b:int) -> bool:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

l = [[93, 53, 4, -7, 1], [612, 342, -5, 9, 18], [1877, 1032, 149, -271, 1], [161, 28, -1, 6, 8], [616, 364, 3, -5, 28]]


print("Проверим алгоритм Евклида. Совершим ошибку в 4 примере массива, чтобы посмотреть на вывод")
print('')
for i in range(len(l)):
    if l[i][-1] == gcd(l[i][0], l[i][1]):
        print(f"Correct: {gcd(l[i][0], l[i][1])}")
    else:
        print(f"Incorrect: Must be: {l[i][-1]}, our result: {gcd(l[i][0], l[i][1])}")
     

        
# Mypy выводит:program1.py:3: error: Incompatible return value type (got "int", expected "bool")  [return-value]
# Found 1 error in 1 file (checked 1 source file). Это значит, что он нашел ошибку
      
    
def gcd(a:int, b:float) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

l = [[93, 53, 4, -7, 1], [612, 342, -5, 9, 18], [1877, 1032, 149, -271, 1], [161, 28, -1, 6, 8], [616, 364, 3, -5, 28]]

print("Проверим алгоритм Евклида. Совершим ошибку в 4 примере массива, чтобы посмотреть на вывод")
print('')
for i in range(len(l)):
    if l[i][-1] == gcd(l[i][0], l[i][1]):
        print(f"Correct: {gcd(l[i][0], l[i][1])}")
    else:
        print(f"Incorrect: Must be: {l[i][-1]}, our result: {gcd(l[i][0], l[i][1])}")

        
# Mypy выводит:program1.py:5: error: Argument 1 to "gcd" has incompatible type "float"; expected "int"  [arg-type]
# Found 1 error in 1 file (checked 1 source file). Таким образом мы видим, что он снова заметил ошибку
 
      
      
      
      
      
      
      
      
