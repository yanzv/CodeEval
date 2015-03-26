#Number of Ones challenge from https://www.codeeval.com/open_challenges/16/
#Write a program which determines the number of 1 bits in the internal representation of a given integer.
#Yan Zverev
#2015

def convertToBinary(number):
    counter = 2
    binaryNumber = ''
    while counter*2 <=number:
        counter = counter *2
    while counter > 0:
        if(number-counter) >= 0:
            binaryNumber+="1"
            number = number - counter
            counter = int(counter/2)
        else:
            binaryNumber+="0"
            counter = int(counter/2)
    return binaryNumber
        
            
binString = convertToBinary(21)
count = 0
for char in binString:
    if char == '1':
        count+=1
print(count,":",binString)
    

        
