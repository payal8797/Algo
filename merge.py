def merge_sort1(array,p,r,q):
    m=r-p+1
    n=q-r
    L=[0] * m
    M=[0] * n
    for i in range(0,m):
        L[i]=array[p+i]
    for j in range(0,n):
        M[j]=array[r+1+j]
    i=0
    j=0
    k=p
    for k in range(p,r):
        if(L[i]<=R[j]):
            array[k]=L[i]
            i=i+1
            k=k+1
        else:
            array[k]=R[j]
            j=j+1
            k=k+1

def merge_sort(array,p,q):
    if p<q:
        r=(p+q-1)/2
        merge_sort(array,p,r)
        merge_sort(array,r+1,q)
        merge_sort1(array,p,r,q)

if __name__=="__main__":
    n=int(input("Enter number of elements:"))
    array=[]
    print("Enter elements:")
    for i in range(n):
        m=int(input())
        array.append(m)
    print("Unsorted array:",array)
    merge_sort(array,0,n-1)
    print("\nSorted array:")
    for i in range(n):
        print(array[i])