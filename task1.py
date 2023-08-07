# Ссылка на github
#https://github.com/s-getmanov/st_python11.git

#В принципе можно использовать готовую функцию из модуля math, но мы напишем свою. 
def factorial(n):
    # Проверка на отрицательные числа
    if n < 0:
        return "Факториал не определен для отрицательных чисел"
    
    # Проверка на ноль
    if n == 0:
        return 1
    
    # Рекурсивное вычисление факториала
    result = n * factorial(n - 1)
    return result

n = int(input("Введите число:"))
factorials = []

for i in range(n,0,-1):
   factorials.append(factorial(i))

print(f"Получился такой список: {factorials}")


