f1 = open("demo.txt")
#f1 = open("demo.txt", "rb")# Open has 2 arguments. Another is mode(reads in binary form)
#f1 = open("demo.txt", "rt")
#content = f1.read(3)# Reads first 3 characters
#print(content)
#content = f1.read(3)# Reads next 3
#print(content)
# content = f1.read(355)# Dumps all the characters
# print("1", content)
# content = f1.read(3)# nothing to dump there for ingores
# print("2", content)

# content = f1.read()# By default read() function reads all charcters.
# for i in content:# Print character by charcter
#     print(i)
# f1.close()

# for i in f1:
#     #print(i)# By default there is new line character in demo.txt file
#     print(i, end="")

# Print line by line
# print(f1.readline())# New line \n already present in file
# print(f1.readline())

# Print using list
print(f1.readlines())