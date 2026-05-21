physics = int(input("Please enter physics marks : "))
chemistry = int(input("Please enter chemistry marks : "))
maths = int(input("Please enter maths marks : "))

total = (100*(physics + chemistry + maths))/300

if((physics>=33 and chemistry>=33 and maths>=33) and total>= 40):
    print("Great You are pass , and you got percentage : ",total)

else:
    print("You are failed, try again next year: ",total)