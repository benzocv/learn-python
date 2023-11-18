f = open("demofile2.txt", "a")
f.write("\n\nNow the file has more content!")
f.close()

#  w - Write - will overwrite any existing content
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()