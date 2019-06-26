from User import User


class Privileges:
    privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privilege(self):
        print("Admin have privileges like: " + str(self.privileges))


class Admin(User):
    def __init__(self, first_name):
        super().__init__(self, first_name)
        self.privilege = Privileges()



admin = Admin('Jas')
admin.privilege.show_privilege()

