
from database.db_functions import verify_user
from database.db_functions import add_user
import re
from helpers.encrypt_decrypt import encrypt_password
from helpers.password_strength_validation import strength_validation
from helpers.string_input_checker import string_checker
from helpers.int_input_checker import neg_int_checker , int_1_2_checker

def verify_Admin(username):
        print("                                                                              You Have Asked To Login As ADMIN")
        code = ""
        while(True):
            code = input("Enter Your Security Code, In Not Enter \"register\" to Register\n---->")
            if not string_checker(code):
                continue
            if(code.lower() == "register"):
                return register()
            break

        Code = ""
        with open("security.key" , "r") as f:
            Code = f.read()
        if(code == Code):
            print(f"                                                                              Welcome {username}, Email Verified")
            return False
        else:
            print("                                                                              Your Code Didn't Match")
            return True

def login():
    print("                                                                              Welcome to Login Page")
    username = ""
    password = ""
    flag = True
    while(flag):
        while(True):
            username = input('Please Enter Your Username or "register" to Register\n---->')
            temp = string_checker(username)
            if not temp:
                continue
            if(username.lower() == "register"):
                    return register()
            break
        password = input("Please Enter Your Password\n---->")
        user = verify_user(username , password)
        if user != None:
            flag = False
    return user
    
   

def register():
    print("                                                                              Welcome to Registration Page")
    flag = True
    username =""
    email = ""
    password = ""
    role = ""
    while(flag):
        while(True):
            username = input("Enter your username:\n----> ")
            temp = string_checker(username)
            if not temp:
                continue
            break    
        while(True):
            while(True):
                email = input("Enter your email:\n----> ")
                temp = string_checker(username)
                if not temp:
                    continue
                break    
            pattern1 = r"^[a-z0-9]+@skate\.com$"
            pattern2 = r"^[a-z0-9]+@[a-z]+\.com$"
            if(re.fullmatch(pattern1 , email)):
                flag = verify_Admin(username)
                if(flag == False):
                    role = 'ADMIN'
                    break
            elif(re.fullmatch(pattern2 , email)):
                role = 'USER'
                break
            else:
                print("                                                                              Email Provided is Not A Valid Address")
        
       
        while(True):
            str = "\n\nEnter Your Password, You Password Must Follow The Guidline\n1) Password length must be between 8 to 16 charachters longs\n2) Password must contain one Upper and one Lower Case Character\n3) Password must contain one digit from 0 to 9\n4) Password must contain one special character from '*@$%.'\n---->" 
            password = input(str)
            flag = string_checker(password)
            if not password:
                continue
            if(len(password) < 8 or len(password) > 16):
                print("                                                                              Your PassWord is not Correct, Adhere To The Guidlines")
                continue
            flag = strength_validation(password)
            if not flag:
                continue

            break
        encrypted_password = encrypt_password(password)
        flag = add_user(username , email , encrypted_password , role)
    return login()

def User_Authentication():
    user_input = -1
    while(True):
        user_input = input("Press 1 to Login     Press 2 to Register  \n---->" )
        flag = int_1_2_checker(user_input)
        if not flag:
            continue
        user_input = int(user_input)
        break

    if(user_input == 1): 
        return login()
    else:
        return register()