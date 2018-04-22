runningTotal = 0

for i in range(5):
    newNumber = int(input('Enter a number or a negative number to quit: '))
    runningTotal = runningTotal + newNumber
print()
print('The runningTotal is: ', runningTotal)

