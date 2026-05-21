friends = ["apple" , "Orange" , 5 , 2.5 , False , "Akash" , "Rohan"]
######## OR ########
friends = list(("apple" , "Orange" , 5 , 2.5 , False , "Akash" , "Rohan"))

print(friends)
print(friends[0])

friends[0] = "Grapes" # Unlike Strirngs lists are mutable
print(friends[0]) 

friends[0:3] = ["niraj" , "BMW" , False]

print(friends)

