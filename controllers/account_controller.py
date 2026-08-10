from database.db_functions import get_balance1
from database.db_functions import set_balance1
from database.db_functions import get_admin_balance1
from controllers.email_controller import send_Email
from helpers.string_input_checker import string_checker
from helpers.int_input_checker import neg_int_checker

def get_balance(user):
    get_balance1(user.Email_Id)



def set_balance(*args):
    balance = 0
    flag = True
    Email = ""
    balance = 0
    temp = 0
    while(flag):
        while(True):
            if(len(args) == 1):
                Email = input("Please Enter User Email Address\n---->")
                flag = string_checker(Email)
                if not flag:
                    continue
                balance = input("Please Enter Amount to Credit\n---->")
                flag = neg_int_checker(balance)
                if not flag:
                    continue
                balance = int(balance)
                break
            else:
                Email = args[1]
                balance = args[2]
                break
        temp = get_admin_balance1(Email)
        if(temp == None):
            continue
        flag = set_balance1(Email , balance + flag)
    print("                                                                              Redirecting You To Email")
    if(len(args) == 1):
        content = f"Hello {Email}, We Have Successfully Added Skate Tokens In Your Account, Your Current Balance is {balance + temp} , Regards , Admin"
        subject = f"Stake Tokens Credited"
        send_Email(args[0] , Email , subject , content)
    elif(len(args) == 3):
        content = f"Hello {Email}, We Have Successfully Placed Your Bid, Your Current Balance is {balance + temp} , Regards , Admin"
        subject = f"Bid Is Live"
        send_Email(args[0] , Email , subject , content)
    else:
        send_Email(args[0] , Email , args[3] , args[4])
