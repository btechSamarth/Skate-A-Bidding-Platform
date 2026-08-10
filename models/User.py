class USER:

    def __init__(self,Id, Username , Email_Id , Password , balance , role):
        self.Id = Id
        self.Username = Username
        self.Email_Id = Email_Id
        self._Password = Password
        self._balance = balance
        self.role = role

    def __str__(self):
        str = f"Id : {self.Id}\nusername : {self.Username}\nemail_id : {self.Email_Id}\npassword : {self._Password}\nbalance : {self._balance}\nrole : {self.role}"
        return str
