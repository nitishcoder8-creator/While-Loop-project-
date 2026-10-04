movies = []
active = True

while active:
    message = input("Enter something: ")
    movies.append(message)
    
    if message == 'quit':
        active = False
    else:
        print(message)

print("\nYeh rahi Meri final list.\n")
print(f"movies = {movies}")

idx = 1
for movie in movies:
    print(f"\t{idx}. {movie.upper()}")
    idx += 1
