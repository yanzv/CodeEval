def execution2(n,m):
    circleArray = []
    executionArray = []
    for pos in range(0,n):
        circleArray.append(pos)
    executedPos = -1
    while(len(circleArray)!=0):
        executedPos+=m
        #print(circleArray)
        #print('pos ',executedPos,"len: ",len(circleArray))
        if(executedPos<len(circleArray)):
            print(circleArray.pop(executedPos))
           
        else:
            pos = -1+executedPos
            print(circleArray.pop(executedPos))
            
        

def execution(n,m):
    pos = -1
    for num in range(0,n):
        pos = pos + m
        if(pos<n):
            print("a",pos)
        else:
            pos = pos - n
            print("b",pos)
            
            
def main():
    execution(10,3)

main()
