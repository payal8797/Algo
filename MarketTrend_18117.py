def marketTrend(n,price):
    array1=[]                                                   # a=[] means declaration of a
    array4=[]
    array5=[]
    arr=[]
    arr1=[]
    for i in range(0,n):
        array=[]
        array2=[]
        array3=[]
        for j in range(i+1,n):                                      #for each day, change in price with all the upcoming days is calculated
            change=price[j]-price[i]
            array.append(change)
            array2.append(i)                                        #i denotes the day on which the change is seen
            array3.append(j)                                        #j denotes the day on which the change is seen wrt i
        arr1.append(array)
        array1 = [e for e in arr1 if e]                            #empty list(last day) is removed
        array4.append(array2)
        array4 = [e for e in array4 if e]                           
        array5.append(array3)
        array5= [e for e in array5  if e]
    
    ''' 
    print 'Change in shares each day:',arr1                                #all arrays are printed
    print '\nAfter removing empty list from the above array:\n'
    print 'Change in shares each day:',array1
    print 'Value of i:',array4
    print 'Value of j:',array5
    '''

    for i in range(0,len(array1)):                                           #in this, a list of tuple(a,b,c) is created that contains profit earned and the days on which it is calculated
        for j in range(0,len(array1[i])):
            tup=(array1[i][j],array4[i][j],array5[i][j])
            arr.append(tup)
    print 'change in price,index i, index j:', arr

    output=sorted(arr,key=lambda x: x[0])[-1]                                #tuple on which the maximum profit is earned is retrieved
    print '\nMaximum profit is earned on purchasing it on ith day and selling on jth day:',output 
    print '\n'

if __name__=="__main__":
    n=int(input("Enter number of days:"))          #Enter the number of days in which share trend is to be calculated
    price=[]
    for i in range(n):
        i=i+1
        print 'Day:',i
        m1=int(input("\tEnter Price:"))
        price.append(m1)
marketTrend(n,price)                            #function called