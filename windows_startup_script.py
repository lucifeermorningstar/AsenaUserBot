from telethon import TelegramClient
API_KEY="Write this here"
API_HASH="Write this here"
#my.telegram.org get it from
bot = TelegramClient('userbot',API_KEY,API_HASH)
bot.start()

#This script won't run your bot, it just creates a session.
