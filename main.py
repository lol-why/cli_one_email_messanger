from get_msg import get_msg
from time import sleep
from write_message import write_message

messages = []  # for get_msg
if __name__ == '__main__':
    while True:
        try:
            request = get_msg(messages)
            if request is None:
                sleep(3)
                continue
            else:
                print('______________________')
                for i in request[0]:
                    print(write_message(i))
                messages = request[1]
                sleep(3)
        except:
            print('______________________')
            sleep(3)

