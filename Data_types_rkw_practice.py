#Data Type Practice rkw - 
#Integer
val_int=100
print(val_int, type(val_int))

#Float
val_float=float(val_int)
print(val_float)

#String
val_string="String_test"
print(val_string,type(val_string))
print("Is it string?",val_string.islower())

#list
val_list=[val_float,val_string,val_int]
print(val_list)

#tuple
val_tuple=(val_list)
print(val_tuple)

for val in val_tuple:
    print(val)
    
#Dictonary
val_dict={"dict1":val_int,"dict2":val_string,"dict3":val_float}
print(val_dict)

#Date
import datetime
x = datetime.datetime.now()
print(x)

