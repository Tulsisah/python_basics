# A program that calculates the factorial of a number
h = int(input("\nEnter a number: "))

fact = 1
for i in range(1, h + 1):
    fact = fact * i

print("Factorial of", h, "is", fact)
