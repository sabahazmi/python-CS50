people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
# commented previous function because we are using lambda function
# def f(person):
#     return person["house"]

people.sort(key=lambda person: person["name"])

print(people)