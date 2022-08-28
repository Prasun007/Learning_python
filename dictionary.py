d1 = {"Prasun":"Coding",
      "Rohan":"Chicken",
      "Rohit":"Paytm",
      "Subham": "SST",
      "Numbers": {1:"One", 2:"Two", 3:"Three"}}
d1["Rina"] = "Cooking"# Updating Dictionary
d1["Ankita"] = "Photos and Videos"
print(d1["Numbers"][2])# Accessing the elements.
#del d1["Subham"] Deleting elements.
d2 = d1
del d2["Prasun"]

print(d1.get("Ankita"))# Gets the value of required key
d1.update({"Harry": "Learning"})# Updating using .update() function.
print(d1["Harry"])
print(d1)
print(d1.keys())# Shows all keys
print(d1.items())#Shows all items