from database.db_functions import fetch_sent_emails
from database.db_functions import fetch_recieved_emails
from database.db_functions import send_email
from database.db_functions import verify_email_for_mail1
from helpers.string_input_checker import string_checker
from helpers.int_input_checker import int_1_2_checker

def show_sent_emails(user):
    user_Id = user.Id
    offset = 0
    count = 1
    while(True):
        emails = fetch_sent_emails(user_Id , offset)
        if(len(emails) == 0):
            print("No More Emails")
            break
        
        for email in emails:
            print(f"---------------------------EMAIL {count}---------------------------")
            print(f"From: {email.Sender_Email}\nTo: {email.Reciever_Email}\nTime: {email.Sent_At}\nSubject: {email.Subject}\n\nContent: {email.Content}")
            count += 1
        user_input = -1
        while(True):
            user_input = input("Press 1 To Show More And 2 For Exit\n---->")
            flag = int_1_2_checker(user_input)
            if not flag:
                continue
            user_input = int(user_input)
            break
        if(user_input == 2):
            return 
        else:
            offset += 5

def show_recieved_emails(user):
    user_Id = user.Id
    offset = 0
    count = 1
    while(True):
        emails = fetch_recieved_emails(user_Id , offset)
        if(len(emails) == 0):
            print("No More Emails")
            break
       
        for email in emails:
            print(f"---------------------------EMAIL {count}---------------------------")
            print(f"From: {email.Sender_Email}\nTo: {email.Reciever_Email}\nTime: {email.Sent_At}\nSubject: {email.Subject}\n\nContent: {email.Content}")
            count += 1
        user_input = -1
        while(True):
            user_input = input("Press 1 To Show More And 2 For Exit\n---->")
            flag = int_1_2_checker(user_input)
            if not flag:
                continue
            user_input = int(user_input)
            break
        if(user_input == 2):
            return
        offset += 5

def send_Email(*args):
    s_id = args[0].Id
    flag = True
    r_email = ""
    r_id = 0
    subject = ""
    content = ""
    while(flag):
        if(len(args) == 1):
            r_email = input("To? (Email Id)\n---->")
        else:
            r_email = args[1]
        data = verify_email_for_mail1(r_email)
        if(data != None):
            r_id = data[0]
            flag = False
    if(len(args) != 4):
        subject = ""
        content = ""
        while(True):
            subject = input("Subject : ")
            flag = string_checker(subject)
            if not flag:
                continue
            break
        while(True):
            content = input("Content : ")
            flag = string_checker(subject)
            if not flag:
                continue
            break
        
        send_email(s_id , r_id , subject , content)
    else:
        send_email(s_id , r_id , args[2] , args[3])
    print("Email Sent Successfully!")
