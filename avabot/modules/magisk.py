# Magisk Module- Module from AstrakoBot
# Inspired from RaphaelGang's android.py
# By DAvinash97
from requests import get
from telegram import Bot, Update, ParseMode
from telegram.ext import Updater, CommandHandler

from avabot import dispatcher
from avabot.modules.disable import DisableAbleCommandHandler
from asyncio import sleep

link = "https://raw.githubusercontent.com/topjohnwu/magisk_files/"

def magisk(bot,update):
    magisk_dict = {
            "*Stable*": "master/stable.json", "\n"
            "*Beta*": "master/beta.json", "\n"
            "*Canary*": "canary/canary.json",
        }.items()

    releases = '*Latest Magisk Releases:*\n\n'
    for magisk_type, release_url in magisk_dict:
        for Canary in magisk_dict:
            canary = "https://github.com/topjohnwu/magisk_files/raw/canary/"
        data = get(link + release_url).json()
        releases += f'{magisk_type}:\n' \
                    f'》 *Installer* - [{data["magisk"]["version"]} ({data["magisk"]["versionCode"]})]({data["magisk"]["link"]}) \n' \
                    f'》 *Manager* - [{data["app"]["version"]} ({data["app"]["versionCode"]})]({data["app"]["link"]}) \n' \
                    f'》 *Uninstaller* - [Uninstaller {data["magisk"]["version"]} ({data["magisk"]["versionCode"]})]({data["uninstaller"]["link"]}) \n'
    out = bot.send_message(chat_id = update.effective_chat.id,
                             text=releases,
                             parse_mode=ParseMode.MARKDOWN,
                             disable_web_page_preview=True)
__help__ = """
 - /magisk, /su, /root: fetches latest magisk.
"""
magisk_handler = CommandHandler(['magisk', 'root', 'su'], magisk)
dispatcher.add_handler(magisk_handler)

__mod_name__ = "Magisk"
__command_list__ = ["magisk", 'root', 'su']
__handlers__ = [magisk_handler]
