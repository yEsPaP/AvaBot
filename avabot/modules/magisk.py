# Copyright (C) 2020 - 2020 KassemSYR. All rights reserved.
# This file was part of Galaxy Helper bot.

from requests import get
from telegram import Bot, Update, ParseMode
from telegram.ext import run_async
from avabot import dispatcher
from avabot.modules.disable import DisableAbleCommandHandler

@run_async
def magisk(bot, update):
    url = 'https://raw.githubusercontent.com/topjohnwu/magisk_files/'
    releases = "*Latest Magisk Releases: *\n"
    for magisk_type, path  in {"*Stable*":"master/stable", "*Beta*":"master/beta", "*Canary (debug)*":"canary/debug"}.items():
        data = get(url + path + '.json').json()
        releases += f'{magisk_type}:\n' \
                f'》Installer - [Zip v{data["magisk"]["version"]}]({data["magisk"]["link"]}) \n' \
                f'》Manager - [App v{data["app"]["version"]}]({data["app"]["link"]}) \n' \
                f'》Uninstaller - [Uninstaller v{data["magisk"]["version"]}]({data["uninstaller"]["link"]}) \n'
    bot.send_message(
    chat_id=update.effective_message.chat_id,
    text=releases,
    parse_mode=ParseMode.MARKDOWN,
    disable_web_page_preview=True
    )

MAGISK_HANDLER = DisableAbleCommandHandler("Magisk", magisk)
dispatcher.add_handler(MAGISK_HANDLER)

__mod_name__ = "Magisk"
__command_list__ = ["magisk"]
__handlers__ = [MAGISK_HANDLER]
