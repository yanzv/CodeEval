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
    execArray = []
    circleArray = []
    for pos in range(0,n):
        #creates a circle array with every position 0 to n-1
        circleArray.append(str(pos))
    executeCount = 0
    while(len(circleArray)>m-1):
        executeCount +=m
        if(executeCount>len(circleArray)):
            executeCount-=len(circleArray)
        execArray.append(circleArray.pop(executeCount-1))
        executeCount-=1
    
    print(executeCount,circleArray)
    while(len(circleArray)>0):
        if(executeCount>=len(circleArray)):
            executeCount = 0
        execArray.append(circleArray.pop(executeCount))
        print(circleArray)
    
    
    return execArray
            
            
def main():
    print(" ".join(execution(10,3)))

main()
