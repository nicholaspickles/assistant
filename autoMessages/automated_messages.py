import sys
sys.path.append("/Users/nicholask/Desktop/Personal Projects")

import datetime
import os
import time
from threading import Thread

import random

stupid = ["yo momma", "Do you like wendy's? cuz u wud luv when deez nutz r in ur face!!", "It's not about what you've done, but what you do with what you've done... for others. Thank you"
,"Life is a highway, I wanna ride it all night long", "Drop it to the floor make that ass shake, make that ground move, that's an ASS QUAKE!!", "Stacy's mom has got it going on", "You should give kong $10 to show him how much you love him.",
"don't buy cryptocurrency", "call your mom, tell her that you love her."]
love = ["Your face, I like that shit.", "Damn, can I hold that hand?", "i miss u", "you're doing great today", "just look how far you've come", "It doesn't matter who you are or what you look like, so long as somebody loves you.",
"We are never so defenseless against suffering as when we love.", ]
inspirational = ["When times are rough and the day seems dark, just remember that the sun will set, and light will rise again, and then begins a new day with better opportunities.", 
"Even when you're not ready for the day, it cannot always be night.", "For me, skinny is a style of jeans, not a goal", "I love it when people underestimate me, and then become pleasantly surprised.",
"Shoot for the moon, and even if you miss, you land amongst the stars.", "It takes 20 years to build a reputation and five minutes to ruin it. If you think about that, you'll do things differently.",
"If you love life, don't waste time, for time is what life is made up of.", "\"It doesn't interest me \nwhat you do for a living.\nI want to know\nwhat you ache for\nand if you dare to dream\nof meeting your heart's longing.\"\n-Oriah Mountain Dreamer"]
quotes = [stupid, love, inspirational]


def generate_quote():
    toUse = quotes[random.randint(0, len(quotes) - 1)]
    rand_idx = random.randint(0, len(toUse) - 1)
    qotd = toUse[rand_idx]
    return qotd

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
                os.system('osascript sendMessage.applescript {} "{}\n\"{}\""'.format(number, msg, generate_quote()))
            else:
                os.system('osascript sendGroupMessage.applescript {} "{}\n\"{}\""'.format(number, msg, generate_quote()))
            time.sleep(1)
    


## send messages in a multithreaded manner
thread_julie = Thread(target=send_message, args=(contacts["Julie"][0], contacts["Julie"][1], 0))
thread_10_mornings = Thread(target=send_message, args=(contacts["$10 mornings"][0], contacts["$10 mornings"][1], 1))
thread_thicc_ass_fam = Thread(target=send_message, args=(contacts["thicc ass fam"][0], contacts["thicc ass fam"][1], 1))
thread_jun = Thread(target=send_message, args=(contacts["Jun"][0], contacts["Jun"][1], 0))

# # ## starting threads 
thread_julie.start()
thread_10_mornings.start()
thread_thicc_ass_fam.start()
thread_jun.start()

# # ## joining threads
thread_julie.join()
thread_10_mornings.join()
thread_thicc_ass_fam.join()
thread_jun.join()


##personal setup for testing
# thread_myself = Thread(target=send_message, args=(contacts["Myself"][0], contacts["Myself"][1], 0))
# thread_myself.start()
# thread_myself.join()


#send_message_by_number(contacts["Myself"][0], contacts["Myself"][1])
