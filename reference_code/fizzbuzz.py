end = input("Until what number do you want to count towards?")
for number in range (1 , int(end)):
    if number%3 == 0 and number%5 == 0:
        print("fizzbuzz")
    elif number%3 == 0:
        print("fizz")
    elif number%5 == 0:
        print("buzz")
    else:
        print(number)
