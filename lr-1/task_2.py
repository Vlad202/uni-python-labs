
"""
Думанський Владлен
ІПЗ-22011 бск
ЛР-1

2. Фібоначчі
"""
def fib_helper(n, a=0, b=1):
    if n == 0:
        return []
    elif n == 1:
        return [a]
    return [a] + fib_helper(n - 1, b, a + b)

def fib(k):
    return fib_helper(k)

def main():
    try:
        k = int(input("Введіть кількість чисел Фібоначчі, які потрібно вивести: "))
        if k <= 0:
            print("Кількість чисел повинна бути додатною.")
        else:
            print(f"Перші {k} чисел Фібоначчі: {fib(k)}")
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")

if __name__ == "__main__":
    main()
