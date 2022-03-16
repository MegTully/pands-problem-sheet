#This program calculates a person's bmi
#It takes in two integers, your weight in kg and height in cm 
#and uses the bmi formula to print out your bmi
# Author: Megan Tully

#Ask user to input weight as int assigned to variable Weight then do the same with Height
Weight = int(input("Enter weight(Kg): "))
Height = int(input("Enter height(cm): "))

bmi = Weight/((Height/100)**2) #Formula to calculate bmi[1]

print("The BMI is {:.2f} kg/m\N{SUPERSCRIPT TWO}".format(bmi)) #.2f sets bmi to 2 dec places[2]
#\N{SUPERSCRIPT TWO} prints m^2 [3]

#[1]Calculator.net/ fitness & health/ bmi calculator, https://www.calculator.net/bmi-calculator.html
#[2]w3schools, Python String Formatting, https://www.w3schools.com/python/python_string_formatting.asp
#[3]stackoverflow, author:jake77, https://stackoverflow.com/questions/8651361/how-do-you-print-superscript-in-python