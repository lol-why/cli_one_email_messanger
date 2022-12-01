import imaplib
from email.message import Message
from time import time, strftime
from auth import name, email, password

"""
Sending message to your own email


"""


def send_message(text):
    mail = imaplib.IMAP4_SSL('imap.mail.ru', 993)
    mail.login(email, password)
    new_message = Message()
    new_message.set_payload(f'{text} -- {name} {strftime("%X")}')
    mail.append('INBOX', '', imaplib.Time2Internaldate(time()), str(new_message).encode('utf-8'))


while True:
    send_message(input())