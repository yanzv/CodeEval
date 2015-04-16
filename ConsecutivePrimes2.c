#include <stdbool.h>
#include <stdio.h>



const int primes[] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
const int numPrimes = sizeof(primes)/sizeof(primes[0]);


bool isEven(int number)
{
  if(number%2==0){
      return true;
  }
  return false;
}

bool isPrime(int number){
    for (int i = 0; i < numPrimes; i++) {
        if (number == primes[i]) {
            return true;
        }
    }
    return false;
}


void swap(int *array, int i, int j) {
    int tmp = array[i];
    array[i] = array[j];
    array[j] = tmp;
}

int calculateNumNecklacesC(int *beads, int numBeads, int fromPosition) {

    if (fromPosition == numBeads ) {
        if (isPrime(beads[0] + beads[numBeads - 1])) {
            return 1;
        } else {
            return 0;
        }
    }

    int count = 0;
    int previousNumber = beads[fromPosition - 1];
    if (isPrime(previousNumber + beads[fromPosition])) {
        count += calculateNumNecklacesC(beads, numBeads, fromPosition + 1);
    }
    for (int pos = fromPosition + 1; pos < numBeads; ++pos) {
        if (isPrime(previousNumber + beads[pos])) {
            swap(beads, fromPosition, pos);
            count += calculateNumNecklacesC(beads, numBeads, fromPosition + 1);
            swap(beads, fromPosition, pos);
        }
    }

    return count;
}

int main(int argc, const char * argv[])
{
    int numBeads =18;
	int beads[numBeads];
	for (int i = 0; i < numBeads; ++i) {
	    beads[i] = i + 1;
	}
	int count = calculateNumNecklacesC(beads, numBeads, 1);
	printf("%d",count);
}

