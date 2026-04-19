n = int(input("Введите размер массива n: "))
A = []
for _ in range(n):
    A.append(int(input()))
i = 0
sum = 0
while i < n:
    sum = sum + A[i]
    i = i + 1
avg = sum / n
print("Среднее значение:", avg)
