class User:
    def __init__(self, email: str, first_run: bool, gcash_number: str, password: str, picture_link: str, qr_image_id: str, username: str):
        self._email = email
        self._first_run = first_run
        self._gcash_number = gcash_number
        self._password = password
        self._picture_link = picture_link
        self._qr_image_id = qr_image_id
        self._username = username
    
    @property
    def email(self):
        return self._email
    
    @property
    def first_run(self):
        return self._first_run
    
    @first_run.setter
    def first_run(self, first_run: bool):
        self._first_run = first_run
    
    @property
    def gcash_number(self):
        return self._gcash_number
    
    @gcash_number.setter
    def gcash_number(self, gcash_number: str):
        self._gcash_number = gcash_number
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password: str):
        self._password = password
    
    @property
    def picture_link(self):
        return self._picture_link
    
    @picture_link.setter
    def picture_link(self, picture_link: str):
        self._picture_link = picture_link
    
    @property
    def qr_image_id(self):
        return self._qr_image_id
    
    @qr_image_id.setter
    def qr_image_id(self, qr_image_id: str):
        self._qr_image_id = qr_image_id
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username: str):
        self._username = username