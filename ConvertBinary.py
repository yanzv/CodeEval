#Decimal to Binary from challenge 
#You are given a decimal (base 10) number, print its binary representation.
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
        
            
binString = convertToBinary(20)
print(binString,":")
if binString[2] == binString[3]:
    print("true")
else:
    print("false")

        
