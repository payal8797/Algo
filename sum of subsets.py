def subset_sum(array,Sum,powerset=[]):
    sum1 = sum(powerset)
    if sum1 == Sum: 
        print(powerset)
    if sum1 >= Sum:
        return 
    for i in range(len(array)):
        n = array[i]
        remaining = array[i+1:]
        subset_sum(remaining, Sum, powerset + [n]) 

if __name__=="__main__":
    n=int(input("Enter number of elements:"))
    print("Enter elements:")
    array=[]
    for i in range(n):
        m=int(input())
        array.append(m)
    print("Elements are:",array)
    Sum=int(input("Required sum:"))

    subset_sum(array,Sum)