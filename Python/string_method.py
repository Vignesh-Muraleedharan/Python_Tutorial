course = "Python's Course for Beginners"
print(len(course))#len() is a built-in function
#Function is general purpose and method is specific to a type
print(course.upper())#upper() is a method
print(course.lower())#lower() is a method
print(course.find('P'))#find() is a method, returns index of the first occurence of the character
print(course.find('o'))
print(course.find('O'))#Case sensitive
print(course.replace('Beginners', 'Absolute Beginners'))#replace() is a method 
print("Python" in course)#in is an operator that returns a boolean value
print("python" in course)#Returns False because of case sensitivity
#find returns index, in returns boolean
print(course.title())#title() is a method