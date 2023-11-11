# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#Insert Items (without replacing any item)
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#Extend List
thislist = ["apple", "banana", "cherry"]
thislist.extend(["orange", "mango", "grapes"])
print(thislist)



#Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



#Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)



#Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


#Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  





