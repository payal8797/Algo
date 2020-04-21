def partition(array,l,h):
    pivot=array[h]
    i=(l-1)
    for j in range(l,h):    
        if(array[j]<=pivot):
            i=i+1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[h]=array[h],array[i+1]
    return (i+1)

def quicksort(array,l,h):
    if(l<h):
        prt=partition(array,l,h)
        quicksort(array,l,prt-1)
        quicksort(array,prt+1,h)

if __name__=="__main__":
    n=int(input("Enter number of elements in array:"))
    array=[]
    for i in range(n):
        m=int(input())
        array.append(m)
    print("Array is:",array)
    quicksort(array,0,n-1)
    print("sorted array:")
    for i in range(n):
        print("%d" %array[i])    