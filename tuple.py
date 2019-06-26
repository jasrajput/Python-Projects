buffet = ('pizza', 'macaroni', 'dry', 'nuts', 'sugar')
for buff in buffet:
    print(buff)
buffet = ('pizza', 'macaroni', 'spaghetti', 'nuts', 'cola')
print("New menu of buffet restaurant")
for buff in buffet:
    print(buff)

banned_user = ['caronlina', 'david', 'fedrick']
user = 'don'
if user not in banned_user:
    print(user.title() + 'You can post a response if you wish.')
