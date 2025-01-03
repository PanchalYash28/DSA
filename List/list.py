# 1. Lists are ordered collection of data items
# 2. They store multiple items in a single variable
# 3. List items are separated by commas and enclosed within square brackets
# 4. Lists are changable meaning we can alter them after creation.


# Example 1
l = [10, 20, 30]
l1 = [20, 30, 40]

print(l)  # op: [10, 20, 30]
print(l1)  # op: [20, 30, 40]
print(type(l))  # op: <class 'list'>
l2 = ["Bhavesh", "Nitesh", "Ram"]
print(l2)  # op: ['Bhavesh', 'Nitesh', 'Ram']
l3 = [1, 2, "Bhavesh"]
print(l3)  # op: [1, 2, 'Bhavesh']

# Example 2
marks = [10, 20, 30]
print(marks)  # op: [10, 20, 30]
print(type(marks))  # op: <class 'list'>
print(marks[0])  # op: 10
print(marks[1])  # op: 20
print(marks[2])  # op: 30

# Example 3
marks = [10, 20, 30, "Bhavesh", False]
print(marks)  # op: [10, 20, 30, 'Bhavesh', False]
print(type(marks))  # op: <class 'list'>
print(marks[0])  # op: 10
print(marks[1])  # op: 20
print(marks[2])  # op: 30

# Example 4 - Negative Indexing
marks = [10, 20, 30, "Bhavesh", False]
print(marks[-3])  # op: 30
print(marks[len(marks)-3])  # op: 30
print(marks[5-3])  # op: 30
print(marks[2])  # op: 30

# Check Whether an Item is present in the list?
marks = [10, 20, 30, "Bhavesh", False]
if 30 in marks:
    print("Yes")  # op: Yes
else:
    print("No")

# Access the value
marks = [10, 20, 30, "Bhavesh", False]
print(marks)  # op: [10, 20, 30, 'Bhavesh', False]
print(marks[:])  # op: [10, 20, 30, 'Bhavesh', False]
print(marks[1:])  # op: [20, 30, 'Bhavesh', False]
print(marks[1:4])  # op: [20, 30, 'Bhavesh']
