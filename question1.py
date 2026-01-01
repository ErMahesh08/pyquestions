# Create a list with 5 different data types.

list1=['1','2','3', "mahesh", "sarry", "bhavesh", 11 , 12, 11.2, ['xyz','abc'], True]
print(list1)

#Find the length of a list without counting manually.
print(len(list1))

#Access the first and last elements of a list using indexing.
print(list1[0])
print(list1[10])

#Access the last element using negative indexing.
print(list1[-1])

print("python" in list1)

#Convert a list into a tuple.
new_tuple= tuple(list1)
print(type(new_tuple))

#Convert a tuple into a list.
new_list = list(new_tuple)
print(type(new_list))

#Create a tuple with only one element.
tuple1= 1 ,
print(type(tuple1))

#Create a set with duplicate values and print it.
dup_tuple = ("mahesh", "dhiraj", "ankit", "mahesh" , "1" , "1", 2, 2) 
print(dup_tuple)


#Iterate through a set using a for loop.

set1 = {"Apple", "Banana", "Cherry", "Date"}

for frt in set1:
    print(frt)

#Change the second element of a list.
list2= ["Apple", "Banana", "Cherry", "Date"]
list2[1]= "mango"
print(list2)

#Replace the first three elements of a list using slicing.
list2= ["Apple", "Banana", "Cherry", "Date"]
list2 [:3]= 1 , 2, 4, "mahesh"
print(list2)

#Insert "AWS" at index position 1 in a list.
list2= ["Apple", "Banana", "Cherry", "Date"]
list2.insert(0,"aws")
print(list2)

#Append an element "Docker" to a list.
list2.append("Docker")
print(list2)



#Extend a list using another list and a tuple.
stdName   = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"]
stdRollNo = (1,2,3,4,5)
nl1=list(stdRollNo)
stdclass  = ["A" , "B"]
school = stdName + nl1
school.extend(stdclass)
print("this is school",school)

# Remove a specific element from a list using remove().
stdName   = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"]
stdName.remove("Mayur")
print(stdName)

# Remove the last element from a list using pop().
stdName.pop()
print(stdName)

#Sort a list of integers in ascending order.
num = [29, 3, 15, 22, 7, 11, 30,
        1, 19, 8, 25, 
       4, 13, 27, 6, 17, 
       9, 21, 2, 14, 26, 10, 5,
         23, 18, 12, 28, 16, 24, 20
         ]
num.sort()
print(num)

#Sort a list of strings in descending order.

num.sort(reverse=True)
print(num)

#Reverse a list using an inbuilt method
num = [29, 3, 15, 22, 7, 11, 30,
        1, 19, 8, 25, 
       4, 13, 27, 6, 17, 
       9, 21, 2, 14, 26, 10, 5,
         23, 18, 12, 28, 16, 24, 20
         ]
num.reverse()
print(num)

#Copy a list using assignment and explain the result.


#Copy a list using the copy() method and show the difference.

numint = [29, 3, 15, 22, 7, 11, 30,
        1, 19, 8, 25, 
       4, 13, 27, 6, 17, 
       9, 21, 2, 14, 26, 10, 5,
         23, 18, 12, 28, 16, 24, 20
         ]
cpynumlist = numint.copy()
print(cpynumlist)

#Join two lists using the + operator.
join1 = [29, 3, 15, 22, 7, 11, 30,
        1, 19, 8, 25, 
       4, 13, 27, 6, 17, 
       9, 21, 2, 14, 26, 10, 5,
         23, 18, 12, 28, 16, 24, 20
         ]
join2   = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"]

join3 = join1 + join2
print(join3)

#Change a tuple value by converting it into a list.

orginal_tuple = ("mahesh", "dhiraj", "ankit", "mahesh" , "1" , "1", 2, 2) 
change_list = list(orginal_tuple)
change_list[0]= "piyush"
change_tuple= tuple(change_list)
print(change_tuple)

#Join two tuples using the += operator.

tuple1 = ("A", "B", "C")
tuple2 = (1, 2, 3)
tuple1+=tuple2
print(tuple1)

#Perform tuple unpacking using the * operator.

unpack = (29, 3, 15, 22, 7, 11, 30,
        1, 19, 8, 25, 
       4, 13, 27, 6, 17, 
       9, 21, 2, 14, 26, 10, 5,
         23, 18, 12, 28, 16, 24, 20
         )
sortunpack= sorted(unpack)
print(sortunpack)
A , B , *C , D , E = sortunpack

print("A:-", A)
print("B:-", B)
print("C:-", C)
print("D:-", D)
print("E:-", E)


#Add elements of a list to a set.
set1    = {"Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"}
addlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
set1.update(addlist)
print(set1)

# Find the common elements between two sets.

set_a = {"Apple", "Banana", "Cherry", "Date"}
set_b = {"Banana", "Dragonfruit", "Date", "Elderberry"}

set_c = set_a | set_b

print("this is set c" ,set_c)

#Find elements present in the first set but not in the second set

find = set_a - set_b
print(find)

#Find all elements except common ones from two sets.










