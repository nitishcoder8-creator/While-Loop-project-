persons = {}
active = True

while active:
    name = input("Name: ")
    age = int(input("Age: "))
    persons[name] = age
    
    rest = input("Would you like to continue? (yes/no): ")
    if rest == 'no':
        active = False

print("\n----- Person Results -----")

number = 1
for person, age in persons.items():
    print(f"{number}. {person.upper()}'s age is {age}.")
    number += 1
