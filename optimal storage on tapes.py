def ost(arr,n):
    res1=[]
    for i in range(n+1):
        res=arr[0:i]
        #print("output:",res)
        out=sum(res,0)
        res1.append(out)
    output=sum(res1,0)
    print("Solution:",output)
    
if __name__=="__main__":
    n=int(input("Enter number of programs:"))
    arr=[]
    print("Enter length  of each program:")
    for i in range(n):
        m=int(input())
        arr.append(m)
    arr.sort()
    print("Length of programs on tape:",arr)
    ost(arr,n)