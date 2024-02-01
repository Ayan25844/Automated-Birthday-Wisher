
import datetime as dt
import pandas, random,smtplib

now=dt.datetime.now()
today=(now.month,now.day)

password="nwzssbrfklklzqnv"
my_email="ayan25844@gmail.com"

df=pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for _, data_row in df.iterrows()}

if today in birthdays_dict:
    
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        letter=letter_file.read()
        letter=letter.replace("[NAME]",birthdays_dict[today].get("name"))

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=birthdays_dict[today].get("email"),msg=f"subject:Happy Birthday\n\n{letter}")  