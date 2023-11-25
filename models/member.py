class Member:
    def __init__(self, username: str, email: str):
        self._email = email
        self._username = username
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email:str):
        self._email = email
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username:str):
        self._username = username