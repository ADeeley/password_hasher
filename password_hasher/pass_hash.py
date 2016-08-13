import bcrypt

#------------------
# To do:
# Add a checking system to hash_pwd to check if the password has already been 
# hashed- use check_pwd function
# add an option to change the file destination.
# take out hard coding from the script

#------------------

destinationFile = "keys.txt"

def hash_pwd(destinationFile):
    '''Hash a password for the first time, with a randomly-generated salt'''
    
    keysFile = open(destinationFile, "a")
    newPwd = raw_input("\nPlease type the password you would like to hash.\n>")
    hashed = bcrypt.hashpw(newPwd, bcrypt.gensalt(10))  
    print "\nYour hashed password is: ", hashed, "\nSaved to file ", destinationFile
    keysFile.write(hashed+ "\n")

def check_pwd(destinationFile):        
    ''' checks if the plain-text password is in the database. returns 
    True or False'''
    
    match = False
    keysFile = open(destinationFile, "r")
    Pwd = raw_input("\nPlease type the password you would like to check: \n>")
    for hash in keysFile:      

        if bcrypt.hashpw(Pwd, hash.strip()) == hash.strip():
            print True
            match = True
            break
    if not match:
        print False

        keysFile.close()

def change_destination(destinationFile):
    destinationFile = raw_input("Type the path of the destination file you would like to use: ")       
    print "\nThe destination file has been updated to: ", destinationFile
    
def engine():        
    while True:
        choice = int(raw_input("""\nWould you like to: 
(1) Hash a new password 
(2) Check a currently hashed one
(3) Change destination file
(4) Quit program
>"""))
            
        if choice == 1: 
            hash_pwd()
        elif choice == 2:
            check_pwd()
        elif choice == 3:
            change_destination()
        elif choice == 4:
            print "\nThanks for hashing!"
            break        

engine()            