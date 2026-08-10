from database.Make_Connection import MAKE_CONNECTION


def intialize():
    
    with MAKE_CONNECTION() as cursor:

        cursor.executescript("""
                CREATE TABLE IF NOT EXISTS USERS(
                    USER_ID INTEGER PRIMARY KEY,
                    USER_USERNAME TEXT NOT NULL UNIQUE,
                    USER_EMAIL TEXT NOT NULL UNIQUE,
                    USER_PASSWORD TEXT NOT NULL,
                    USER_BALANCE INTEGER NOT NULL DEFAULT 0,
                    USER_ROLE TEXT NOT NULL CHECK (USER_ROLE IN ('USER', 'ADMIN'))
                );

                CREATE TABLE IF NOT EXISTS PRODUCTS(
                    PRODUCT_ID INTEGER PRIMARY KEY,
                    SELLER_ID INTEGER NOT NULL,
                    NAME TEXT NOT NULL,
                    PRICE INTEGER NOT NULL,
                    QUANTITY INTEGER NOT NULL,
                    CATEGORY TEXT NOT NULL,
                    FOREIGN KEY(SELLER_ID) REFERENCES USERS(USER_ID)
                );

                CREATE TABLE IF NOT EXISTS EMAILS(
                    EMAIL_ID INTEGER PRIMARY KEY,
                    SENDER_ID INTEGER NOT NULL,
                    RECEIVER_ID INTEGER NOT NULL,
                    SUBJECT TEXT NOT NULL,
                    CONTENT TEXT NOT NULL,
                    SENT_AT DATETIME DEFAULT CURRENT_TIMESTAMP,

                    FOREIGN KEY(SENDER_ID) REFERENCES USERS(USER_ID),
                    FOREIGN KEY(RECEIVER_ID) REFERENCES USERS(USER_ID)
                );

                CREATE TABLE IF NOT EXISTS LIVE_EVENTS(
                    EVENT_ID INTEGER PRIMARY KEY,
                    NAME TEXT NOT NULL,
                    ENDING_DATE TEXT NOT NULL,
                    BASE_BET INTEGER NOT NULL DEFAULT 1000,
                    WINNER INTEGER
                );
                                
                CREATE TABLE IF NOT EXISTS BETTERS(
                    BET_ID INTEGER PRIMARY KEY,
                    EVENT_ID INTEGER NOT NULL,
                    BETTER_ID INTEGER NOT NULL,
                    BETTER_EMAIL TEXT NOT NULL,
                    BET_AMOUNT INTEGER NOT NULL,
                    BET_ON INTEGER NOT NULL,
                    
                    FOREIGN KEY(EVENT_ID) REFERENCES LIVE_EVENTS(EVENT_ID)
                    ON DELETE CASCADE,
                    FOREIGN KEY(BETTER_ID) REFERENCES USERS(USER_ID)
                    ON DELETE CASCADE
                );
            """)

    print("DATABASE CREATED")