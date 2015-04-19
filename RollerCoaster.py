def rOllerCoaster(text):
    lastUpper = False
    newText =''
    textList = list(text)
    for pos in range(0,len(textList)):
        if(textList[pos].isalpha()):
            if(lastUpper == False):
                textList[pos]=textList[pos].upper()
                lastUpper = True
            else:
                textList[pos]=textList[pos].lower()
                lastUpper = False
    return "".join(textList)
                

def main():
    print(rOllerCoaster('tes3223t'))


main()
