import imaplib
from auth import email, password

"""
Receiving messages from the 'inbox' and displaying them
Works only with 'mail.ru'.
If you want to change your mail, write me
"""


def get_msg(messages):  # messages for limit -> list with ids
    mail = imaplib.IMAP4_SSL('imap.mail.ru', 993)  # connect to mailbox
    mail.login(email, password)
    mail.list()
    mail.select("inbox")  # Receiving messages
    result, data = mail.search(None, "ALL")
    ids = data[0]
    try:
        id_list = ids.split()[-12:]
    except IndexError: # if you have less, than 12 messages
        id_list = ids.split()
    if messages == id_list:  # check ID of messages
        return
    messages = id_list[:]
    message_texts = []
    for i in id_list:
        result, data = mail.fetch(i, "(RFC822)")
        raw_email = data[0][1]
        message_texts.append(raw_email.decode('utf-8'))
    return message_texts, messages


