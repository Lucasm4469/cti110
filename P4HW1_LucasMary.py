# Distance = speed * travel

vehiclespeed = int(input('What is the speed of the vehicle:' ))
hourstraveled = int(input('How many hours has it traveled?:'))

print()

print('hour', '\tdistance traveled' )
for hour in range(1, hourstraveled + 1 ):
    distancetraveled = vehiclespeed * hour
    print(hour, '\t', distancetraveled )
