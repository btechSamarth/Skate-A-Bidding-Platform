from database.Make_Connection import MAKE_CONNECTION
import sqlite3
from helpers.encrypt_decrypt import decrypt_password


def add_user_bet1():
    pass

def add_user(username , email , password , role):
    with MAKE_CONNECTION() as cursor:
        try:
            cursor.execute("INSERT INTO USERS(USER_USERNAME , USER_EMAIL , USER_PASSWORD , USER_ROLE) VALUES(? , ? , ? , ?)" , (username , email , password , role))
            return False
        except sqlite3.IntegrityError:
            print("Username or Email Already Taken")
            return True
        
def bet_on1(event_id , user_id , email , amount , bet):
    with MAKE_CONNECTION() as cursor:
        cursor.execute("INSERT INTO BETTERS(EVENT_ID , BETTER_ID , BETTER_EMAIL , BET_AMOUNT , BET_ON) VALUES(? , ? , ?, ? , ?)" , (event_id , user_id , email , amount , bet))

    print("Your Bet Has Been Made, Best Of Luck!!")


def fetch_big_events1(matches , ending_dates):
    with MAKE_CONNECTION() as cursor:
        cursor.execute("DELETE FROM LIVE_EVENTS")
        for i in range(len(matches)):
            cursor.execute("INSERT INTO LIVE_EVENTS(NAME , ENDING_DATE) VALUES(? , ?)" , (matches[i] , ending_dates[i]))
        print("Big Events Added Succesfully")


def get_admin_balance1(email):
    with MAKE_CONNECTION() as cursor:
        cursor.execute("SELECT USER_BALANCE FROM USERS WHERE USER_EMAIL = ?",  (email ,))
        temp = cursor.fetchone()
        if(temp == None):
            print("Wrong Email Address Provided!")
            return None
        else:
            return temp[0]


def get_balance1(email):
        with MAKE_CONNECTION() as cursor:
            cursor.execute("SELECT USER_BALANCE FROM USERS WHERE USER_email = ?" , (email,))
            print(f"User Mail : {email}, ACCOUNT BALANCE : {cursor.fetchone()[0]}\n\n")

def get_product_Ids1(Id):
    with MAKE_CONNECTION() as cursor:
        cursor.execute("SELECT PRODUCT_ID FROM PRODUCTS WHERE SELLER_ID = ?" , (Id,))
        product_ids = []
        data = cursor.fetchall()
        if(data == None):
            print("No Product found")
            return None
        for id in data:
            product_ids.append(id[0])
        return product_ids
        

def list_product1(s_id , name , price , quantity , prod_cat):
    with MAKE_CONNECTION() as cursor:
        #                                     1           2       3       4         5
        cursor.execute("INSERT INTO PRODUCTS(SELLER_ID , NAME , PRICE , QUANTITY , CATEGORY) VALUES(? , ? , ? , ? , ?)" , (s_id , name , price ,quantity , prod_cat))

def send_email(s_id , r_id , subject , content):
    with MAKE_CONNECTION() as cursor:
        try:
            cursor.execute("INSERT INTO EMAILS(SENDER_ID , RECEIVER_ID , SUBJECT , CONTENT) VALUES(?, ? , ? , ?)" , (s_id , r_id , subject , content))
        except Exception as e:
            print(e)

def set_balance1(email , balance):
    with MAKE_CONNECTION() as cursor:
        cursor.execute("UPDATE USERS SET USER_BALANCE = ? WHERE USER_EMAIL = ?" , (balance , email))

    if(cursor.rowcount == 0):
        print("Wrong Email Address Provided!")
        return True
    else:
        return False


from models.Emails import EMAIL

def fetch_recieved_emails(Id , offset):
    with MAKE_CONNECTION() as cursor:
        #                     0               1            2           3                   4            
        cursor.execute("SELECT e.SUBJECT , e.CONTENT , e.SENT_AT , s.USER_EMAIL , r.USER_EMAIL FROM EMAILS AS e JOIN USERS AS s ON e.SENDER_ID = s.USER_ID JOIN USERS AS r ON e.RECEIVER_ID = r.USER_ID WHERE e.RECEIVER_ID = ? ORDER BY e.SENT_AT DESC LIMIT ? OFFSET ? " , (Id,5,offset))
        emails = []

        for email in cursor.fetchmany(5):
            e = EMAIL(*email)
            emails.append(e)
        return emails


def fetch_sent_emails(Id , offset):
    with MAKE_CONNECTION() as cursor:
        #                     0               1            2           3                   4            
        cursor.execute("SELECT e.SUBJECT , e.CONTENT , e.SENT_AT , s.USER_EMAIL , r.USER_EMAIL FROM EMAILS AS e JOIN USERS AS s ON e.SENDER_ID = s.USER_ID JOIN USERS AS r ON e.RECEIVER_ID = r.USER_ID WHERE e.SENDER_ID = ? ORDER BY e.SENT_AT DESC LIMIT ? OFFSET ? " , (Id,5,offset))
        emails = []

        for email in cursor.fetchmany(5):
            e = EMAIL(*email)
            emails.append(e)
        return emails

