import re
def  PasswdCheck(pwd):

    """check if the password satisfies pre-defined conditions """
    return(len(pwd)>=8 and pwd.isalnum() and not pwd.isalpha() and not pwd.isdigit() and not pwd.islower())



pwd1=input("enter password:")
if(PasswdCheck(pwd1)):
    print("strong password")
else:
    print("weak password")

