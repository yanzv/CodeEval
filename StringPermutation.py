#String Permutations challenge from https://www.codeeval.com/open_challenges/14/
#Write a program which prints all the permutations of a string in alphabetical order. We consider that digits < upper case letters < lower case letters. The sorting should be performed in ascending order.
#Yan Zverev
#2015

import sys
strings=[]
def stringPermutate(myString,resultString):
    #The function uses recursion to permutate the string
    for char in myString:
        if len(myString) == 1:
            strings.append(str(resultString+char))
        else:
            tempString = myString.replace(char,"")
            print(tempString,"\n")
            stringPermutate(tempString,resultString+char)

stringPermutate("hat",'')
result = ",".join(sorted(strings))
sys.stdout.write(result+"\n")