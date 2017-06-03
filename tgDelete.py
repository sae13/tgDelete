#!/usr/bin/env python3
# coding=utf-8
#فراخوانی پکیج‌هایی که نیاز داریم
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
#هرشخص یه یونیک آی دی داره.یه لیست از مدیران تعریف میکنیم که بدونه اینا مدیرن و مجازن
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

#ارتباتمون رو با تلگرام راه میندازیم و تابعمون فرا میخونیم
def main():
    receiver.start()
    receiver.message(schedulerDeleter(sender))
    receiver.stop()
    print("I am done")
@coroutine
#تابعی که قراره پیاما رو پاک کنه تعریف میکنیم
def schedulerDeleter(sender):
    quit = False
    try:
        while not quit:
			#پیام رو از تلگرام به صورت فایل جیسون میگیره
            msg = (yield)
            #print(msg) we need this for debug maybe
			#وقتی پیامی میاد استاتوس ربات رو آنلاین میکنه
            sender.status_online()
			#خط زیر میگیم اگه اتفاقی ک الان افتاد از نوع پیام هست-مثلا اگه ما رو توی گروهی
			#دعوت میکنن اتفاق خاصی نیفته- اگه از نوع پیام هست بعد این کارا رو بکن
            if msg.event == "message" and not msg.own:
                msgID = msg.id #هرپیام یه آی دی مخصوص به خودش داره
                msgSenderId = msg.sender.id #هرفرستنده یه آی دی مخصوص به خودش داره
                msgTime = localtime(time()) #ساعت لوکال سیستم
                msgHour = int(msgTime[3]) #ما فقط به ساعتش نیاز داریم نه دقیقه
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
#بالا گفتی اگه فرستنده از لیست مدیران نیست و ساعت پیام بین یازده شب تا هفت صبحه
                    if msgSenderId not in SpammerUsers:
                        SpammerUsers.append(msgSenderId)
                        sender.send_msg(msgSenderId, msgToFirst)
                        sender.send_msg(msgSenderId, msgToBtw)
                    sender.fwd(msgSenderId,msgID)
                    sender.message_delete(msgID)
					#به طرف پیامای پیش فرض رو که تعریف کردیم میده بعد پیامی فرستاده
					#بعد پیامی که خودش فرستاده رو به خودش فوروارد میکنه
					#و پیام رو پاک میکنه

                else:
                    continue
            #خط‌های زیر ادامه دستور ترای هست برای وقتایی که دستورات ارضا نمی‌شن و تعریف
			#کلید خروچ

    except GeneratorExit:

        pass
    except KeyboardInterrupt:

        pass
    else:

        pass
#اگه تابع ماین داخل همین صفحه کد تعریف شده اجراش کن
if __name__ == '__main__':
    main()
