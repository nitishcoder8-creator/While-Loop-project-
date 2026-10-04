race = []

while True:
    name = input("Enter something: ")
    
    if name == 'quit':
        break
    else:
        print(name)
        race.append(name)

print(f"\nrace = {race}")

oil = []
while race:
    nima = race.pop()
    oil.append(nima)

print(f"\noil = {oil}\n")
print("Here are the objects in oil:\n")

number = 1
for item in oil:
    print(f"{number}. {item}")
    number += 1
