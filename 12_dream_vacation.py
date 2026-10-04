users = {}
active = True

while active:
    dreamer = input("User: ")
    wish = input("Dream vacation: ")
    users[dreamer] = wish
    
    tired = input("Would you want to continue further? (yes/no): ")
    if tired == 'no':
        active = False

print(f"\n{users}")
