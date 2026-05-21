l1 = [22 , 56 ,2 ,99 ,8]

#1)
l1.sort()
print(l1)

l1.sort(reverse= True)
print(l1)

#2)
l2 = l1.copy()
print(l2)

#3)
l3 = ["banana" , "graps" , "guavava"]
l1.extend(l2 + l3)
print(l1)
        #### or ####
# print(l1 + l2 + l3)