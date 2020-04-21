def jobseq(n):
    deadline=[]
    profit=[]
    job_number=[]
    for i in range(n):
        i=i+1
        print("\nJob number:",i)
        m1=int(input("\tEnter deadline:"))
        deadline.append(m1)
        m2=int(input("\tEnter profit:"))
        profit.append(m2)
    for j in range(1,n+1):
        job_number.append(j)
    #print("job number:",job_number)
    #print("Deadlines:",deadline)
    #print("Profit:",profit)
    Z = [x for _,x in sorted(zip(profit,job_number))]
    Y = [x for _,x in sorted(zip(profit,deadline))]
    profit.sort(reverse=True)
    Z.reverse()
    print("Corresponding Job number: ",Z)
    Y.reverse()
    print("Corresponding Deadline: ",Y)
    print("Profit in descending order: ",profit)
    

if __name__=="__main__":
    n=int(input("Enter number of jobs: "))
    jobseq(n)
