#Double Squares challenge from https://www.codeeval.com/open_challenges/33/
#This challenge appeared in the Facebook Hacker Cup 2011.
#A double-square number is an integer X which can be expressed as the sum of two perfect squares. For example, 10 is a double-square because 10 = 3^2 + 1^2. Your task in this problem is, given X, determine the number of ways in which it can be written as the sum of two squares.
#Yan Zverev 
#2015

import math

def isPerfectSquare(number):
    sqrtNum = math.sqrt(number)
    if sqrtNum.is_integer():
        return True
    return False
    

def doubleSqures(number):
    #The algorithm is using the Pythagorean theorem A^2+B^2=C^2
    #C^2 - B^2 = A^2
    #C^2 = number 
    #The fucntions will go through the loop starting at sqrt(number) which will be set as B
    #and get A^2 by C^2-B^2=A^2 which will be checked if A^2 is a perfect square
    
    count = 0
    lastPerfectSquare = 0
    sqrtNumber = int(math.sqrt(number)) #
    while lastPerfectSquare < sqrtNumber:
        numSqrd = sqrtNumber*sqrtNumber
        if isPerfectSquare((number-numSqrd)):
            count=count+1
            lastPerfectSquare = math.sqrt(number-numSqrd)
        sqrtNumber-=1
    return count
    
def main():
    print(doubleSqures(29641625))
main()
