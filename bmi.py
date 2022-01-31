#This program calculates a person's bmi
#It takes in two integers, your weight in kg and height in cm 
#and uses the bmi formula to print out your bmi
# Author: Megan Tully
 
Weight = int(input("Enter weight(Kg): "))
Height = int(input("Enter height(cm): "))
bmi = Weight/((Height/100)**2)

print("The BMI is {} kg/m\N{SUPERSCRIPT TWO}".format(bmi)) #reference \N{SUPERSCRIPT TWO}

#reference : stackoverflow.com