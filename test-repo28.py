# Write a program to check if a given number is a prime number.
# simple code to check if it's a prime number
# using if, else, and for loop

num = int(input("Enter any number to check whether it's a prime number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num," is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")