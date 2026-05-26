#FizzBuzz Classic: Write a program that prints numbers from 1 to 50. For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; for numbers divisible by both, print "FizzBuzz".
for num in range(1,51):
    if num% 3 == 0 and num % 5 == 0:
        print(f"{num} is a multiple of both 3 and 5")
    elif num % 3 == 0:
        print(f"{num} is a multiple of 3")
    elif num % 5 == 0:
        print(f"{num} is a multiple of 5")
    else:
        print(f"{num} is not a multiple of 3 or 5")    