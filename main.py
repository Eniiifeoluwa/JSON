# sort_keys orders the list, alphabetically.
# importing  json module
import json

person = {"name": "John Dowey", "age": 30, "city": "New York"}

# Creating an indentation with the dumps function
person_2 = json.dumps(person, indent=4, sort_keys=True)
print(person_2)
#Creating a New File
with open('NEW FILE.json', 'w') as file:
    json.dump(person, file, indent=4)
person = json.loads(person_2)
print(person)


# Encoding
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Max", 37)


def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Error")


userjson = json.dumps(user, default=encode_user)
print(userjson)


# Deccoding
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct['age'])
    return dct


user = json.loads(userjson, object_hook=decode_user)
print(type(user))
