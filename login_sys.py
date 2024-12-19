
#Create a login system in Python using Object-Oriented Programming (OOP).
class LoginSystem:
    def __init__(self, correct_password, max_attempts):
        
        #Initialize the LoginSystem with a correct password and a maximum number of attempts.
        
        self.correct_password = correct_password
        self.max_attempts = max_attempts
        self.attempts = 0

    def get_user_input(self):
        
        #Prompt the user to input the password and return it.
        
        return input("Enter your password: ")

    def validate_password(self, password):
        
        #Check if the entered password is correct.
        
        return password == self.correct_password

    def show_message(self, message):
        
        #Display a message to the user.
        
        print(message)

    def authenticate(self):
        
        #Manage the authentication process.
        
        while self.attempts < self.max_attempts:
            password = self.get_user_input()
            if self.validate_password(password):
                self.show_message("Welcome to the system!")
                return
            else:
                self.attempts += 1
                self.show_message("Wrong Password!")

        self.show_message("Too many failed attempts. Access locked!")

if __name__ == "__main__":
    # Create an instance of LoginSystem with the correct password and maximum attempts
    login_system = LoginSystem(correct_password="123456789", max_attempts=3)

    # Start the authentication process
    login_system.authenticate()
