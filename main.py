from get_msg import get_msg
from time import sleep
from write_message import write_message
from os import system

messages = []  # for get_msg
if __name__ == '__main__':
    while True:
        try:
            request = get_msg(messages)
            if request is None:
                sleep(1)
                continue
            else:
                system('cls')
                print('______________________')
                for i in request[0]:
                    print(write_message(i))
                messages = request[1]
                sleep(1)
        except:
            print('______________________')
            sleep(1)

