#  SMTP - Simple mail transfer protocol

import smtplib
import random
import datetime
import pathlib
import pandas

my_email = ""
my_pass = ""


class SMTPMail:

    def __init__(self):
        self.connection = smtplib.SMTP("smtp.gmail.com")
        self.connection.starttls()

    def login(self, user: str, password: str) -> None:
        self.connection.login(user=user, password=password)

    def send_email(self, from_address: str, to_address: str, mail_text: str) -> bool:
        try:
            self.connection.sendmail(from_addr=from_address, to_addrs=to_address, msg=mail_text)
            return True
        except Exception as e:
            print(str(e))
            return False


if __name__ == '__main__':
    smtp = SMTPMail()
    path_to_letter = pathlib.Path.joinpath(pathlib.Path("./static_files/letter_templates/"),
                                           f"letter_{random.randint(1, 3)}.txt")
    path_to_csv = pathlib.Path("./static_files/birthdays.csv")
    with open(path_to_letter) as o:
        c1 = o.read()
    birthday_dates = pandas.read_csv(path_to_csv)
    x = birthday_dates[(birthday_dates.month == datetime.datetime.now().month) &
                       (birthday_dates.day == datetime.datetime.now().day)]
    with smtp.connection:
        smtp.login(user=my_email, password=my_pass)
        for index, row in x.iterrows():
            mail_msg = c1.replace("[NAME]", row["name"])
            res = smtp.send_email(my_email, row["email"], f"Subject:Congrats\n\n{mail_msg}")
