#!/usr/bin/env python3
# coding=utf-8
from __future__ import unicode_literals
from pytg import Telegram
tg = Telegram(
	telegram="/home/pi/App/telegram-cli/tg/bin/telegram-cli",
	pubkey_file="/home/pi/App/telegram-cli/tg/tg-server.pub",
    port=8092
    )
inline_image = False
receiver = tg.receiver
sender = tg.sender
from pytg.receiver import Receiver  # get messages
from pytg.sender import Sender  # send messages, and other querys.
from pytg.utils import coroutine
from time import time, localtime
#import logging
#logging.basicConfig(level=logging.DEBUG)
#315156394

__author__ = 'saeb'

ADMIN_IDS =['$0100000084cba20ed401c9a0893540b9']  # you should probably change this.
msgToFirst = "سلام همکار گرامی.\n\
بنا بر قوانین گروه، ارسال پیام از ساعت ۲۳ تا هفت صبح \
ممنوع می‌باشد.\n\
لطفافردا مجدد تلاش کنید.\
باتشکر.\n\
روابط‌عمومی‌مس‌منطقه‌کرمان"
msgToBtw = "ضمنا این ربات آزمایشی می‌باشد\n\
می‌توانیدمشکلات، انتقادات و پیشنهادات خود را در مورد این ربات\
از راه‌های زیر با ما در میان بگذارید:\n\
از طریق تلگرام:\n\
@saeb_m\n\
از طریق آدرس الکترونیکی:\n\
shahrbabak@nicico.com\n\
با چهارشماره ای ۶۳۲۹\n\
با تشکر"

def main():
    receiver.start()
    receiver.message(schedulerDeleter(sender))
    receiver.stop()
    print("I am done")
@coroutine
def schedulerDeleter(sender):
    quit = False
    try:
        while not quit:
            msg = (yield)
            print(msg)
            sender.status_online()
            if msg.event == "message" and not msg.own:
                msgID = msg.id
                msgSenderId = msg.sender.id
                msgTime = localtime(time())
                msgHour = int(msgTime[3])
                print (msgTime)
                print("\n msg time= {}\n msgID = {}\
                msgSenderId = {}".format(msgHour, msgID,\
                msgSenderId))
                #print("\n msg txt = {} \n".format(msg.text))
                if (msg.sender.id not in ADMIN_IDS) and \
                (( msgHour > 22 ) or ( msgHour < 7 )):

                    sender.send_msg(msgSenderId, msgToFirst)
                    sender.send_msg(msgSenderId, msgToBtw)
                    sender.fwd(msgSenderId,msgID)
                    sender.message_delete(msgID)
                    # if 'text' not in msg:
                    #
                    #     sender.fwd_media(msgSenderId,msgID)
                    #     try:
                    #         sender.fwd(msgSenderId,msgID)
                    #     except:
                    #         pass
                    # else:
                        # print(msgID)

                else:
                    continue
            #print(msg)
            # if msg.event != "message":
            #     continue
            # if msg.own:
            #     continue
            # else:
            #     sender.send_msg(msg.peer.cmd, "سلام!")

    except GeneratorExit:

        pass
    except KeyboardInterrupt:

        pass
    else:

        pass

if __name__ == '__main__':
    main()

