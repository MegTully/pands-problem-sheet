#This program reads in the moby-dick.txt file I created
filename = "moby-dick.txt"

with open(filename, "rt") as f:
    read_data = f.readlines()

print(read_data)
