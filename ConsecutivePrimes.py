#Adam Zverev
import sys
myCount = []

def isPrime(number):
    for count in range(2,int(number/2+1),1):
        if(number%count)==0:
            return False
    return True

def calculateConsecutivePrimes(startNum, totalNum, count):
    if(startNum == totalNum):
        print("here")
        return 1
    for num in range(startNum + 1,totalNum+1):
        print(startNum,":",num)
        if(isPrime(startNum+num)):
            count += calculateConsecutivePrimes(startNum+1,totalNum,count)
        return count


def calculateConsecutivePrimes2(inputArray,count):
    #print(inputArray)  
    if(len(inputArray) == 1):
        return 1
    firstNum = int(inputArray.pop(0))
    for num in inputArray:
        if(isPrime(firstNum+int(num))):
            print(num,":",inputArray)
            count+=calculateConsecutivePrimes2(inputArray,count)
    return count
    

def calculateConsecutivePrimes3(inputString,count):
    if (len(inputString) == 1):
        myCount.append(1)
    num = inputString[0]
    tempString = inputString.replace(num,"")
    for nextNum in tempString:
        if(isPrime(int(num) + int(nextNum))):
            calculateConsecutivePrimes3(tempString.replace(num,""),count)
            

def main():
    userInput = 18
    inputArray = []
    for num in range (1,userInput+1):
        inputArray.append(str(num))
    inputString = ''.join(inputArray)
    calculateConsecutivePrimes3(inputString,0)
    print(len(myCount))
    
    
    
main()