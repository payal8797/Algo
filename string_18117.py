def sort_elements(array):
    for i in range(n):
        i=1
        while i<(n):
            if array[i-1]>array[i]:
                array[i],array[i-1]=array[i-1],array[i]
            i=i+1
    print(array)

if __name__=="__main__":
    n=int(input("Enter number of elements:"))
    array=[]
    for i in range(n):
        y=raw_input("Enter value:")
        array.append(y)
    print(array)
    
    sort_elements(array)


    '''output
    Enter number of elements:5
Enter value:fd43
Enter value:gf7
Enter value:aw2
Enter value:54
Enter value:hy
['fd43', 'gf7', 'aw2', '54', 'hy']
['54', 'aw2', 'fd43', 'gf7', 'hy']
'''
