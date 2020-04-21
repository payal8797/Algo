#include<stdio.h>
#include<stdlib.h>

int boardPainting(p,n)
{
    
}

int main()
{
    int i,p,n,arr[100];
    printf("Enter number of painters:");
    scanf("%d",&p);
    printf("Enter number of boards:");
    scanf("%d",&n);
    printf("Enter dimensions of board:\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }

    boardPainting(p,n);
}