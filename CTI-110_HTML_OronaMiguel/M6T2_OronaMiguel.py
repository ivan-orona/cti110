#Converting an amount of feet to inches
#November 19, 2017
#CTI-110 M6T2_FeetToInches
#Miguel Orona
#The program will convert feet to inches.

#The user will input and feet will be defined
def main():
    feet = int(input('Enter a number of feet: '))
    print(feet, 'equals', feet_to_inches(feet),'inches.')

#the conversion will be returned.
def feet_to_inches (feet):
    return feet * 12

main()
#End program.
