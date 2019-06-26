username = ['jas', 'gurpal', 'kamal', 'harman', 'safee', 'admin']
for user in username:
    if user == '' or len(user) == 0:
        print('We need to find some users!')
    elif user == 'admin':
        print("Hello " + user.title() + ",would you like to see a status report?")
    else:
        print("Hello ," + user.title() + " thank you for logging in again.")

current_user = ['ro']
new_users = ['jas', 'kamal', 'david', 'rams']
for new_user in new_users:
    if new_user.lower() in current_user:
        print("you will need to enter a new username.")
        break
    else:
        print("username is available.")
        break
