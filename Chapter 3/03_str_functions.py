name = "Harry are are" # 1 white space counts 1 , 2 white space counts 2
# either space is between the word , eding the word or staring it will cocnsiders 1 count

print(len(name))
print(name.endswith("ry"))
print(name.startswith("H"))
print(name.capitalize()) # it's capitalize only H will not space after A
print(name.upper())
print(name.lower())
print(name.count("r"))
print(name.find("Harry"))
print(name.find("are"))
print(name.replace("are", "and")) 

Dhruv = ("rohan" , "vivek" , "aaryan" , 56 , True)
print(Dhruv)
print(type(Dhruv))

###########################################
###########################################

# note : str , tuple aa banne ni methon with print j use karvi means
# print(name.upper()) # true

# name.upper()
# print(name) # false

# list , dictonery , set a traney ne pela je te method declare kari ne pachi navi line ma print karavi

# name.upper()
# print(name) # false

