#Write a program that reads in a text file and outputs the number of e's it contains. 
#Author: Megan Tully

#Opens the .txt file called "moby-dick" 
file = open("moby-dick.txt","r")
Counter = 0
  
#Reading from file
Content = file.read()

#For loop that adds 1 to the counter for every e found in file
for char in Content:
    if char == 'e':
        Counter += 1
        

print("The number of e's in this file are: ",Counter)