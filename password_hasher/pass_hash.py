import bcrypt

def hash_pwd():
    '''Hash a password for the first time, with a randomly-generated salt'''
    
    keysFile = open("keys.txt", "a")
    newPwd = raw_input("\nPlease type the password you would like to hash.>")
    hashed = bcrypt.hashpw(newPwd, bcrypt.gensalt(10))  
    print "\nYour hashed password is: ", hashed, "\nSaved to file \"keys.txt\""
    keysFile.write(hashed+ "\n")

def check_pwd():        
    ''' checks if the plain-text password is in the database. returns 
    True or False'''
    
    match = False
    keysFile = open("keys.txt", "r")
    Pwd = raw_input("\nPlease type the password you would like to check: \n>")
    for hash in keysFile:      

        if bcrypt.hashpw(Pwd, hash.strip()) == hash.strip():
            print True
            match = True
            break
    if not match:
        print False

        keysFile.close()

def engine():        
    while True:
        choice = int(raw_input("""\nWould you like to: 
(1) Hash a new password 
(2) Check a currently hashed one?
(3) Quit program
>"""))
            
        if choice == 1: 
            hash_pwd()
        elif choice == 2:
            check_pwd()
        elif choice == 3:
            print "\nThanks for hashing!"
            break        

engine()            