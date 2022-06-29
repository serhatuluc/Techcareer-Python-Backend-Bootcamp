def check_at():
    mail = input("mail : ")
    if "@" in mail:
        return True
    else: 
        return False

    
print(check_at())