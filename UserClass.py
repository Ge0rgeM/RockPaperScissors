class User:
    def __init__(self, id, firstname, lastname, username, password, user_score, PC_score):
        self._id = id
        self._firstname = firstname
        self._lastname = lastname
        self._username = username
        self._password = password
        self._user_score = user_score
        self._PC_score = PC_score
    
    @property #No need for setter
    def id(self):
        return self._id
    @property #No need for setter
    def firstname(self):
        return self._firstname
    @property #No need for setter
    def lastname(self):
        return self._lastname
    @property #No need for setter
    def username(self):
        return self._username
    @property #No need for setter
    def password(self):
        return self._password
    @property #No need for setter
    def user_score(self):
        return self._user_score
    @property #No need for setter
    def PC_score(self):
        return self._PC_score
    
    def __str__(self):
        return f'''
    User Info:
User_Id: {self._id},
Firstname: {self._firstname},
Lastname: {self._lastname},
Username: {self._username},
Password: {self._password},
User_score: {self._user_score},
PC_Score: {self._PC_score}
'''