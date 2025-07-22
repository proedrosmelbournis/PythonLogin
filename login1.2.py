users = {
        "user1": "user",
        "user2": "user2",
        "user3": "user3"
    }
    
attempts = 3
    
while attempts > 0:
        username = input("enter username: ")
        password = input("enter password: ")
    
        if username in users and users[username] == password:
            print("Login successful!.")
            break
        else:
            attempts -= 1
            print(f"Incorrect password. You have {attempts} attempts left.")
            if attempts == 0:
                print("Too many failed attempts. Account Locked.")
                break