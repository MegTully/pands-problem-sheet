# Task03: Write a program that asks a user to input a string and outputs every second letter in reverse order 
## Author: Megan Tully

## Step One: Get user to input a sentence
The input() function was used to ask the user to "Enter a sentence: ". The input was assigned the variable name sentence. The input function was put inside a str() function, this converts the sentence the user enters into a string so that if the user enters numbers they will be converted from integers to strings so the program can run without error. 

## Step Two: Write the sentence backwards
String slicing was researched on the website The Real Python referenced in my code. The index position of the characters/letters in the string/sentence were repositioned starting with the last character and ending with the last i.e the sentence was written backwards. The code used to do this was "sentence[::-1]", the square brackets indicate the position/index of the characters in sentence and returns the characters in that order. The range can be specified inside the index by [start:end:step], "start" represents the start position, "end" represents the end position, leaving these blank indicates to start from the first character and end at the last. Since we can't predict the length of the sentence we leave them blank but if we want to start or end at a specific position we would input the positions. "step" represents the stride at which the characters are returned so -1 starts at the end of the string and returns every character moving backwards along the string. The variable "Backwards" was assigned to the backwards sentence.

## Step Three: Print out every second letter of the backwards sentence
Using the same slice syntax in the previous step every second letter was returned from the string "Backwards". The code used was "Backwards[0::2]", this returns a string that starts with the character at position 0, ends at the last character of the sentence "Backwards" and has a stride of 2 so returns every second character. The print() function prints out every second letter of the sentence the user enters backwards.
