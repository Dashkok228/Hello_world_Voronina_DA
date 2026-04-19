n = int(input("Введите размер массива n: "))
A = []
print("Введите элементы массива:")
for _ in range(n):
    A.append(int(input()))

i = 0
sum = 0

while i < n:
    if i % 2 != 0:
        sum = sum + A[i]
    i = i + 1

print("Сумма элементов с нечётными индексами:", sum)