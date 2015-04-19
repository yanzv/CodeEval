def rOllerCoaster(text):
    lastUpper = False
    newText =''
    for char in text:
        
        if(char.isalpha()):
            if(lastUpper == False):
                newText+=str(char.upper())
                lastUpper = True
            else:
                newText+=str(char.lower())
                lastUpper = False
        else:
            newText+=str(char)
    print(newText)
    return lastUpper
                

def main():
    rOllerCoaster('tes3223t')


main()
