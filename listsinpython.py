computer_languages = ["python", "java", "javascript"]
serial = [3, 2, 1]# Numeric List
numbers = [2, 7, 9, 11, 3]
serial.sort()
serial.reverse()
print(serial)
print(computer_languages)
print("Required number are", numbers[1:4:2])
print(computer_languages[0:4:3])
print(numbers[-1:-5:-3])
print(max(numbers))# Prints the maximum number
print(min(numbers))# Prints the minimum number
numbers.append(7)#join at the end
computer_languages.append("github")
numbers.insert(1, 67)# Insert after first element.
numbers.remove(9)
numbers.pop()# Removes last element.
print(numbers)
print(computer_languages)
numbers[2] = 98# Replace list elements.
print(numbers)
tp = (1, 2, 3)# Creating tupple
#tp[2] = 5
tp1 = (1,)#Tupple of only one element.
print(tp)
print(tp1)


#Swapping two numbers
a = 7
b = 9
print(a, b)
"""temp = a
a = b
b = temp
print(a, b)"""
a, b = b, a
print(a, b)