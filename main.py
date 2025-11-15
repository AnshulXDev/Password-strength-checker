# Created by Anshul
# GitHub - @AnshulXDev

# ask for password
password=input("Enter the password: ")

# check length
pass_length=len(password)
if pass_length == 0:
    print("Retry!")
elif pass_length == 6 or pass_length == 7:
    rank_a=0 # weak
elif pass_length >=8 and pass_length <=11:
    rank_a=1 # medium
elif pass_length>=12:
    rank_a=2 # strong

# check special characters and numbers
special_ch="!@#$%^&*()"
have_sp_ch = any(spch in special_ch for spch in password)

nums="0123456789"
have_num = any(num in nums for num in password)

# ranks of special characters
if have_sp_ch==True:
    rank_b=1 # strong
else:
    rank_b=0 # weak

# ranks of numbers   
if have_num==True:
    rank_c=1 # strong
else:
    rank_c=0 # weak

# calculate for rank
score = rank_a + rank_b + rank_c

if score >= 3:
    print("Password is strong")
elif score == 2:
    print("Password is medium")
else:
    print("Password is weak!")