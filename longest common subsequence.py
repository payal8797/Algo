def LCS(array1, array2, i, j): 
    arr=[]
    if i == 0 or j== 0: 
        return 0; 
    elif array1[i-1] == array2[j-1]: 
        arr.append(array2[j-1])
        return 1 + LCS(array1, array2, i-1, j-1),arr; 
    else: 
        return max(LCS(array1, array2, i, j-1), LCS(array1, array2, i-1, j)); 

    
if __name__=="__main__":
    array1=str(input("Enter string 1:"))
    array2=str(input("Enter string 2:"))
    i=len(array1)
    j=len(array2)
    LCS(array1,array2,i,j)
    arr=[]
    print(arr)
    print("Length of LCS is:", LCS(array1,array2,i,j))