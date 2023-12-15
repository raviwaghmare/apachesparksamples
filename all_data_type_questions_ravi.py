#1. Create a list named my_list with elements [10, 20, 30, 40, 50]. Print the length of the list.
my_list=[10, 20, 30, 40, 50]
print(len(my_list))

#2. Create a string my_string with the text "Hello, Python!". Extract the word "Python" from my_string.
my_string="Hello, Python!"
print(my_string.split(",")[0])

#3. Create an integer variable num1 with the value 25 and a float variable num2 with the value 3.14. Print the sum of these two variables.
num1=25
num2=3.14
print(num1+num2)

#4. Create a dictionary my_dict with keys 'name', 'age', 'city', and their respective values ('Alice', 30, 'New York'). 
# Access the value associated with the 'age' key in the my_dict.

my_dict={"name":"Alice","age":"30","city":"New York"}
print(my_dict["age"])

#5. Create a set named set1 with elements [1, 2, 3, 4] and a tuple named my_tuple with elements (10, 20, 30, 40). 
# Find the intersection of set1 and the elements of my_tuple.
set1=[1, 2, 3, 4]
my_typle=(10, 20, 30, 1)
list3= set1 + list(my_typle)
print(set(list3))


#6. Replace the word "Hello" with "Hi" in the string "Hello, how are you?".
my_string = "Hello, how are you?"
x = my_string.replace("Hello", "Hi")
print(x)

#7. Create a tuple my_tuple with elements (5, 10, 15, 20, 25). Access the third element and attempt to modify its value (Note: Tuples are immutable).
my_tuple=(5, 10, 15, 20, 25)
list1=list(my_typle)
list1[2]=100
my_tuple=tuple(list1)
print(my_tuple)

#8. Add the value 60 to the end of the list my_list. Print the updated list.
my_list=[1,2,3]
my_list.append(60)
print(my_list)

#9. Convert the float 3.14 to an integer.
print(int(3.14))
#10. Remove the 'city' key and its corresponding value from the my_dict. Print the updated dictionary.
person_dict={"name":"Ravi","age":"36","city":"Pune"}
del person_dict["city"]
print(person_dict)


###11. Create a list my_list containing integers [1, 2, 3, 4, 5]. 
# Create a dictionary my_dict with keys 'A', 'B', and 'C' mapping to values from my_list.
my_list=[1,2,3,4,5]
my_dict={"A":my_list[0],"B":my_list[1],"C":my_list[2]}
print(my_dict)




#12. Create a string my_string with the text "Python is awesome!". Extract the word "awesome" from my_string.
my_string="Python is awesome!"
print(my_string.split()[2])

###13. Calculate the result of 8 divided by 3. Convert the result to a string and then to an integer without using the round function.
str1=str(8/3)
print(int(float(str1)))


#14. Create a set set1 with elements [1, 2, 3, 4]. Add the value 5 to set1.
set1={1,2,3,4}
print(set1)
set1.add(5)
print(set1)

#15. Create a tuple my_tuple with elements (10, 20, 30) and another tuple new_tuple with elements (40, 50, 60). Concatenate my_tuple and new_tuple without using loops.
my_tuple=(10,20,30)


#16. Replace the character 'o' with 'x' in the string "Python Programming".
print("Python Programming".replace('o','x'))

#17. Create a dictionary student with 'name', 'age', and 'grades' as keys and their corresponding values ('Alice', 22, [85, 90, 78]). 
# Access the second grade of the student.
student={"name":"Alice","age":"22","grades":[85,90,78]}
print(student["grades"][1])

#18. Create a string my_string with the text "This is a sentence.". Convert the string to uppercase and then split it into a list of words.
print("This is a sentence.".upper().split())

#19. Create a tuple my_tuple with elements (5, 10, 15, 20, 25). Retrieve the last element from the tuple.
my_tuple=(5, 10, 15, 20, 25)
print(my_tuple[-1])

#20. Create a set set1 with elements {'apple', 'banana', 'orange'} and another set set2 with elements {'banana', 'grapes', 'apple'}. Find the difference between set1 and set2.
set1={'apple', 'banana', 'orange'} 
set2={'banana', 'grapes', 'apple'}
print(set1.difference(set2))


#21. Create a list my_list with elements [10, 20, 30, 40, 50]. 
# Convert this list to a string without using any list-specific methods like join().
my_list=[10, 20, 30, 40, 50]
str1=""
for list1 in my_list:
    str1=str1+" "+str(list1)

print(str1)

#22. Create a string my_string with the text "Learning Python is fun!". Count the number of occurrences of the letter 'n'.


#23. Create an integer variable num1 with the value 15 and a float variable num2 with the value 3.5. Convert num1 to a float and multiply it with num2.
num1=15
num2=3.5
print(float(num1)*num2)

#24. Create a dictionary employee with 'name', 'age', and 'department' as keys and their corresponding values ('John', 30, 'Engineering'). Remove the 'department' key and its value from the dictionary.
my_dict={"name":"John","age":"30","dept":"Engg"}
print(my_dict)
del my_dict["dept"]
print(my_dict)

#25. Create a set set1 with elements [1, 2, 3, 4] and another set set2 with elements [3, 4, 5, 6]. Find the union of set1 and set2.
set1={1, 2, 3, 4}
set2={3, 4, 5, 6}
print(set1.union(set2))

#26. Create a tuple my_tuple with elements (5, 10, 15, 20). Access the second to last element from the tuple.
my_tuple=(5, 10, 15, 20)
print(my_tuple[1:])

#27. Create a string my_string with the text "Python is versatile and powerful!". Split the string by the word 'and'.
my_string="Python is versatile and powerful!"
print(my_string.split("and"))

#28. Create a dictionary courses with keys as course names ('Math', 'Science', 'History') 
# and their corresponding values as the number of students enrolled in each course. Access the number of students enrolled in 'Science'.


#29. Create a tuple my_tuple with elements (2, 4, 6, 8). Attempt to modify the value at index 2 in my_tuple (Note: Tuples are immutable).

#30. Create two sets set1 and set2 with elements {1, 2, 3} and {3, 4, 5} respectively. Find the intersection of set1 and set2.
