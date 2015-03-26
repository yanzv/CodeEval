#Sum of Primes challenge from https://www.codeeval.com/open_challenges/4/
#Write a program which determines the sum of the first 1000 prime numbers.
#Yan Zverev
#2015

import sys
def isPrime(number):
    for count in range(2,int(number/2+1),1):
        if(number%count)==0:
            return False
    return True

sum = 2
count = 3
primeCount = 1
while primeCount < 1000:
    if isPrime(count):
        sum=sum+count
        primeCount = primeCount+1
    count=count+2
        
sys.stdout.write(str(sum))
sys.exit(0)