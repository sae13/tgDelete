#!/usr/bin/env python3
# coding=utf-8
from pytg import Telegram
tg = Telegram(
		telegram="path/to/to/bin/telegram-cli",
		pubkey_file="/path/to/telegram-cli/tg-server.pub1",
	    port=8092
	    )
