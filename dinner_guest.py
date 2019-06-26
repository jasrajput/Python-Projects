invitation_list = ['joey', 'chandler', 'ross']
invited_people = []
for invited_people in invitation_list:
    invited_people = invited_people.replace('ross', 'john')
    print(invited_people + ", I am inviting you on dinner")

invitation_list.insert(0, 'Rachel')
invitation_list.insert(2, 'Monica')
invitation_list.append('Phoebe')
invitation_list += [invited_people]

for new_invitation in invitation_list:
    print(new_invitation + "(New) I am inviting you on dinner")

while len(invitation_list) != 2:
    not_invited = invitation_list.pop()
    print("Sorry, " + not_invited + " can’t invite you to dinner.")

for final_list in invitation_list:
    print("Hey," + final_list + " You are still invited..!")

new_list = sorted(invitation_list)
print("Total: " + str(len(new_list)))


print('ross can\'t make it to the dinner')
print("Ahh..! just found a bigger table")
print("Sorry guys, I can invite only two people for dinner.")

invitation_list.clear()
print(invitation_list)

