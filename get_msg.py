import imaplib
from time import sleep
from write_message import write_message
from auth import email, password

"""
Receiving messages from the 'inbox' and displaying them
Works only with 'mail.ru'.
If you want to change your mail, write me
"""


def get_msg():
    mail = imaplib.IMAP4_SSL('imap.mail.ru', 993)  # connect to mailbox
    mail.login(email, password)
    mail.list()
    mail.select("inbox")  # Receiving messages
    messages = []  # did it for limit
    while True:
        result, data = mail.search(None, "ALL")
        ids = data[0]
        try:
            id_list = ids.split()[-7:]
        except IndexError:
            id_list = ids.split()
        if messages == id_list:
            continue
        messages = id_list[:]
        print('____________________________')
        for i in id_list:
            result, data = mail.fetch(i, "(RFC822)")
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            print(write_message(raw_email_string))
        sleep(3)


