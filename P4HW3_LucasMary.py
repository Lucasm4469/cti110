# Display the factorial for a non-negative integer.

userInteger = int(input('Please enter a number: '))
while userInteger <1:
    userInteger = int(input('Please enter a positive number please: '))

factorial = 1

for currentNumber in range(1, 5 ):
    factorial = factorial * currentNumber

    print()
    print('The factorial of', userInteger, 'is', factorial)
