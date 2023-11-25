class Group:
    def __init__(self, group_name: str, created_by: str, description: str, members: list, picture_id: str, unique_code: str, transactions: list):
        self._group_name = group_name
        self._created_by = created_by
        self._description = description
        self._members = members
        self._picture_id = picture_id
        self._unique_code = unique_code
        self._transactions = transactions
    
    @property
    def group_name(self):
        return self._group_name
    
    @property
    def created_by(self):
        return self._created_by
    
    @created_by.setter
    def created_by(self, created_by: str):
        self._created_by = created_by
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description: str):
        self._description = description
    
    @property
    def members(self):
        return self._members
    
    @members.setter
    def members(self, members: list):
        self._members = members
    
    @property
    def picture_id(self):
        return self._picture_id
    
    @picture_id.setter
    def picture_id(self, picture_id: str):
        self._picture_id = picture_id
    
    @property
    def unique_code(self):
        return self._unique_code
    
    @unique_code.setter
    def unique_code(self, unique_code: str):
        self._unique_code = unique_code
    
    @property
    def transactions(self):
        return self._transactions
    
    @transactions.setter
    def transactions(self, transactions: list):
        self._transactions = transactions