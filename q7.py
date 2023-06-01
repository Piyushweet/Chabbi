'''Calculate the factorial of a number using lambda function.'''

'''The lambda function factorial calculates the factorial of a 
number recursively by multiplying the number with the factorial 
of its predecessor until reaching 0.'''

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

number = int(input("Enter the number: "))
result = factorial(number)

print("Factorial of", number, "is:", result)