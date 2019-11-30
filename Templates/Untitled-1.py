t=int(input())
for i in range(t):
    n=int(input())
    A=input().split(" ")
    list=[]
    for q in A:
        list.append(int(q))
    li=()
    li=list
    print(li)
    while n>2 :
        list.sort()
       
        if n%2==0:
            k=n/2-1
            m=k+1
            if n==4:
                print(k,m)
                print(list[int(m)] )
        else :

            k=n/2
            m=0
        if m!=0:
            if n==4:
                print(list)
            list.pop(int(m))
            list.pop(int(k))
            if n==4:
                print(list)
        else :
            list.pop(int(k))
        n=len(list)
        print(n)
     
      
    y=[]
    print(li) 
    for j in li:
        p=0
        
        if list.index(j)>=0:
            y.append(j)
        p+=1
    print(y)