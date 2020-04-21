def binary(arr,low,high,key):
    if(low<=high):
        mid=int((low+high)/2)
        if (key==arr[mid]):
            print("Index is:",mid)
            return mid
        elif(key<arr[mid]):
            return binary(arr,low,mid-1,key)
        else:
            return binary(arr,mid+1,high,key)
    else:
        return -1
    result= binary(arr,0,len(arr)-1,key)
    if result!=-1:
        print("Index is:%d",result)
    else:
        print("Element is not present in array")

if __name__=="__main__":
    n=int(input("Enter number of elements in array:"))
    arr=[]
    
    for i in range(n):
        m=int(input())
        arr.append(m)
    print("Elements of array:",arr)
    key=int(input("Enter element whose index is to be found in array:"))
    low=0
    #arr.sort()
    #print(arr)
    high=len(arr)-1
    mid = binary(arr,low,high,key)
