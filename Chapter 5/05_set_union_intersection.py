# s1 = {1 , 45 , 6 , 78}
# s2 = {7 , 8 ,  1 , 78}

# print(s2.union(s1))
# print(s1.intersection(s2))


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# result = a.intersection(b)
# print(result)  # Output: {3, 4}
# print(a)       # Output: {1, 2, 3, 4} (original remains same)

# ## BUT ##

# result = a.intersection_update(b) ## intersection_update() method: ,Original set ko hi update kar deta hai, sirf common elements rakh kar.
# # Return kuch nahi karta (None return karta hai).
# print(result)
# print(a)  # Output: {3, 4} (original set changed)

a.symmetric_difference(b)
print(a)

a.symmetric_difference_update(b)
print(a)
