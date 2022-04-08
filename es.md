# Task07: Write a program that reads in a text file and outputs the number of e's it contains
## Author: Megan Tully

## Step One: Read in Moby Dick File
Using the open() function the file "moby-dick.txt" was opened for reading "r". This function was given the variable name "file".

## Step Two : Read the amount of e's in the file
A variable called "Counter" was created and assigned the value 0. Then a function .read was used to read all the contents of the file and was assigned a variable name "Content". Next a for loop was created that states for all characters written as char in the file, if they are equal the character "e" add 1 to the Counter for each of them. The number of e's in the file was then printed.