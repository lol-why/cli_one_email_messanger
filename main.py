from get_msg import get_msg
from time import sleep

if __name__ == '__main__':
    while True:
        try:
            get_msg()
        except:
            print('______________________')
            sleep(3)

