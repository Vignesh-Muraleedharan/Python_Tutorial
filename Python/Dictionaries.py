customer ={
    "name" : "Jane Doe",
    "age" : 30,
    "is_verified" : True
}
print(customer["name"])
print(customer.get("birthdate","Jan 1 1980"))
customer["name"] = "John Smith"
print(customer["name"])
customer["birthdate"] = "Jan 1 1980"    
print(customer["birthdate"])
print(customer)

# Exercise
phone = input("Phone: ")
digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch,"!") + " "
print(output)
