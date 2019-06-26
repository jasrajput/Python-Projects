# Find phone_no using regular expression
# 415-555-4242
import re


def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 11):
        if not text[i].isdecimal():
            return False
    return True


print(is_phone_number('123-456-7891'))

texts = 'hello'
# for k in range(0, 3):
# print(texts[k])
# texts[0] = h
# texts[1] = e
# texts[2] = l

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i + 12]
    print(chunk)
    if is_phone_number(chunk):
        print('Phone number found: ' + chunk)
print('Done')
# 0:12 1:13 2:14 3:15


msg = 'hello'
# for i in range(len(msg)):
# print(str(i), msg[i: i + 5])


# 0:5 1:6 2:7 3:8
# Total 5 times
# 0 + 5 = 0:5 hello
# 1 + 5 = 1:6 ello
# 2 + 5 = 2:7 llo
# 3 + 5 = 3:8 lo
# 4 + 5 = 4:9 0

# Passing a string value representing your regular expression to re.compile() returns a Regex pattern object
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# returns a match object if it found the string searching for.
mo = phoneNumRegex.search('My number is (415) 555-4242.')
# Match object have group method that will return the actual matched text from the searched string
print("Phone number found " + mo.group(1))
print("Phone number found " + mo.group(2))
print("Phone number found " + str(mo.groups()))

# The | character is called a pipe. You can use it anywhere you want to match one of many expressions.
heroRegex = re.compile(r'Batman|superman')
matchObj = heroRegex.search('superman and Batman')
print(matchObj.group())

# question mark can have two meanings in regular expressions:
# or declaring a non-greedy match or flagging an optional group.
haRegex = re.compile(r'(ha){3,5}?')  # min 3 and max 5.(it will return min 3 bcoz of ?.remove ? and it'll return max 5
mo1 = haRegex.search('hahahahaha')
print(mo1.group())
print(mo1 != None)


# search() will return a Match object of the first matched text in the searched string
# findall() method will return the strings of every match in the searched string
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
moSearch = phoneNumberRegex.search('Cell: 412-8031-1234 Work: 123-456-7891')
print(moSearch.group())  # return one occurrence only .return error if not found
mo2 = phoneNumberRegex.findall('Cell: 412-890-1232 Work: 123-456-7891')
print(mo2)  # return every occurrence. return empty list if not found
# with no groups findall() returns a list of string matches
# such as ['415-555-9999', '212-555-0000'] .
# with groups findall() returns a  list of tuples of strings (one string for each group),
# such as [('415', '555', '1122'), ('212', '555', '0000')]

