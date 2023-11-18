f = open("demofile.txt", "r")
print(f.read())

# read some part only
f = open("demofile.txt", "r")
print(f.read(5))

# read line by line
f = open("demofile.txt", "r")
print(f.readline())


# Close Files
f.close()