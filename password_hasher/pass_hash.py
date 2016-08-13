import bcrypt

choice = int(raw_input("""Would you like to 
(1) hash a new password 
(2) Check a currently hashed one?"""))

if choice == 1: #Hash a password for the first time, with a randomly-generated salt
    keysFile = open("keys.txt", "w")
    newPwd = raw_input("Please type the password you would like to hash: ")
    hashed = bcrypt.hashpw(newPwd, bcrypt.gensalt(10))  
    print "Your hashed password is: ", hashed, "\nSaved to file \"keys.txt\""
    keysFile.writelines(hashed)
    
if choice == 2:
    keysFile = open("keys.txt", "r")
    hashed = keysFile.readline()
    Pwd = raw_input("Please type the password you would like to check: ")
    if bcrypt.hashpw(Pwd, hashed) == hashed:
        print "It matches"
    else:
        print "It does not match"
keysFile.close()