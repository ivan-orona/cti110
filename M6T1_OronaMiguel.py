#Miguel Orona
#CTI 110
#M6T1 Kilometer Converter
#November 18, 2017
#The program will change an input of kilometers to miles

#The conversion factor is defined
Conversion_Factor = 0.6214

#kilometers will be defined to simplify the equation.
def main():
    kilometers = float(input('Please enter a distance in kilometers: '))
    show_miles (kilometers)
    
#miles will be defined to simply the equation.
def show_miles(km):
    miles = km * Conversion_Factor

    print(km, 'kilometers equals', miles, 'miles.')

main()

#end program
