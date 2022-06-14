import sys
sys.path.append("/Users/nicholask/Desktop/Personal Projects")

import datetime
import os
import time
from threading import Thread

'''
    Format is as follows:
    {Name/Group Name : [sending_id, message]}

    for individuals, sending_id is their number
    for groups, it will be the internal chat guid which could be found
                by searching through the chat.db, located in 
                ~/Library/Messsages/chat.db

    this small file is kept out of the scope of what is seen on github
'''
from secret import contacts

## if group, set to 1, else set to 0
def send_message(number, msg, group):
    while True:
        curr = datetime.datetime.now().strftime("%H:%M:%S")
        h, m , s = curr.split(":")
        if (h == "08" and m == "00" and s == "00"):
            if group == 0:
                os.system('osascript sendMessage.applescript {} "{}"'.format(number, msg))
            else:
                os.system('osascript sendGroupMessage.applescript {} "{}"'.format(number, msg))
            time.sleep(1)
    


## send messages in a multithreaded manner
thread_julie = Thread(target=send_message, args=(contacts["Julie"][0], contacts["Julie"][1], 0))
thread_10_mornings = Thread(target=send_message, args=(contacts["$10 mornings"][0], contacts["$10 mornings"][1], 1))

# ## starting threads 
thread_julie.start()
thread_10_mornings.start()

# ## joining threads
thread_julie.join()
thread_10_mornings.join()


##personal setup for testing
# thread_myself = Thread(target=send_message, args=(contacts["Myself"][0], contacts["Myself"][1], 0))
# thread_myself.start()
# thread_myself.join()


#send_message_by_number(contacts["Myself"][0], contacts["Myself"][1])
