#number and string concatenation
#easy
a = "hello my age is "
b = 20
print(a + str(b))


#using format
a = "hello my age is {}"
b = 20
print(a.format(b))

#using two data 
a = "hello my age is {} and my name is {}"
b = 20
c = "john"
print(a.format(b,c))


#using f string
a = "hello my age is {}"
b = 20
print(f"hello my age is {b}")


#how to use double quote in string
a = "hello my age is \"20\""
print(a)

#escape character list
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value
a = "hello my age is \n20"
print(a)

