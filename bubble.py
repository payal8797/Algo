def bubble(array):
    array=[]
    n=int(input("Enter number of elements:"))
    for s in range(n):
        m=int(input())
        array.append(m)
    print("Elements are:",array)
    for i in range(n):
        for j in range(n-i-1):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]
    print("Sorted array is:")
    for i in range(n):
        print("%d" %array[i])
    
if __name__=="__main__":
    array=[]
    bubble(array) 