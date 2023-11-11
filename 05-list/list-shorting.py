
# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# Sort List Numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)



# Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


#Reverse Order
thislist = ["apple", "banana", "cherry"]
thislist.reverse()


#Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Another way to make a copy is to use the built-in method list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)



#Join Two Lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)




