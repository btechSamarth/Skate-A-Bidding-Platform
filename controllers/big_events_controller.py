from database.db_functions import view_big_events1
from database.db_functions import view_my_bids1
from database.db_functions import fetch_big_events1
from database.db_functions import validate_event_id1
from database.db_functions import get_admin_balance1
from database.db_functions import validate_event_id1
from database.db_functions import set_balance1
from database.db_functions import delete_event1
from controllers.account_controller import set_balance
from database.db_functions import bet_on1
from controllers.email_controller import send_Email
from database.db_functions import declare_result1
from bs4 import BeautifulSoup
from selenium import webdriver
from helpers.int_input_checker import neg_int_checker , int_1_2_checker


def view_big_events(user):
    offset = 0
    count = 1
    while(True):
        events = view_big_events1(offset)
        if(events == None):
            break
        for event in events:
            
            print(f"                                                                              ---------------------------EVENT {count}---------------------------")
            print(f"                                                                              Id: {event.Id}\n                                                                              Name: {event.Name}\n                                                                              Ending Date: {event.Ending_Date}\n                                                                              Base Bet: {event.Base_Bet}")
            print("\n\n")
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

def view_my_bids(user):
    offset = 0
    count = 1
    while(True):
        bids = view_my_bids1(user.Id , offset)
        if(bids == None):
            break
        for bid in bids:
            print(f"                                                                              ---------------------------BID {count}---------------------------")
            print(f"                                                                              Event Id: {bid.Event_Id}\n                                                                              Name: {bid.Name}\n                                                                              Ending Date: {bid.Ending_Date}\n                                                                              Bet Amount: {bid.Bet_Amount}\n                                                                              Bet On: {bid.Bet_On}")
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


def fetch_big_events(user):
    driver = webdriver.Edge()
    driver.get("https://www.cricbuzz.com/cricket-match/live-scores/upcoming-matches")
    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    rows = soup.select("a.w-full.bg-cbWhite.flex.flex-col.p-3.gap-1[title]")
    print("Rows found:", len(rows))

    driver.quit()
    dates = soup.select("span.text-cbPreview")
    matches = []
    end_dates = []
    for row in rows:
        matches.append(row["title"])
    for date in dates:
        end_dates.append(date.get_text(strip=True))
    fetch_big_events1(matches, end_dates)

def add_user_bet(user):
    flag = True
    Email = user.Email_Id
    user_balance = 0
    betting_amount = 0
    event_id = -1
    user_id = user.Id
    event_name = ""
    bet = -1

    while(True):  #event id
            event_id = input("Enter Event Id\n---->")
            flag = neg_int_checker(event_id)
            if not flag:
                continue
            event_id = int(event_id)
            event_name = validate_event_id1(event_id)
            if not event_name:
                continue
            break
        

    while(True):  #betting amount
        betting_amount = input("Enter Betting Amount\n---->")
        flag = neg_int_checker(betting_amount)
        if not flag:
            continue
        betting_amount = int(betting_amount)
        break

    user_balance = get_admin_balance1(Email)

    if(betting_amount > user_balance):
        print("                                                                              User Do Not Have Enough Balance")
        print("                                                                              Redirecting You To Email")
        send_Email(user)
        return

   

    while(True):
        bet = input(f"-----------------{event_name}-----------------\nEnter 1 To Bet on Team A\nEnter 2 To Bet on Team B\n---->")
        flag = int_1_2_checker(bet)
        if not flag:
            continue
        bet = int(bet)
        break
           
    bet_on1(event_id , user_id , Email , betting_amount , bet)
    print("\n                                                                              Redirecting You To Bank Account")
    set_balance(user , Email , user_balance - betting_amount)


def declare_result(user):
    event_id = -1
    winner = -1
    while(True):
            event_id = input("Please Enter Event Id\n---->")
            flag = neg_int_checker(event_id)
            if not flag:
                continue
            event_id = int(event_id)
            flag = validate_event_id1(event_id)
            if not flag:
                break
       
    while(True):
            try:
                winner = input("Please Enter Winner no (1-> Team A, 2->Team B, -1->Draw)\n---->")
                winner = int(winner)
                if(winner != 1 and winner != 2 and winner != -1):
                    print("                                                                              Not a Valid Input")
            except ValueError:
                print("                                                                              Please Enter Input in number")
            else:
                break
    offset = 0
    while(True):
        datas = declare_result1(event_id , winner , offset)
        if(datas == None):
            break
        for data in datas:
            user_balance = get_admin_balance1(data[0])
            set_balance1(data[0] , user_balance + 2*data[1])
            subject = "CONGRATULATIONS, YOU WON THE BET"
            content = f"Hello {data[0]}, You Won Your Bet, Your Current Balance is {user_balance + 2*data[1]} , Ragards , Admin"
            set_balance(user , data[0] , user_balance + 2*data[1] , subject , content)
        offset += 5


    delete_event1(event_id)
