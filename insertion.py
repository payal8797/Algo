def insertion_sort(array):
    for j in range(1,len(array)):
        key=array[j]
        i=j-1
        while i>=0 and array[i]>key:
            array[i+1]=array[i]
            i=i-1
        array[i+1]=key


if __name__=="__main__":
    n=int(input("Enter elements:"))
    array=[]
    for i in range(n):
        m=int(input())
        array.append(m)
    insertion_sort(array)
    print("Sorted list:")
    print(array) 