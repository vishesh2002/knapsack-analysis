#include <stdio.h>
#include<time.h>
#include<stdlib.h>
int max(int a, int b) { return (a > b) ? a : b; }
int knapSack(int W, int wt[], int val[], int n)
{
    if (n == 0 || W == 0)
        return 0;
    if (wt[n - 1] > W)
        return knapSack(W, wt, val, n - 1);
    else
        return max(
            val[n - 1]
                + knapSack(W - wt[n - 1], wt, val, n - 1),
            knapSack(W, wt, val, n - 1));
}
void writetoFile(double time)
{
    FILE *f;
    f  = fopen("greedydata.txt","a");
    fprintf(f,"%f \n",time);
    fclose(f);
}
int main()
{
    int W,val[10], wt[10],n;
    // clock_t start, end;
    // double time;
    printf("\nEnter no of objects: ");
    scanf("%d", &n);
    printf("\n Enter the maximum capacity of the Sack: ");
    scanf("%d", &W);
    for(int i=0;i<n;i++)
    {
        printf("\n Enter the weight of the item # %d : ",i+1);
        scanf("%d", &wt[i]);
        printf("\n Enter the profit of the item # %d : ", i+1);
        scanf("%d", &val[i]);

    }
    // start = clock();
    printf("%d", knapSack(W, wt, val, n));
    // end = clock();
    // time= (double)(end-start )/CLOCKS_PER_SEC;
    // writetoFile(time*1000);
    // printf("\nExecution time : %lf", time);
    return 0;
}