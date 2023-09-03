names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[-2])
print(names[0:])
print(names[3:-1])
print(names[:4])
names[0]="Vignesh"
print(names)


#Exercise
numbers = [3, 6, 2, 8, 4, 10]
small_num = numbers[0]
for i in numbers:
    if small_num > i:
        small_num = i
print(f"The smallest number in the list is {small_num}")