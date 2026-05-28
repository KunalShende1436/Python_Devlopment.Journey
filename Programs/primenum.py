# Genarate a prime number in range
num = int(input("Enter a number: "))
if num== 2:
    print(f"Prime numbers less than {num}: []")
    exit()
else:
    prime = [True] * num
    prime[0] = prime[1] = False
    for i in range(2, int(num**0.5) + 1):
        if prime[i]:
            for j in range(i*i, num, i):
                prime[j] = False
    print(f"Prime numbers less than {num}: {[i for i in range(num) if prime[i]]}")    