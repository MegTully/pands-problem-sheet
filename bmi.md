# Task 02: Write a program that calculates somebody's Body Mass Index (BMI)
## Author: Megan Tully

To calculate a person's BMI you need their weight in kg and height in metres.

## Step One : Get the user to input their height and weight
The input() function was used to ask the user to "Enter weight(kg): "  and then to 
"Enter height(cm): ". These inputs were assigned variable names Weight and Height respectively.
The input function is taking in a string but we need to convert this to an int to be able to 
input it into our maths formula, both input functions were put inside an int() function to do this.

## Step Two: Calculate BMI
The formula for BMI is weight in kg divided by height in metres squared. Therefore the variable 
Height was multiplied by 100 to covert from centimetres to metres and then squared. The variable Weight was then divided by this. The result was then assigned a variable name bmi.

## Step Three: Print BMI result to user
Using the print() function the users BMI was printed. The .format(bmi) function puts the bmi variable inside the parantheses within the message in the print function. The .2f code inside the parantheses converts the BMI result to 2 decimal places. The code \N{SUPERSCRIPT TWO} inside the print function prints out m^2.
