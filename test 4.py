def bmm (x,y):
    n = z = 0
    j = abs(x*y) +1
    if abs(x)>abs(y) :
    
        n=abs(x)


    else:
       
        n=abs(y)

    #print(n)
    #print(j)

    for i in range (n,j):
        if i%x ==0 and i%y ==0 :
            z=i
            #print(z)
            break
    
    return(z)

x = int(input('please enter x: '))
y = int(input('please enter y: '))
javab = bmm(x,y)
print(javab)