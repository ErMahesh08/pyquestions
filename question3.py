#Write a function named hello() that prints Hello Python when called
def hello():
    print("Hello Python")
hello()

# Create a function welcome() and call it once.
def welcome():
    print("Welcome to Python programming!") 
welcome()

#Write a function print_name(name) that prints the name passed to it.
def print_name(name):
    print("Name:", name)   
print_name("mahesh")

#Create a function city(city_name) and call it with Nashik.
def city(city_name):
    print("City:", city_name)
city("Nashik")

# Write a function add(a, b) that prints the sum of two numbers.
# sum1 = int(input("Enter first number: "))
# sum2 = int(input("Enter second number: "))
# def add(a, b, c=2):
#     print("Sum:", a + b - c)   
# add(sum1, sum2)

# Create a function student(fname, lname) that prints full name.
def student(fname, lname):
    print("Full Name:", fname + " " + lname)
student("Alice", "Johnson") 

#Write a function marks(m1, m2, m3) that prints all three marks.
# Mark1 = int(input("Enter first mark: "))
# Mark2 = int(input("Enter second mark: "))
# Mark3 = int(input("Enter third mark: "))
# def marks(m1, m2, m3):
#     print("Marks:", m1, m2, m3)
# marks(Mark1, Mark2, Mark3)

# Write a function kids(names) that prints all kids names.
def kids(names):
    for name in names:
        print("Kid's Name:", name)
kids(["chetan", "mahesh", "sarry"])

# Print the first kid name using args.
def first_kid(*names):
    print("First Kid's Name:", names[0])
first_kid("chetan", "mahesh", "sarry")

# Write a function language(lang="Python") and call it with and without argument.
def language(lang="Python"):
    print("Language:", lang)
language()
language("Java")
language("C++")

# Write a function employee(id, name) and call it using keyword arguments.
EMPLOYE_NAME = input("Enter Employee Name :-")
EMPLOYE_ID = int(input("Enter Employee ID :-"))
def employee(id, name):
    print("Employee ID:", id)
    print("Employee Name:", name)
employee(name=EMPLOYE_NAME, id=EMPLOYE_ID)

# Call a function using arguments in different order.
employee(name="Ramesh", id=102)

#Write a function person(info) and print name and age.
def person(info):
    print("Name:", info["name"])
    print("Age:", info["age"])
person({"name": "John", "age": 28})
person({"age": 35, "name": "Dhiraj"})

#Access values from kwargs using keys.
def details(**kwargs):
    print("Name:", kwargs.get("name"))
    print("Age:", kwargs.get("age"))
details(name="Alice", age=30)
details(age=25, name="Bob")

# Write a function print_list(data) that prints each item of a list.
def print_list(data):
    for item in data:
        print("Item:", item)
print_list([1, 2, 3, 4, 5])
print_list(["apple", "banana", "cherry"])

# Pass a list of company names to a function.
def companies(names):
    for name in names:
        print("Company Name:", name)
companies(["Google", "Microsoft", "Apple"])

# Write a function square(num) that returns the square of a number.
def square(num):
    return num * num
print("Square of 4:", square(4))
print("Square of 7:", square(7))

# Write a function add_five(num) that returns number + 5.
def add_five(num):
    return num + 5
print("10 + 5 =", add_five(10))
print("20 + 5 =", add_five(20))

# Create an empty function using pass.
def empty_function():
    pass

# Define a function now and complete its logic later using pass.
def future_function():
    pass







