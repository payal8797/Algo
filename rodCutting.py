def rodCutting(price,n):
    if n==0:
        return 0
    q=0
    for i in range(1,n):
        cost=price[i]+rodCutting(price,n-i)
        if(cost>q):
            q=cost
    return q
        
if __name__=="__main__":
    len=int(input("Enter length of rod:"))
    yy=int(input("Enter length of each part:"))
    price=[]
    for j in range(1,len):
        y=int(input())
        price.append(y)
    n=int(input("Enter the size whose profit is to be calculated:"))
    q=rodCutting(price,n)
    print "Maximum profit:",q