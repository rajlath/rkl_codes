#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int N;
    int Q;
    int t, x, y;
    int seq;
    int lastAnswer = 0;
    int **seqList;
    int * seqCount;
    int index;
    scanf("%i", &N);
    seqList = malloc(N*sizeof(int *));
    seqCount = malloc(N*sizeof(int));
    for(int i = 0; i < N; i++)
        seqCount[i] = 1;
    scanf("%i", &Q);
    for(int i = 0; i < Q; i++){
        scanf("%i %i %i", &t, &x, &y);
        if(t==1){
            seq = ((x^lastAnswer)%N);
            seqList[seq] = realloc(seqList[seq],seqCount[seq]*sizeof(int));
            seqList[seq][seqCount[seq]-1] = y;
            seqCount[seq]++;
        }else
        {   seq = ((x^lastAnswer)%N);
            index = y%(seqCount[seq]-1);
            lastAnswer = seqList[seq][index];
            printf("%i\n", lastAnswer);
        }  
    }
    for(int i = 0; i < N; i++)
        free(seqList[i]);     
    free(seqList);
    free(seqCount);
            
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}