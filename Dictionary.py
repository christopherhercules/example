# Dictionary store key-vaule pair (entries / entry)
user_dictionary = {
    "danp": "Dan Pickles",
    "howie": "Howard Johnson"
}

print(user_dictionary["danp"])
user_dictionary["randy"] = "Randolph Scott"
print(user_dictionary["randy"])

username = input("Add a username: ")
name = input("What is th user's full name: ")

user_dictionary[username] = name
print(user_dictionary[username])

search = input("Search by username:")
print(user_dictionary.get(search, "Value not found"))

