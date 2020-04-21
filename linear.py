def linear(arr,n,key):
    for i in range(n):
        if (arr[i]==key):
            print("Element is a index:",i)
            i=i+1
        else:
            return -1
    
if __name__=="__main__":
    n=int(input("Enter number of elements in array:"))
    arr=[]
    for i in range(n):
        m=int(input())
        arr.append(m)
    print("Elements of array:",arr)
    key=int(input("Enter element to be found in array:"))
    linear(arr,n,key)
