# Magisk Module- Module from AstrakoBot
# Inspired from RaphaelGang's android.py
# By DAvinash97
from requests import get
from telegram import Bot, Update, ParseMode
from telegram.ext import Updater, CommandHandler
from avabot import dispatcher
from avabot.modules.disable import DisableAbleCommandHandler

def magisk(bot,update):
    magisk_dict = {
        "*Stable*":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/master/stable.json",
        "\n"
        "*Beta*":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/master/beta.json",
    }
    releases = '*Latest Magisk Releases:*\n\n'
    for magisk_type, release_url in magisk_dict.items():
        data = get(release_url).json()
        releases += f'{magisk_type}:\n' \
                    f'》 *Installer* - [Zip v{data["magisk"]["version"]}]({data["magisk"]["link"]}) \n' \
                    f'》 *Manager* - [App v{data["app"]["version"]}]({data["app"]["link"]}) \n' \
                    f'》 *Uninstaller* - [Uninstaller v{data["magisk"]["version"]}]({data["uninstaller"]["link"]}) \n'
    bot.send_message(chat_id = update.effective_chat.id,
                             text=releases,
                             parse_mode=ParseMode.MARKDOWN,
                             disable_web_page_preview=True)
                             
magisk_handler = CommandHandler(['magisk', 'root', 'su'], magisk)
dispatcher.add_handler(magisk_handler)

__mod_name__ = "Magisk"
__command_list__ = ["magisk", 'root', 'su']
__handlers__ = [magisk_handler]
