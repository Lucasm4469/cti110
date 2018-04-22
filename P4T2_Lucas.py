# Bug Accumulation.
total = 0

# Get the bugs collected for each day.
for day in range(1, 8):
    print('Enter the bugs collected on the day', day)
    bugs = int(input())
    total = total + bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')
