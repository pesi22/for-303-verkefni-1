credentials = {}
with open('password.txt') as f:
    credentials = dict(x.rstrip().split(";", 1) for x in f)


username = input("username: ")
password = input("password: ")
#match the password with the username and also check if the user is real
get_pass = credentials.get(username,"")
if get_pass == password:
    print("VELKOMIN")
elif get_pass == "":
    print("EKKI TIL")
else:
    print("RANGT")
