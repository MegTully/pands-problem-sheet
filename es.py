#Question : Write a program that reads in a text file and outputs the number of e's it contains.
#Think about what is being asked here, document any assumptions you are making.
#The program should take the filename from an argument on the command line. I have not shown you how 
#to do this, you need to look it up.


#import sys

#filename= sys.argv[1]

#text = "moby-dick.txt"

#with open(filename, "rt") as f:
    #read_data = f.readlines()

#print(read_data)

#open txt file and read and count number e (char= '')

#use open() method to open and read file, must be in same foulder
#file = open("moby-dick.txt", "r")

#ecounter
#ecount = 0

#while true: while there is stuff in the file to go through
#while True:
   
    #read all char and store
   # char = file.read(1)
   
    #find e and add to counter
  #  if char == 'e':
 #       ecount += 1
    #break end loop
#    if not char:
#        break
   
#output  
#print("Number of e's is: ", ecount)

#Opening a file
file = open("gistfile1.txt","r")
Counter = 0
  
# Reading from file
Content = file.read()
CoList = Content.split("\n")
  
for i in CoList:
    if i:
        Counter += 1
          
print("This is the number of lines in the file")
print(Counter)