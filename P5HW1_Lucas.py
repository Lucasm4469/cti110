# This is a Test Average and Grades function.
# 22 April 2018
# CTI-110 P5T2_FeetToInches
# Mary Ann Lucas

def main():
    test1 = int(input('Enter test grade 1: '))
    test2 = int(input('Enter test grade 2: '))
    test3 = int(input('Enter test grade 3: '))
    test4 = int(input('Enter test grade 4: '))
    test5 = int(input('Enter test grade 5: '))
    average = calc_Average(test1 + test2 + test3 + test4 + test5)
    print ('Score: '+str(test1)+'  Grade:'+determine_Grade(test1))
    print ('Score: '+str(test2)+'  Grade:'+determine_Grade(test2))
    print ('Score: '+str(test3)+'  Grade:'+determine_Grade(test3))
    print ('Score: '+str(test4)+'  Grade:'+determine_Grade(test4))
    print ('Score: '+str(test5)+'  Grade:'+determine_Grade(test5))
    print('Your average score is', average)

def calc_Average(test):
    return test / 5

def determine_Grade(test):
    if test >= 90 and test <= 100:
        return 'A'
    elif test >= 80 and test <= 89:
        return 'B'
    elif test >= 70 and test <= 79:
        return 'C'
    elif test >= 60 and test <= 69:
        return 'D'
    else:
        return 'F'

main()
