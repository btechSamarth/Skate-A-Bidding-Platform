from database import Initialize
from controllers.auth_controller import User_Authentication
from controllers.user_dashboard import User_Dashboard


def main():
    # db initialized
    print("                                                                              Welcome to Skate")
    Initialize.intialize()
    # login/register
    user = User_Authentication()
    #dashboard1
    User_Dashboard(user)

    

    
if __name__ == "__main__":
    main()