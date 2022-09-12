#f = open("demo_2.txt", "w")# open has two arguments first is name of file 2nd is mode(Here mode is write)
#f = open("demo_2.txt", "a")# opening file in append mode jotobar run korum apend korbo "Prasun ....
#a = f.write("Prasun is a sane\n")# Jotobar program run korum totobar demo_2.txt ta khali koira "Prasun....." ida print hoibo
#print(a) a returns the number of characters in the file.

# Read write both
f1 = open("demo_2.txt", "r+")
print(f1.read())
f1.write(" or not")

f1.close()