a = 3
b = 2
if a > b:
    print("a is greater than b")


# Elif 
a = 3
b = 3
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")


# Else
a = 2
b = 3
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")


# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

# And
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")


a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")


# Nested If
x = 41
y = 21
z = 10
if x > y:
    print("x is greater than y")
    if x > z:
        print("x is greater than z")
    else:
        print("x is less than z")
