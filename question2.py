# #Create a dictionary with keys name, age, and city and print the dictionary

my_dict = {"name": "John", 
           "age": 30, 
           "city": "New York" ,
           "country" : "India" ,
           "state" : "japan",
           "ADDRESS" : "xcz"

           }
print(my_dict)

# #Access and print the value of key "name" from a dictionary.
print(my_dict["name"])

# #Find the length of a dictionary using len().
print(len(my_dict))

# #Check the data type of a dictionary using type().
print(type(my_dict))

# #Create a dictionary using the dict() constructor from a tuple of key-value pairs.
tuple1 = (("name", "Alice"), ("age", 25), ("city", "Los Angeles"))
print(type(tuple1))
new_dict = dict(tuple1)
print(new_dict)

# # Use the get() method to access a key that exists in the dictionary.
print(my_dict.get("age"))

#  # Add a new key "rollNo" with value 25 to an existing dictionary.
my_dict["rollNo"] = 25  
print(my_dict)
# Remove the key "address" from a dictionary using pop().
my_dict.pop("ADDRESS")
print(my_dict)

# #Clear all elements from a dictionary using the clear() method.
my_dict.clear()
print(my_dict)

# # Write an if statement to check whether a number is positive or negative.
num = -10
if num > 0:
    print("The number is positive.")    
else:
    print("The number is negative.")

# #Create a dictionary with duplicate keys and print the output. Explain the result.
dup_dict = {"name": "John", "age": 30, "name": "Alice"}
print(dup_dict)

# #Check whether a key "college" exists in a dictionary using in.
my_dict = {"name": "Mahesh", "age": 30, "city": "Mumbai"}   
print("college" in my_dict)

# Update the value of "city" in a dictionary using the update() method.
my_dict.update({"city": "Pune"})
print(my_dict)

#Copy one dictionary into another using the copy() method and prove both are independent.
dict1 = {"name": "Dhiraj", "age": 28}
dict2 = dict1.copy()
dict2["age"] = 29   
print(dict1) 
print(dict2)

# Remove the last inserted item from a dictionary using popitem().
dict1.popitem()
print(dict1)

#Write a program to print all keys and values using keys() and values().
my_dict1 = {"name": "Mahesh", "age": 30, "city": "Mumbai"}
print(my_dict1.keys())
print(my_dict1.values())

#Write an if–else program to check whether a number is even or odd.
num = 7
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#Write a program using elif to check whether a number is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")   
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#19. Write a nested if statement to check if a person is eligible to vote (gender = "female" and age ≥ 18).

gen = input("Enter The Gender :-")
age = int(input("Enter The Age :-"))
if gen == "female" and age >= 18:
        print("You are not eligible to vote.")
else:
            print("enter the correct gender.")


# Use a shortcut if–else to print "Pass" or "Fail" based on marks.

marks = int(input("Enter the marks: "))
result = "Pass" if marks >= 40 else "Fail"  
print(result)

# Create a dictionary and use a loop to print all key-value pairs using items().
dict3 = {"name": "Ravi", "age": 22, "city": "Chennai"}
for key, value in dict3.items():
    print(f"{key}: {value}")

#Write a program to check if a key exists in a dictionary and print an appropriate message.

my_dict2 = {"name": "Anita", "age": 27, "city": "Delhi"}
key_to_check = "age"
if key_to_check in my_dict2:
    print(f"The key '{key_to_check}' exists in the dictionary.")

# Create two dictionaries. Copy one into another using assignment (=) and show how changes affect both.
dict_a = {"name": "Sita", "age": 24}
dict_b = dict_a
dict_b["age"] = 25
print(dict_a)
print(dict_b)

# Write a program that takes a dictionary and prints only keys whose values are integers.
dict4 = {"name": "Rohan", "age": 29, "height": 5.9, "weight": 70, "city": "Bangalore"}
for key, value in dict4.items():
    if isinstance(value, int):
        print(f"{key}: {value}")

# Use setdefault() to insert a key "grade" if it does not exist.
my_dict5 = {"name": "Vikram", "age": 31}
my_dict5.setdefault("grade", "A")
print(my_dict5)

# Write a program using logical operators (and, or, not) inside an if condition.
# Write a program using pass inside an if statement.
num1 = 10
num2 = 20
if num1 > 5 and num2 < 30:
    print("Both conditions are true.")
    pass
if not (num1 < 5 or num2 > 30):
    print("Neither condition is true.")


# Write a match statement to display a message based on the day name (Monday, Tuesday, etc.)
day = input("Enter the day name: ")
match day:
    case "Monday" | "monday":
        print("It's Monday!")
    case "Tuesday":
        print("It's Tuesday")
    case "Wednesday":
        print("It's Wednesday")
    case _:
        print("It's some other day.")

# Use a match statement with multiple values in one case to categorize students.
grade = input("Enter the student's grade (A, B, C, D, F): ")
match grade:
    case "A" | "B":
        print("Excellent performance!")
    case "C":
        print("Good performance.")
    case "D":
        print("Needs improvement.")
    case "F":
        print("Failing grade.")
    case _:
        print("Invalid grade.")

# Write a match statement with an extra condition using if to check name and age.
person_name = input("Enter the name: ")
person_age = int(input("Enter the age: "))
match person_name:
    case person_name if person_age >= 18:
        print(f"{person_name} is an adult.")
    case person_name if person_age < 18:
        print(f"{person_name} is a minor.")
    case _:
        print("Unknown person or age.")



        


   
     












