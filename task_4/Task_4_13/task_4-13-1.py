A = float(input("Введите число A: "))
B = float(input("Введите число B: "))
C = float(input("Введите число C: "))
D = float(input("Введите число D: "))

min = A
if B < min:
    min = B

if C < min:
    min = C

if D < min:
    min = D
    
print("Минимальное число:", min)