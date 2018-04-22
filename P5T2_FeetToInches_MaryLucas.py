# The feet_to_inches program converts feet to inches.
# 22 April 2018
# CTI-110 P5T2_FeetToInches
# Mary Ann Lucas

# Constant for the number of inches per foot.

INCHES_PER_FOOT = 12

def main():
    feet = int(input('Enter a number of feet: '))

    print(feet, 'equals', feet_to_inches(feet), 'inches. ')

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
