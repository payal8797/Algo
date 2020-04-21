#include<stdio.h>
#include<stdlib.h>

int fibonacci(int n)
{
    int f[n];
    int i;
    f[0]=0;
    f[1]=1;
    for (i=2;i<=n;i++)
    {
        f[i]=f[i-1]+f[i-2];
    }
    return f[n];
}
int main()
{
    int n;
    printf("Enter the number whose fibonacci number is to be found:");
    scanf("%d",&n);
    //f[n]=fibonacci(n);
    printf("Fibonacci number:%d\n",fibonacci(n));
}