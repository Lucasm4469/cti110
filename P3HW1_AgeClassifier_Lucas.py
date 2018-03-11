# CTI-110
# P3HW1 - Age Classifier
# Mary Ann Lucas
# 11 March 2018

userAge = int(input('Please enter your age: '))
              
if userAge <= 1:
    print('You are an infant' )
elif userAge < 13:
    print('You are a child' )
elif userAge < 20:
    print('You are a teenager' )
elif userAge > 20:
    print('You are an adult' )
              
