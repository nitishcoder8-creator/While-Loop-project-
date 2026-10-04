unconfirmed_users = ['alice', 'polim', 'kirin', 'trishna']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(current_user)
    confirmed_users.append(current_user)

print(f"\nConfirmed users: {confirmed_users}")
