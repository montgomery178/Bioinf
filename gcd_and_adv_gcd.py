def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def adv_gcd(a,b):
    if b==0:
        return 1,0,a
    x,y,d=adv_gcd(b,a%b)
    return y, x-(a//b)*y, d
    

l=[[93,53,4,-7,1],[612,342,-5,9,18],[1877,1032,149,-271,1], [161,28,-1,6,8],[616,364,3,-5,28]]

print("Проверим алгоритм Евклида. Совершим ошибку в 4 примере массива, чтобы посмотреть на вывод")
print('')
for i in range(len(l)):
    if l[i][-1]==gcd(l[i][0],l[i][1]):
        print(f"Correct: {gcd(l[i][0],l[i][1])}")
    else:
        print(f"Incorrect: Must be: {l[i][-1]}, our result: {gcd(l[i][0],l[i][1])}") 

print('')        
print("Проверим алгоритм расширенный алгоритм Евклида")        
for i in range(len(l)):
    x,y,d=adv_gcd(l[i][0],l[i][1])
    
    if l[i][2]==x and l[i][3]==y and l[i][4]==d:
        print(f"Correct: {adv_gcd(l[i][0],l[i][1])}")
    else:
        print(f"Incorrect: Must be: {l[i][2:]}, our result: {adv_gcd(l[i][0],l[i][1])}")
