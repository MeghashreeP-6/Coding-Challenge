# Given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

def reverse_fun(x, reverse):
    if x > 2147483648 or x < -2147483647:
        return 0
    else:
        if x < 0:
            temp = -(x)  
        else:
            temp = x
        while(temp != 0):
            remainder = int(temp%10)
            reverse = reverse * 10 + remainder
            temp = temp//10
        if reverse > 2147483648 or reverse < -2147483647:
            return 0
        elif x < 0:
            reverse = "-" + str(reverse)
        else:
            pass
    reverse = int(reverse)
    return(reverse)


reverse = 0
x = 1534236469
result = reverse_fun(x, reverse)
print(result)