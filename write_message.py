def write_message(all_info):
    message = all_info.split('X-Mailru-Intl-Transport')[1].split()[2:]
    message_text = ' '.join(message[:message.index('--')])
    sender = message[-2]
    time_mess = message[-1]
    return f'{sender} [{time_mess}]  |  {message_text}'


