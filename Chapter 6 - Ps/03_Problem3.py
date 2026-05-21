p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe now"
p4 = "click this"

message = input("Enter your comment : ")

if((p1 in message)or (p2 in message) or (p3 in message) or (p4 in message)) :
    print("This comment is a spam!")

else :
    print("This comment is not a spam!")


##### OR ######
# p1 = "make a lot of money"
# p2 = "subscribe now"
# p3 = "Buy now"
# p4 = "click this"

# comm = input("Enter the comment : ")

# if((p1.lower() in comm.lower()) or (p2.lower() in comm.lower()) or (p3.lower() in comm.lower()) or (p4.lower() in comm.lower())):
#     print("This is spam")
# else:
#     print("this is not spam")
