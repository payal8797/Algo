def maxheap(array,n,largest):
    n=int(input("Enter elements in array:"))
    for i in range(n):
        m=int(input())
        array.append(m)
    print("Elements:",array)
    left=2*i
    right=2*i+1
    if(left<=n and array[left]>array[i]):
        largest=left
    else:
        largest =i
    if(right<=n and array[right]>array[largest]):
        largest=right
    
    if(largest != i):
        array[largest],array[i]=array[i],array[largest]
        maxheap(array,n,largest)

if __name__=="__main__":
    array=[]
    n=len(array)
    largest=0
    maxheap(array,n,largest)