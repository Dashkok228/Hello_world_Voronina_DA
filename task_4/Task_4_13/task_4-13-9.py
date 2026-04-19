n = int(input("Введите размер массива n: "))
A = []
for _ in range(n):
    A.append(int(input()))
i = 0
sum = 0
while i < n:
    print(f"Проверяем элемент {A[i]}, i = {i}")  
    if A[i] % 2 != 0:
        print(f"{A[i]} нечётный, добавляем к сумме")  
        sum = sum + A[i]
    else:
        print(f"{A[i]} чётный, пропускаем")  
    i = i + 1
print(f"Сумма нечётных элементов: {sum}")
