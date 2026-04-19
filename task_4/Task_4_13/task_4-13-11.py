n = int(input("Введите размер массива n: "))
A = []
print("Введите элементы массива:")
for _ in range(n):
    A.append(int(input()))

i = 0
sum = 0
count = 0

while i < n:
    if i % 2 == 0:
        sum = sum + A[i]  
        count = count + 1  
    i = i + 1  

if count > 0:  
    avg = sum / count
else:
    avg = 0 

print("Среднее арифметическое элементов с чётными индексами:", avg)