number = input("Enter a number of your choice: ")
number1 = input("Tell a number to be checked: ")
if number%4==0:
    print "%d is divisible by 4"%(number)
elif number%2== 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

if number % number1 == 0:
    print(number, "divides evenly by", number1)
else:
    print(number, "does not divide evenly by", number1)
