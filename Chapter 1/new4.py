L = [2,4,5,6,7,8,10,11]

i = 0 
while(i<len(L)):
    if(L[i]%2==0):
        L.remove(L[i])
    else:
        i+=1
print(L)

