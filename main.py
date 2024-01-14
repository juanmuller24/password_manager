import os
import hashlib
import pass_manager

path = os.getcwd()


def item_menu():
    while True:
        print("\n________Menu________")
        print("List the username. (1)")
        print("Store new Username and Password. (2)")
        print("Access the Password. (3)")
        print("Exit. (4)")
        menu = int(input(""))

        if menu == 1:
            data = [filename for filename in os.listdir(path + "/data")]
            if not data:
                print("No usernames")
            else:
                for i in range(len(data)):
                    print(f"{i + 1}. {os.path.splitext(data[i])[0]}")

        elif menu == 2:
            username = input("Username: ").strip()
            password = input("Password: ").encode()
            e = pass_manager.PasswordManager(username, password)
            result = e.store_data()
            print(result)

        elif menu == 3:
            data = [filename for filename in os.listdir(path + "/data")]
            if not data:
                print("No Passwords to access!!")
            else:
                acc_username = input("Enter Username: ")
                e = pass_manager.PasswordManager(acc_username, '')
                result = e.access_password()
                print(result)
        elif menu == 4:
            break
        else:
            print('Select a number from menu.')


if __name__ == "__main__":
    master_password = input('Enter Master Password: ').encode()
    master_hash = hashlib.sha256(master_password).hexdigest()
    if os.path.exists(path + '/master_hash.txt'):
        with open(path + '/master_hash.txt', 'r') as f:
            hash_data = f.read()
        if hash_data == master_hash:
            item_menu()
        else:
            print('Wrong Password!!')
    else:
        with open(path + '/master_hash.txt', 'w') as f:
            f.write(master_hash)
        item_menu()