def update_my_product1(s_id , product_id , quantity):
    with MAKE_CONNECTION() as cursor:
        if(quantity == 0):
            cursor.execute("DELETE FROM PRODUCTS WHERE SELLER_ID = ? AND PRODUCT_ID = ?" , (s_id , product_id))
        else:
            cursor.execute("UPDATE PRODUCTS SET QUANTITY = ? WHERE SELLER_ID = ? AND PRODUCT_ID = ?" , (quantity , s_id , product_id))


def validate_event_id1(event_id):
    with MAKE_CONNECTION() as cursor:
        cursor.execute("SELECT NAME FROM LIVE_EVENTS WHERE EVENT_ID = ?" , (event_id,))
        temp = cursor.fetchone()
        if(len(temp) == 0):
            print("No Such Event Exist!")
            return None
        else:
            return temp[0]

def verify_email_for_mail1(r_email):
    with MAKE_CONNECTION() as cursor:
        cursor.execute("SELECT USER_ID FROM USERS WHERE USER_EMAIL = ?" , (r_email,))
        data = cursor.fetchone()
        if(data == None):
            print("Wrong Email Address Provided")
            return None
        else:
            return data


from models.User import USER

def verify_user(username , password):
    with MAKE_CONNECTION() as cursor:

        cursor.execute("Select * FROM USERS WHERE USER_USERNAME = ?" , (username,))
        data = cursor.fetchone()
        if(data == None):
            print("                                                                              Please Check Your Username!")
            return None
        hashed_password = data[3]
        if(decrypt_password(password , hashed_password) == False):
            print("                                                                              Please Check Your Password!")
            return None
        print(f"Welcome to SKATE, {username}")
        user = USER(*data)
        return user

def view_all_products1(Id):
    categories = ["electronics" , "clothes" , "accesories" , "footwears" , "transport"]
    with MAKE_CONNECTION() as cursor:
        categories = categories
        for cat in categories:
            cursor.execute("SELECT p.PRODUCT_ID , p.NAME , p.QUANTITY , p.PRICE ,u.USER_USERNAME , u.USER_EMAIL FROM PRODUCTS as p JOIN USERS as u ON p.SELLER_ID = u.USER_ID WHERE p.CATEGORY = ? AND u.USER_ID != ?" , (cat , Id))

            print(f"---------------{cat}--------------------")

            for row in cursor.fetchall():
                print(f"Product Id: {row[0]}\nProduct Name: {row[1]}\nQuantity Available: {row[2]}\nPrice: {row[3]}\nSeller Name: {row[4]}\nSeller Email: {row[5]}")
                print("\n\n")

from models.Live_Events import LIVE_EVENTS

def view_big_events1(offset):
    with MAKE_CONNECTION() as cursor:
            cursor.execute("SELECT * FROM LIVE_EVENTS LIMIT ? OFFSET ?" , (5,offset))
            events = []
            data = cursor.fetchmany(5)
            if(len(data) == 0):
                  print("No Big Event Listed")
                  return None
            for event in data:
                  e = LIVE_EVENTS(*event)
                  events.append(e)
            return events


from models.Product import PRODUCT

def view_my_products1(Id , offset):
    with MAKE_CONNECTION() as cursor:
        cursor.execute("SELECT * FROM PRODUCTS WHERE SELLER_ID = ? LIMIT ? OFFSET ?", (Id,5,offset))
        products = []
        for product in cursor.fetchmany(5):
            e = PRODUCT(*product)
            products.append(e)
        return products

from models.Bids import BIDS

def view_my_bids1(Id , offset):
    
    with MAKE_CONNECTION() as cursor:
        cursor.execute("SELECT be.EVENT_ID , be.NAME , be.ENDING_DATE, b.BET_AMOUNT , b.BET_ON FROM LIVE_EVENTS AS be JOIN BETTERS as b ON be.EVENT_ID = b.EVENT_ID WHERE b.BETTER_ID = ? LIMIT ? OFFSET ?" , (Id,5 , offset))
        data = cursor.fetchmany(5)
        if((len(data)) == 0):
            print("No Live Bids")
            return None
        bids = []
        for bid in data:
            b = BIDS(*bid)
            bids.append(b)
     
        return bids


def declare_result1(event_id , winner , offset):
    with MAKE_CONNECTION() as cursor:
        cursor.execute("UPDATE LIVE_EVENTS SET WINNER = ? WHERE EVENT_ID = ?" , (winner , event_id))
        cursor.execute("SELECT BETTER_EMAIL , BET_AMOUNT FROM BETTERS WHERE EVENT_ID = ? AND BET_ON = ? LIMIT ? OFFSET ?" , (event_id , winner , 5 , offset))

        data = cursor.fetchmany(5)
        if(len(data) == 0):
            return None
        return data

def delete_event1(event_id):
    with MAKE_CONNECTION() as cursor:
        cursor.execute("DELETE FROM LIVE_EVENTS WHERE EVENT_ID = ?", (event_id ,))


