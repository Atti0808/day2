# #
# # In Python, the == and is operators are used for comparison, and they have different purposes. Here's a detailed explanation of both:

# # == (Equality Operator)
# # Value Comparison: The == operator checks if the values of two objects are equal. It compares the data/content of the objects.
# # Flexible: Works with different types of objects as long as they are compatible for comparison.

# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a

# print(a == b)  # True, because the contents of the lists are the same
# print(a == c)  # True, because they are the same object
# print(5 == 5)  # True, because the values are the same
# print(5 == 5.0)  # True, because the values are considered equal
# print('hello' == 'hello')  # True, because the string values are the same



# # is (Identity Operator)
# # Identity Comparison: The is operator checks if two variables point to the same object in memory. It does not compare the values, but rather the identities of the objects.
# # Strict: Used to check if two references point to the same object.

# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a

# print(a is b)  # False, because a and b are different objects in memory
# print(a is c)  # True, because c is the same object as a
# print(5 is 5)  # True, because integers with the same value often reference the same object
# print(5 is 5.0)  # False, because they are different objects (integer vs float)
# print('hello' is 'hello')  # True, because string literals are interned and reference the same object



# # #Type Sensitivity: The == operator is type-sensitive in the sense that it will return False if the types are not compatible for comparison. However, if types are compatible (like int and float), it can still return True if the values are equal.
# # Identity Check: The is operator checks for object identity, not value equality.
# # Use Cases:
# # Use == when you need to compare values.
# # Use is when you need to check if two references point to the same object (e.g., when checking if a variable is None).
# # Here is a practical illustration in Python:

# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a

# print(a == b)  # True, because the contents of a and b are the same
# print(a is b)  # False, because a and b are different objects
# print(a == c)  # True, because a and c have the same contents
# print(a is c)  # True, because c is the same object as a

# # Checking for None
# x = None
# print(x is None)  # True, the recommended way to check for None
# print(x == None)  # Also works, but less preferred


# #List


# #In Python, a list is a collection of items that can be of different types. Lists are created using square brackets [] and can contain any number of elements. Here are various ways to create and manipulate lists in Python:


# #Empy list

# my_list = []

# #List with Values

# my_list = [1, 2, 3, 4, 5]
# my_list = ['apple', 'banana', 'cherry']
# my_list = [1, 'apple', 3.14, True]



# #adding elements to a list 

# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)  # Output: [1, 2, 3, 4]


# my_list = [1, 2, 3]
# my_list.insert(1, 'a')
# print(my_list)  # Output: [1, 'a', 2, 3]



# my_list = [1, 2, 3]
# my_list.extend([4, 5, 6])
# print(my_list)  # Output: [1, 2, 3, 4, 5, 6]



# my_list = ['a', 'b', 'c']
# print(my_list[0])  # Output: 'a'
# print(my_list[1])  # Output: 'b'



# my_list = ['a', 'b', 'c']
# print(my_list[-1])  # Output: 'c'
# print(my_list[-2])  # Output: 'b'

# my_list = [1, 2, 3]
# my_list[1] = 'a'
# print(my_list)  # Output: [1, 'a', 3]

# my_list = [1, 2, 3]
# my_list.pop()
# print(my_list)  # Output: [1, 2]
# my_list.pop(0)
# print(my_list)  # Output: [2]

# my_list = [1, 2, 3]
# del my_list[1]
# print(my_list)  # Output: [1, 3]

# my_list = [1, 2, 3]
# print(len(my_list))  # Output: 3

# my_list = [1, 2, 3]
# print(2 in my_list)  # Output: True
# print(4 in my_list)  # Output: False

# my_list = [1, 2, 3]
# for item in my_list:
#     print(item)
# # Output:
# # 1
# # 2
# # 3

# numbers = [1, 2, 3, 4, 5] #lost of integeres

# fruits = ['apple', 'banana', 'cherry'] # list of strings


# mixed = [1, 'apple', 3.14, True] #mixed data types

# #Let's say you have a list and you want to access its elements using a variable:

# # Define a list
# my_list = ['apple', 'banana', 'cherry', 'date']

# # Define a variable to hold the index
# index = 2

# # Access the element at the specified index
# value = my_list[index]

# print(value)  # Output: 'cherry'

# # Define a list
# my_list = ['apple', 'banana', 'cherry', 'date']

# # Access the first element
# index = 0
# print(my_list[index])  # Output: 'apple'

# # Access the second element
# index = 1
# print(my_list[index])  # Output: 'banana'

# # Access the last element using negative indexing
# index = -1
# print(my_list[index])  # Output: 'date'


# # Define a list
# my_list = ['apple', 'banana', 'cherry', 'date']

# # Define a function to get the element at a specified index
# def get_element_at_index(lst, idx):
#     return lst[idx]

# # Use a variable to specify the index
# index = 3
# value = get_element_at_index(my_list, index)

# print(value)  # Output: 'date'

# #To access the value of a list element using a variable:

# # Define the list.
# # Define a variable to hold the index.
# # Use the variable to access the element.
# # This method allows you to dynamically access elements of a list based on variable values, which can be especially useful in loops and functions.