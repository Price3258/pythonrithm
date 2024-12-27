def factorial(n):
    if n <= 2:
        return n
    return n * factorial(n - 1)


print(factorial(4))
print(factorial(2))
print(factorial(1))
print(factorial(5))