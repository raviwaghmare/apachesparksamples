'''
### For Loops:

1. Use a for loop to calculate the sum of all numbers from `1` to `10`.

2. Iterate through a list `my_list = [4, 7, 2, 9, 5]` and find the maximum value in the list using a for loop.
3. Create a dictionary `my_dict` with some key-value pairs and iterate through its keys, printing each key along with its corresponding value.

### If-Else Statements:

1. Write an if-else statement to check if a number `num` is a prime number. Print 'Prime' if it is, otherwise 'Not prime'.
2. Create a variable `marks` and assign a value. Write an if-else statement to assign a grade 'A', 'B', 'C', or 'Fail' based on the marks.
3. Check if a year entered by the user is a leap year or not using an if-else statement. Print 'Leap year' or 'Not a leap year'.

### While Loops:

1. Using a while loop, find the factorial of a number `n` entered by the user.
2. Write a program that asks the user to guess a secret number between `1` and `10`. Use a while loop to continue asking until the user guesses correctly.
3. Create a variable `num` and initialize it with `100`. Use a while loop to print the numbers from `100` to `80` in steps of `5`.
'''

#1. Use a for loop to calculate the sum of all numbers from `1` to `10`.
j=0
for i in range(1,10):
    j = i + j
print(j)

#2. Iterate through a list `my_list = [4, 7, 2, 9, 5]` and find the maximum value in the list using a for loop.
my_list = [4, 7, 2, 9, 5,55555555]
j=my_list[0]
for i in my_list:
    if i > j:
        j = i
print(j)

val_dict={"dict1":1,"cict2":2,"dict3":3}
for key in val_dict:
    print(val_dict[key])
    

#2. Create a variable `marks` and assign a value. Write an if-else statement to assign a grade 'A', 'B', 'C', or 'Fail' based on the marks.
marks=int(input("input marks"))
if [ marks >= 0  and marks <= 100]:
    if [ marks >= 75 ]:
        print("Grade A")
    elif [ marks >= 65 ]:
        print("Grade B")
    elif [ marks >= 35 ]:
        print("Grade C")
    else:
        print("Failed")
else:
    print("Marks should be between 0 and 100")



#3. Create a variable `num` and initialize it with `100`. Use a while loop to print the numbers from `100` to `80` in steps of `5`.
import time
num = 100
i = 0

while i <= 4 :
    print(num)
    num = num - 5
    i = i + 1
    time.sleep(2)




