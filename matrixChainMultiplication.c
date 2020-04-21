#include<stdio.h>
#include<stdlib.h>

matrixChainMul(int d[], int size)
{
    
    int m[size][size];
    int i,j,k,len,res;
    for(i=0;i<size;i++)
    {
        m[i][i]=0;
    }
    j=i+len-1;
    for(len=2;len<size;len++)
    {
        for(i=1;i<j;i++)
        {
            for(k=i;k<=j-1;k++)
            {
                res=m[i][k] + m[k + 1][j] + d[i - 1] * d[k] * d[j];
                if (res<m[i][j])
                {
                    m[i][j]=res;
                }
            }
        }
    }
    return m[1][size-1];
}

int main()
{
    int i,n[100],len;
    printf("Enter the dimensions of the matrices:");
    scanf("%d",&len);
    for(i=0;i<len;i++)
    {
        scanf("%d",&n[i]);
    }
    for(i=0;i<len;i++)
    {
        printf("%d\t",n[i]);
    }
    int size=sizeof(n)/sizeof(n[0]);

    printf("%d",matrixChainMul(n,size));

}