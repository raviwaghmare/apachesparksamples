#1. How do you create an empty dictionary in Python?
empty_dict={}
print(empty_dict)

#2. Create a dictionary named person containing keys for "name", "age", and "city" with corresponding values.
person_dict={"name":"Ravi","age":"36","city":"Pune"}

#3. How would you access the "age" value from the person dictionary created earlier?
print(person_dict["age"])

#4. Change the value of the "city" key in the person dictionary to "London".
person_dict["city"]="Mumbai"
print(person_dict["city"])

#5. Add a new key-value pair to the person dictionary for "email" with the value "person@example.com".
person_dict["email"]="ravi@gmail.com"

#6. How do you remove the "age" key and its corresponding value from the person dictionary?
del person_dict["age"]
print(person_dict)

#7. Get all keys present in the person dictionary.
print(person_dict.keys())

#8. Get all values present in the person dictionary.
print(person_dict.values())

#9. Create a nested dictionary named books where each book contains keys for "title", "author", and "year". Include at least two books.
books_nested_dict={
    "book1": {"title":"python","author":"rav","year":"1988"},
    "book2":{"title":"python1","author":"rav1","year":"1980"}
}
print(books_nested_dict)

#10. How would you access the "author" of the second book in the books dictionary?
print(books_nested_dict["book2"]["author"])