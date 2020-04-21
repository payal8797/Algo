#Time complexcity = O(logn)
#space complexcity = O(1)
#the function uses Divide and conquer strategy (search search)
#After rotation, the array will still be in sorted order at some mid value.
#we search for this mid value of rotation, but the element can also be in the other half.
#this is the reason for the 2 consecutive recurssive calls.
def search(array,start,end,key):
    if(start<=end):
        mid=int((start+end)/2)
        if (key==array[mid]):
            return mid
        elif(key<array[mid] and key>=array[start]):
            return search(array,start,mid-1,key)
            return search(array,mid+1,end,key)
        else:
            return search(array,mid+1,end,key)
            return search(array,start,mid-1,key)
    else:
        return -1
    
if __name__=="__main__":
    size=int(input("Enter size of the array: "))
    array=[]
    for i in range(size):
        element=int(input("Enter element: "))
        array.append(element)
    key=int(input("Enter element whose index is to be search:"))
    result= search(array,0,len(array)-1,key)
    if result!=-1:
        print("Element found at Index : ",result)
    else:
        print("Element not found.")

#--------------------OUTPUT----------------------
#Enter size of the array: 6
#Enter element: 13
#Enter element: 18
#Enter element: 25
#Enter element: 2
#Enter element: 8
#Enter element: 10
#Enter element whose index is to be search:8
#Element found at Index :  4


#Enter size of the array: 8
#Enter element: 10
#Enter element: 20
#Enter element: 30
#Enter element: 40
#Enter element: 50
#Enter element: 60
#Enter element: 70
#Enter element: 5
#Enter element whose index is to be search:5
#Element found at Index :  7


