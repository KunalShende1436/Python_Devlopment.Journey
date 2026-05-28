# Count Primes

num = int(input("Enter a number: "))
if num <= 2:
    print(f"Number of primes less than {num}: 0")
    exit()  
prime = [True]*num
prime[0]=prime[1]=False
for i in range(2,int(num**0.5)+1):
    if prime[i]:
        for j in range(i*i,num,i):
            prime[j]=False
print(f"Number of primes less than {num}: {sum(prime)}")
