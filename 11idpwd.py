i = 1
while i<4:
    username_password = {"siri":"0000"}
    name = input("enter username:\n")
    passcode = input("enter password:\n")
    
    
    i+=1
    if username_password.get(name) == passcode:
        print("successfully logged in")
        break
    else:
        print("username_passcode not matched")
else:
    print("attempt maximum")

        
    
