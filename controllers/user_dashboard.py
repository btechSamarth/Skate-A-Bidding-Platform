from controllers import email_controller
from controllers import market_controller
from controllers import account_controller
from controllers import big_events_controller
from helpers.Negative_Input_Handler import CustomError1

def User_Dashboard(user):
    while(True):
            while(True):
                try:
                    user_input = ""
                    str = "                                                                              -----------------Email-----------------\n                                                                              Press 1 To View Your Inbox\n                                                                              Press 2 to View Your Sent Emails\n                                                                              Press 3 To Send a New Email\n\n"
                    if(user.role == "USER"):
                            str = str + "                                                                              -----------------Market-----------------\n                                                                              Press 4 To Sell Products\n                                                                              Press 5 To View Your Products\n                                                                              Press 6 To View Market\n                                                                              Press 7 to Update Any Product\n\n                                                                              -----------------Account-----------------\n                                                                              Press 8 to View Your Balance\n\n                                                                              -----------------Live Event-----------------\n                                                                              Press 9 To View Live Events\n                                                                              Press 10 To Bet\n                                                                              Press 11 To View Your Bids\n\n                                                                              -----------------Exit-----------------\n                                                                              Press 12 To Exit\n---->"
                            while(True):
                                try:
                                    user_input = input(str)
                                    user_input = int(user_input)
                                except CustomError1 as e:
                                    print(e)
                                except ValueError:
                                    print("Please Enter Input In Number")
                                else:
                                    break
                    else:
                        str = str + "                                                                              -----------------Market-----------------\n                                                                              Press 4 to View Market\n\n                                                                              -----------------Live Event-----------------\n                                                                              Press 5 To Fetch Live Events\n                                                                              Press 6 to View Big Events\n                                                                              Press 7 to Declare Result\n\n                                                                              -----------------Account-----------------\n                                                                              Press 8 To Update Account Balance\n\n                                                                              -----------------Exit-----------------\n                                                                              Press 9 to Exit\n---->"
                        user_input = input(str)
                        user_input = int(user_input)
        
                except ValueError:
                    print("                                                                              Please Enter a Correct option")
                finally:
                    break

            if(user.role == "USER"):
                user_dict = {
                    1 : email_controller.show_recieved_emails,
                    2 : email_controller.show_sent_emails,
                    3 : email_controller.send_Email,
                    4 : market_controller.list_product,
                    5 : market_controller.view_my_products,
                    6 : market_controller.view_all_products,
                    7 : market_controller.update_my_product,
                    8 : account_controller.get_balance,
                    9 : big_events_controller.view_big_events,
                    10 : big_events_controller.add_user_bet,
                    11 : big_events_controller.view_my_bids

                }
                if(user_input == 12):
                    break
                elif(user_input < 1 or user_input > 12):
                    print("                                                                              Asked Option Doesn't Exit")
                else:
                    action = user_dict[user_input]
                    action(user)
            else:
                admin_dict = {
                    1 : email_controller.show_recieved_emails,
                    2 : email_controller.show_sent_emails,
                    3 : email_controller.send_Email,
                    4 : market_controller.view_all_products,
                    5 : big_events_controller.fetch_big_events,
                    6 : big_events_controller.view_big_events,
                    7 : big_events_controller.declare_result,
                    8 : account_controller.set_balance,
                }

                if(user_input == 9):
                    break
                elif(user_input < 1 or user_input > 9):
                    print("                                                                              Asked Option Doesn't Exit")
                else:
                    action = admin_dict[user_input]
                    action(user)

    print("                                                                              Missing You Already!")