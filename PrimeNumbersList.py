#Prime Numbers
#Print out the prime numbers less than a given number N
#Yan Zverev
#2015


import sys
def isPrime(number):
    for count in range(2,int(number/2+1),1):
        if(number%count)==0:
            return False
    return True

number = 3
inputNumber = 1000
if inputNumber >2:
    sys.stdout.write('2')
while number < inputNumber:
    if isPrime(number):
        sys.stdout.write(',')
        sys.stdout.write(str(number))
    number=number+2
sys.stdout.write('\n') 
sys.exit(0)