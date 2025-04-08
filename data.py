# imports pandas and uuid
import pandas as pd
import uuid
import json

customer_id = str(uuid.uuid4())
print("Generated Customer ID:", customer_id)

# loads json data and sets up related variables
with open("new_user_data.json", 'r') as file:
    loaded_data = json.load(file)
nameF = loaded_data.get("firstName")
nameL = loaded_data.get("lastName")
email = loaded_data.get("email")
password = loaded_data.get("password")
price = loaded_data.get("price")

# reads pre existing CSV file into dataframe
#existingUsers = pd.read_csv('user_data.csv')

#nameF = input("Enter first name: ")
#nameL = input("Enter last name: ")
#email = input("Enter email: ")
#password = input("Enter password: ")


# dishes = None

# newDishes = input("Do you want to add any prefered dishes? (Y/N): ")

# if newDishes.lower() == "y" or newDishes.lower == "yes":

#     dishes = input("Enter a dish: ")

#     i = False
#     while i == False:
#         newDishes = input('Enter more dishes, or "-1" to stop: ')
#         if newDishes == "-1":
#             break

#         dishes = dishes + "," + newDishes


# price = int(input("Enter the maximum budget you have to work with daily for a single food: "))

data = {

    'UserID': [customer_id],
    'First Name': [nameF],
    'Last Name': [nameL],
    'Email': [email],
    'Password': [password],
    'Price Range': [price]
}

df = pd.DataFrame(data)


print(df)

# new_data = {'UserID': 'value1', 'First Name': nameF, 'Last Name': nameL, 'Email': email}

df.to_csv('user_data.csv', mode='a', index=False, header=False)
