#include <stdio.h>

static int count;

int isPrime(int number){
    for(int i = 2;i<(int)(number/2)+1;i++){
        if (number%i == 0) {
            return 0;
        }
    }
    return 1;
}

int isEven(int number)
{
    if(number%2==0){
        return 1;
    }
    return 0;
}



void calculateNumNecklacesC(int numOfBeads, int beadsArray[], int sizeBeadsArray, int necklace[], int sizeNecklaceArray)
{
    
    if (sizeBeadsArray == 1) {
        if((isPrime(necklace[sizeNecklaceArray-1] + beadsArray[sizeBeadsArray-1]) == 1) && (isPrime(necklace[0] + beadsArray[sizeBeadsArray-1])==1)){
            necklace[sizeNecklaceArray+1] = beadsArray[sizeBeadsArray];
            count +=1;
            
        }
    }else{
        int previousNumber = necklace[sizeNecklaceArray-1];
        int startPos = 0;
        for (int pos = startPos; pos < sizeBeadsArray; pos++) {
            if (isPrime(previousNumber  + beadsArray[pos])) {
                
                
                
				necklace[sizeNecklaceArray] = beadsArray[pos];
				sizeNecklaceArray+=1;
                int tempSizeBeadsArray = sizeBeadsArray-1;
                int tempBeadsArray[tempSizeBeadsArray];
                int tempPos = 0;
                for (int i = 0; i<sizeBeadsArray; i++) {
                    
                    if (i!=pos) {
                        tempBeadsArray[tempPos] = beadsArray[i];
                        tempPos+=1;
                    }
                }
                calculateNumNecklacesC(numOfBeads, tempBeadsArray, tempSizeBeadsArray, necklace, sizeNecklaceArray);
				sizeNecklaceArray-=1;
            }
        }
        
    }
    
}

int main(int argc, const char * argv[])
{
    int input =18;
    count = 0;
    if (isEven(input)) {
        int beadsArray[input-1];
        int pos = 0;
        while (pos<input-1) {
            beadsArray[pos] = pos+2;
            pos+=1;
        }
        int necklace[input];
        necklace[0]=1;
        calculateNumNecklacesC(input, beadsArray, input-1, necklace,1);
        
    }
    printf("answer: %d",count);
}