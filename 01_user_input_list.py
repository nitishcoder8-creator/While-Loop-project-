user_list = []
message = ""

while message != 'quit':
    message = input("Enter something: ")
    
    if message == 'quit':
        break
    
    print(message)
    user_list.append(message)

print("\nMeri final list niche hai:\n")
print(user_list)
