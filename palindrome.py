def isPalindrome(a,b):
    str1=''
    a=a.casefold()
    b=b.casefold()
    if(a==b[::-1]):
        str1="it's a palindrome"
    else:
        str1="Not a palindrome"
    return str1

s1=input("enter  1st value:")
s2=input("enter 2nd value:")
print(isPalindrome(s1,s2))

