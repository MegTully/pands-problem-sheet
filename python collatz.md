# Task04: Python Collatz

## Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
## Have the program end if the current value is one.

## Author: Megan Tully

## Step One: Get user to input a sentence
The input() function was used to ask the user to "Enter a positive integer: ". The input was assigned the variable name number. The input function was put inside an int() function, this ensures the input the user enters is an integer so that if the user doesn't enter a number they will recieve an error.

## Step Two: Create a loop
A while loop was created to keep the program repeating while the value of the variable number is greater than or equal to one. Within the while loop first there is a print() function that prints out every number on the same line separated by a space, using end" ",that is input into the loop at the beginning of each iteration. Then there are three statements. 

The first statement is an if statement that tells the program to divide the number by two if it is even. To determine if the number is even or not, the fact that all even numbers when divided by two have no remainder was used. The number modulo, denoted by "%", two should equal zero. If this condition is true the statement says to divide the number by two. If the condition is false the second statement is run which is an elif statement. This statement checks if the number is equal to one and if it is the break statement is run which terminates the loop. If the number is not equal to one the the last statement is run which is the else statement. This statement says that all other numbers which must be odd and not equal to one should be multiplied by three and then add on one. This new value will be assigned to the variable number.