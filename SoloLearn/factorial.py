def factorial(x):
    print(x)
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))

# 5! = 5 * 4 * 3 * 2 * 1

