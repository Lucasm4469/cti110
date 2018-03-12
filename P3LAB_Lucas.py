# CTI-10
# P3TLAB - DEBUGGING
# LUCAS, MARY
# 12 MARCH 2018


def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    # TO DO: define the rest of the scores

    score = int(input('Enter grade: '))

    if score >= 90:
            print('Your grade is: A')
    elif score > 80:
        print('Your grade is: B')
    elif score > 70:
        print('Your grade is: C')
    elif score > 60:
        print('Your grade is: D')
    elif score < 60:
        print('Your grade is: F')
        

main()
