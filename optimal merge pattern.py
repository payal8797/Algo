 ddef omp(arr,n):
    for i in range(n-1):
        arr[i+1]=arr[i]+arr[i+1]
        arr.sort()
    print("result:",arr[-1])

if __name__=="__main__":
    n=int(input("Enter number of files:"))
    print("Enter number of sub-files in each file:")
    arr=[]
    for i in range(n):
        m=int(input())
        arr.append(m)
    arr.sort()
    print("Sub-files in files:",arr)
    omp(arr,n)