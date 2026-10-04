active = True

while active:
    users = input("Age: ")
    
    if users == 'quit':
        break
    
    users = int(users)
    
    if users <= 3:
        print("\tTicket price: Free\n")
    elif users <= 12:
        print("\tTicket price: 10$\n")
    else:
        print("\tTicket price: 15$\n")
