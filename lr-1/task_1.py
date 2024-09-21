
"""
Думанський Владлен
ІПЗ-22011 бск
ЛР-1

1. Пошук простих чисел за діапазоном
"""
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    # я перевіряю всі можливі дільники до квадратного кореня н включно

def find_primes_in_range(a, b):
    return [n for n in range(min(a, b), max(a, b) + 1) if is_prime(n)]

def main():
    try:
        a = int(input("Введіть ціле натуральне число (a): "))
        b = int(input("Введіть ціле натуральне число (b): "))

        primes = find_primes_in_range(a, b)
        print(f"Прості числа між {a} і {b}: {', '.join(map(str, primes))}" if primes else f"Між {a} і {b} немає простих чисел.")
    except ValueError:
        print("Будь ласка, введіть коректні цілі числа.")

if __name__ == "__main__":
    main()
