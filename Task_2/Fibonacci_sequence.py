def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("Welcome to fibonacci series")
n = int(input("Enter the number of terms: "))

print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i), end=" ")