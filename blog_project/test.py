numbers = (1, 2, 3, 4, 5)
print(numbers[0])

numbers[0] = 10

person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
}

keys = list(person.keys()) # ['name', 'age', 'city', 'is_student']

i = 0

while i < len(keys):
    key = keys[i] # 
    print(f"{key}: {person[key]}")
    i+= 1

