import yagmail
password = ""
with open("/home/pi/Desktop/email/.email_password", "r") as pswd:
    password=pswd.read()

yag= yagmail.SMTP("youssefraspitest@gmail.com", password)

yag.send(to='medyousef95@gmail.com',
        subject="1stemail",
        contents="hello from raspi")
print("email sent")
    
