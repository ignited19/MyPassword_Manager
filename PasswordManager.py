from random import choice, randint, shuffle
from io import *
from json import *
from datetime import *


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class PasswordManager:

    def __init__(self):
        self.password = None

    def findPassword(self, website, ):

        try:
            with open("data.json","r") as data_file:
                JSON_Data = load(data_file)

            if website in JSON_Data:
                return JSON_Data[website]["Password"]
        except:
            print("No data to search from")



    def GeneratePassword(self):
        self.password = [choice(letters) for _ in range(randint(8,10))]
        self.password += [choice(numbers) for _ in range(randint(2,4))]
        self.password += [choice(numbers) for _ in range(randint(2, 4))]

        shuffle(self.password)
        print(self.password)

        return self.password


    def SavePassword(self,website, email, password):
        user_input = {"Website": website, "E-mail": email, "Password": password}
        new_json_data = {
            website:{
            "E-mail": email,
            "Password": password,
            "DatePasswordGenerated": str(date.today())
            }
        }

        #Check to make sure that all the fields are populated
        for key in user_input.keys():
            if len(user_input[key]) == 0:
                print(f"{key} is missing information")
                return

        #Handles the creation, update, and writting of JSON
        try:

            with open("data.json", "r") as data_file:
                print("1")
                old_data = load(data_file)

                old_data.update(new_json_data)

            with open("data.json", "w") as data_file:
                dump(old_data, data_file, indent=4)
                data_file.close()

        #Incase the file goes missing or this is the first run of the program
        except:

            with open("data.json", "w") as data_file:
                dump(new_json_data, data_file, indent=4)
                data_file.close()
