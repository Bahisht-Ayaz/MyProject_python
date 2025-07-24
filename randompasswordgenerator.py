import random
import string
import sys
import pyperclip

my_password=[]
print("******** Random Password Generator ********")
pswd_length = int(input("Enter password length : "))

if pswd_length < 8 or pswd_length > 20:
    print("Password minimum length is 8 and maximum length is 20")
    sys.exit()

else:
    password_list = string.ascii_letters + string.digits + string.punctuation
    for a in range(pswd_length):
        my_password.append(random.choice(password_list))

    string_pswd = "".join(my_password)
    print(f"Generated password : {string_pswd}")

    choice = input(f"Do you want to copy {string_pswd} ?")
    if choice.lower() == "yes":
        pyperclip.copy(string_pswd)
        print("Password has been copied")