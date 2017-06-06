#!/usr/bin/env python3
# coding=utf-8
from __future__ import unicode_literals
from pytg.receiver import Receiver  # get messages
from pytg.sender import Sender  # send messages, and other querys.
from pytg.utils import coroutine
from time import time, localtime
#قسمت زیر ارتباطمون رو با تلگرام تحت کلای تعریف میکنیم که وصل بشه به تلگراممون
from telegramCliConf import tg
tg = tg
inline_image = False
receiver = tg.receiver
sender = tg.sender
__author__ = 'saeb'
ADMIN_IDS =['$0100000084cba20ed401c9a0893540b90']  # you should probably change this.
SpammerUsers=[]
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
            #print(msg) we need this for debug maybe
            sender.status_online()
            if msg.event == "message" and not msg.own:
                msgID = msg.id
                msgSenderId = msg.sender.id
                msgTime = localtime(time())
                msgHour = int(msgTime[3])ه
                #print (msgTime) for debug
                # print("\n msg time= {}\n msgID = {}\
                # msgSenderId = {}".format(msgHour, msgID,\
                # msgSenderId))
                #print("\n msg txt = {} \n".format(msg.text))
                dbTextFile = open("dbTextFile.text","a")
                dbTextFile.write("\n\n\n\n\n{}".format(msg))
                dbTextFile.close
                print("msg peer id:{}\n".format(msg.peer.peer_id))
                #sender.send_msg(msg.sender.cmd,"hi")
                if (msg.sender.id not in ADMIN_IDS) and \
                (( msgHour > 0 ) or ( msgHour < 7 )):
                    if msgSenderId not in SpammerUsers:
                        SpammerUsers.append(msgSenderId)
                        sender.send_msg(msgSenderId, msgToFirst)
                        sender.send_msg(msgSenderId, msgToBtw)
                    sender.fwd(msgSenderId,msgID)
                    sender.message_delete(msgID)

                else:
                    continue

    except GeneratorExit:

        pass
    except KeyboardInterrupt:

        pass
    else:

        pass
if __name__ == '__main__':
    main()
