while True:
    factorial_number = int(input("Enter number: "))
    
    fact = 1
    i = 1
    
    while i <= factorial_number:
        fact *= i
        i += 1
    
    print(fact)
    
    if factorial_number == 5:
        break
