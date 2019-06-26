class User:
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.other = user_info
        self.login_attempt = 0

    def describe_user(self):
        profile = dict()
        profile['first_name'] = self.first_name
        profile['last_name'] = self.last_name
        for key, val in self.other.items():
            profile[key] = val
        return profile

    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        return "Welcome " + full_name

    def check_login_attempt(self, attempt):
        self.login_attempt += attempt
        if self.login_attempt >= 3:
            return "Sorry wait for 1 minute"
        else:
            return "There you go..!"

    def reset_login_attempt(self):
        self.login_attempt = 0
        return self.login_attempt


user1 = User(first_name='jas', last_name='rajput', hobby='rambo', father_name='lakhvinder_singh')
print(user1.describe_user())
print(user1.greet_user())
print(user1.check_login_attempt(8))
print(user1.reset_login_attempt())
print(user1.check_login_attempt(1))

user2 = User(first_name='sam', last_name='rajput', hobby='no idea')
print(user2.describe_user())
print(user2.greet_user())