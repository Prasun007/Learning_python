mystr_1 = "Prasun is a good boy"
print(len(mystr_1))
print(mystr_1[0:5])# initial(0) = including, final(5) = excluding
print(mystr_1[0:20])
print(mystr_1[0:19])
print(mystr_1[0:29])

mystr = "Prasun"
print(mystr[3:6])
print(mystr[0:6:2])
print(mystr[0:6:29])# Takes how mush is available ie only P
print(mystr[::-1])# Print in reverse
print(mystr_1[0:20:4])
print(mystr[-5:-2])
"""Note to self: Excluding er modhe jeda thakbo ui character ta aito na.(Positive er modhe ui character
er porer ta hoibo ar negative er modhe ui charcter er ager ta hoibo)"""
print(mystr_1[::-2])

mystr_3 = "Harryisagoodboy5"
print(mystr_3.isalnum())# True because contains no space and has neumeric value.
print(mystr_3.isalpha())# False because conatins neumeric value
mystr_4 = "harry is a good boy"
print(mystr_4.isalpha())# False becasue contains space.
print(mystr_4.endswith("boy"))# True because ends with boy.
print(mystr_4.count("y"))# Counts the given alphabet.
print(mystr_4.capitalize())# Makes first letter capital.
print(mystr_4.find("good"))# Searches the index of the given character.
print(mystr_4.replace("good", "bad"))# Replaces the given word with the required.
print(mystr_4.upper())# Makes everything upper(capital).
print(mystr_4.lower())# Makes everything lower(small).