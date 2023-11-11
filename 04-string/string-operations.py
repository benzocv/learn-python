a = "Hello"
print(a)


#Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)



#Strings are Arrays
a = "Hello, World!"
print(a[1])


#Looping Through a String
for x in "banana":
  print(x)

#String Length
a = "Hello, World!"
print(len(a))


#Check String
txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)


#Slicing
b = "Hello, World!"
print(b[2:5])



#Slice From the Start
b = "Hello, World!"
print(b[:5])


#Slice To the End
b = "Hello, World!"
print(b[2:])

# Negative Indexing Slice
b = "Hello, World!"
print(b[-5:-2])


#Upper Case
a = "Hello, World!"
print(a.upper())

#Lower Case
a = "Hello, World!"
print(a.lower())


#Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))


#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


#more ref
# https://www.w3schools.com/python/python_ref_string.asp



# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)


