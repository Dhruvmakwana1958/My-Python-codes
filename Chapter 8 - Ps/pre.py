def is_palindrome(num):

    # convert a number into a string

    str_num = str(num)

    # check the string ia equaal to its reverse 

    if str_num == str_num[::-1]:
        return True
    else:
        return False
    
a = int(input("Enter the number : "))
if is_palindrome(a):
    print(f"{a} is palindrome")
else:
    print(f"{a} is not a  palindrome")