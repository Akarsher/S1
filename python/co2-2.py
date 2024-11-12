#2.	Generate Fibonacci series of N terms
n = int(input("Enter the number of terms: "))

a, b = 0, 1
fibonacci_series = []
for i in range(n):
    fibonacci_series.append(a)
    a, b = b, a + b

print(f"Fibonacci series of {n} terms: {fibonacci_series}")
