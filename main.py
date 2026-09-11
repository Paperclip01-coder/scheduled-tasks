##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import random
import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
day = now.day
month = now.month
weekday = now.weekday()

letter_list = ["letter_1.txt","letter_2.txt","letter_3.txt"]

df = pandas.read_csv("birthdays.csv")
birthday_dict = df.to_dict(orient="records")

for data in birthday_dict:
    if data["month"] == month and data["day"] == day and data["email"] == "AKUN_UTAMA":
        data["email"] = MY_EMAIL
        chosen_file = random.choice(letter_list)
        file_path = f"letter_templates/{chosen_file}"

        with open(file_path,"r") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", data["name"])

        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=data["email"],
                msg=f"Subject:Happy Birthday\n\n{letter}"
            )
