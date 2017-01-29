import controllers
import getpass


def main_menu():
    print("Welcome to our bank service. You are not logged in.\n\
Please register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")

            controllers.register(username, password)

            print("Registration Successful")

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")

            logged_user = controllers.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.username)
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.username)
            print("Your id is: " + str(logged_user.id))
            print("Your balance is:" + str(logged_user.balance) + '$')

        elif command == 'changepass':
            new_pass = input("Enter your new password: ")
            controllers.change_password(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            controllers.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.message)

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("exit - logout and exit")
        elif command == 'exit':
            break
        else:
            print("Invalid command - type help to see commands.")


def main():
    main_menu()


if __name__ == '__main__':
    main()
