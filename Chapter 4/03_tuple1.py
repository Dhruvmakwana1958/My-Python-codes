a = (1 , 56 , False , "Rohan" , "Dhruv")

# su apne tuple ni value change kari sakia?
# to javab che na kem ke tuple pan string ni jem j kamm kare che

# a[1] = 36
# print(a)

############################# but  ###################################
# 1)
t  = (2 , 0 , 55 ,25 , [2 , 33]) # ana thi tuple element ni to ny pan ema rahela list element ni valuue change thy
print(t[4][0])

t[4][1] = 99
print(t)

# 2)
x = ("dhruv" , "rahul" , "singham" , 87 , False )

y = list(x)
y[4] = "jigo"
x = tuple(y)  # ana thi tuple ni koi pan value change kari sakia ane list ni koi pan method no use kari saki

print(x)

