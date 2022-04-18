myfile = open("files/fruits.txt")
#print(myfile.read())

content = myfile.read()
myfile.close()

# This is better
with open("files/fruits.txt") as myfile:
    content = myfile.read()
    # with context manager closes the file automatically


print(content)

# Create new file
with open("files/vegetables.txt", "w") as myfile2:
    myfile2.write("Tomato\nCucumber\nOnion\n")
    myfile2.write("Garlic\n") 


# Append
with open("files/fruits.txt", "a+") as myfile3:
    myfile3.write("Okra\n")
    myfile3.seek(0)
    content3 = myfile3.read()

print(content3)