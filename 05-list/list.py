#basic list
a = ['apple','banana','orange']
print(a)

#list allow duplicate
a = ['apple','banana','orange','apple']
print(a)

#list allow different data type
a = ['apple','banana','orange',1]
print(a)

#get list length
a = ['apple','banana','orange',1]
print(len(a))

#create  list using list constructor
a = list(('apple','banana','orange',1))
print(a)


#Access Items
this_list = ["apple", "banana", "cherry"]
print(this_list[0])


#Negative Indexing
this_list = ["apple", "banana", "cherry"]
print(this_list[-1])

# Range of Indexes
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])

#range from start
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[:4])

#range to end
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:])

#range negative
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[-4:-1])

#check item exist
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in this_list:
  print("Yes, 'apple' is in the fruits list")