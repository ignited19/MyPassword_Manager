from random import choice, randint, shuffle
from io import *

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class PasswordManager:



    def __init__(self):
        self.password = None

    def GeneratePassword(self):
        self.password = [choice(letters) for _ in range(randint(8,10))]
        self.password += [choice(numbers) for _ in range(randint(2,4))]
        self.password += [choice(numbers) for _ in range(randint(2, 4))]

        shuffle(self.password)
        print(self.password)

        return self.password


    def SavePassword(self,website, email, password):
        user_input = {"Website": website, "E-mail": email, "Password": password}


        for key in user_input.keys():
            if len(user_input[key]) == 0:
                print(f"{key} is missing information")
                return

        try:
            file = open("data.txt", "a")
            file.write(f"{website}|{email}|{password}\n")
            file.close()
        except(Exception):
            print(f"It appears there was an issue writing the data: {Exception}")