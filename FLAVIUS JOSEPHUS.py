def execution(n,m):
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
    for pos in range(-1,n-1):
        if(
            
def main():
    execution(10,3)

main()
