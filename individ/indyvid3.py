"""
Определить среди всех двузначных чисел те, которые делятся на сумму своих цифр.
"""
if __name__ == '__main__':
    n = int(10)
    while n < 100:
        summ = (n // 10) + (n % 10)
        if n % summ == 0:
            print(n)
        n = n + 1