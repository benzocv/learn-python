x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#use the global keyword, the variable belongs to the global scope
def myfunc2():
    global x 
    x = "very good"
    print("Python is " + x)
myfunc2()