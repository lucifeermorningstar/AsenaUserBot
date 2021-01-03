# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Devil UserBot - Devil

""" UserBot Starting Point"""
import importlib
from importlib import import_module
from sqlite3 import connect
import os
import requests
from telethon.tl.types import InputMessagesFilterDocument
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.tl.functions.channels import GetMessagesRequest
from . import BRAIN_CHECKER, LOGS, bot, PLUGIN_CHANNEL_ID, CMD_HELP, LANGUAGE, ASENA_VERSION, PATTERNS
from .modules import ALL_MODULES
import userbot.modules.sql_helper.mesaj_sql as MSJ_SQL
import userbot.modules.sql_helper.galeri_sql as GALERI_SQL
from pySmartDL import SmartDL
from telethon.tl import functions

from random import choice
import chromedriver_autoinstaller
from json import loads, JSONDecodeError
import re
import userbot.cmdhelp

DIZCILIK_STR = [
    "I'm straightening the sticker ... ",
    "Long live ordering ...",
    "I invite this sticker to my package ...",
    "I have to fix this ...",
    "Hey, this is a nice sticker!
    "I'm flattening your sticker \ nhahaha.",
    "Hey look over there. (☉｡☉)! → \ n While I was editing this ...",
    "Roses red violets blue, I'll be cool by putting this sticker on my pack ...",
    "Sticker is imprisoned ...",
    "Mister stunner wonders this sticker... ",
]

AFKSTR = [

हिंदी में खोजें
ट्रांसलेट


Turkish
English
"Şu an acele işim var, daha sonra mesaj atsan olmaz mı? Zaten yine geleceğim.",
    "Aradığınız kişi şu anda telefona cevap veremiyor. Sinyal sesinden sonra kendi tarifeniz üzerinden mesajınızı bırakabilirsiniz. Mesaj ücreti 49 kuruştur. \n`biiiiiiiiiiiiiiiiiiiiiiiiiiiiip`!",
    "Birkaç dakika içinde geleceğim. Fakat gelmezsem...\ndaha fazla bekle.",
    "Şu an burada değilim, muhtemelen başka bir yerdeyim.",
    "Güller kırmızı\nMenekşeler mavi\nBana bir mesaj bırak\nVe sana döneceğim.",
    "Bazen hayattaki en iyi şeyler beklemeye değer…\nHemen dönerim.",
    "Hemen dönerim,\nama eğer geri dönmezsem,\ndaha sonra dönerim.",
    "Henüz anlamadıysan,\nburada değilim.",
    "Merhaba, uzak mesajıma hoş geldiniz, bugün sizi nasıl görmezden gelebilirim?",
    "7 deniz ve 7 ülkeden uzaktayım,\n7 su ve 7 kıta,\n7 dağ ve 7 tepe,\n7 ovala ve 7 höyük,\n7 havuz ve 7 göl,\n7 bahar ve 7 çayır,\n7 şehir ve 7 mahalle,\n7 blok ve 7 ev...\n\nMesajların bile bana ulaşamayacağı bir yer!",
    "Şu anda klavyeden uzaktayım, ama ekranınızda yeterince yüksek sesle çığlık atarsanız, sizi duyabilirim.",
    "Şu yönde ilerliyorum\n---->",
    "Şu yönde ilerliyorum\n<----",
    "Lütfen mesaj bırakın ve beni zaten olduğumdan daha önemli hissettirin.",
    "Sahibim burada değil, bu yüzden bana yazmayı bırak.",
    "Burada olsaydım,\nSana nerede olduğumu söylerdim.\n\nAma ben değilim,\ngeri döndüğümde bana sor...",
    "Uzaklardayım!\nNe zaman dönerim bilmiyorum !\nUmarım birkaç dakika sonra!",
    "Sahibim şuan da müsait değil. Adınızı, numarınızı ve adresinizi verirseniz ona iletibilirm ve böylelikle geri döndüğü zaman.",
    "Üzgünüm, sahibim burada değil.\nO gelene kadar benimle konuşabilirsiniz.\nSahibim size sonra döner.",
    "Bahse girerim bir mesaj bekliyordun!",
    "Hayat çok kısa, yapacak çok şey var...\nOnlardan birini yapıyorum...",
    "Şu an burada değilim....\nama öyleysem ...\n\nbu harika olmaz mıydı?",
]
"I'm in a rush right now, can't you send me a message later? I'll be back anyway.",
    "The person you are calling cannot answer the phone right now. You can leave your message on your own tariff after the tone. The message costs 49 kurus. \ N`biiiiiiiiiiiiiiiiiiiiiiiiiiip`!",
    "I'll be back in a few minutes. But if I don't ... wait longer.",
    "I'm not here right now, I'm probably somewhere else.",
    "Roses are red \ nOns are blue \ nLeave me a message \ nAnd I'll get back to you.",
    "Sometimes the best things in life are worth the wait… \ nI'll be right back.",
    "I'll be right back, but if I don't come back, I'll be back later.",
    "If you don't get it yet, I'm not here.",
    "Hello, welcome to my distant message, how can I ignore you today?",
    "I am away from 7 seas and 7 countries, \ n7 water and 7 continents, \ n7 mountains and 7 hills, \ n7 plains and 7 mounds, \ n7 pools and 7 lakes, \ n7 spring and 7 meadows, \ n7 cities and 7 neighborhoods, \ n7 blocks and 7 houses ... \ n \ nA place where even messages can't reach me! ",
    "I'm away from the keyboard right now, but if you scream loud enough on your screen, I can hear you.",
    "I'm moving in the following direction \ n ---->",
    "I'm moving in this direction \ n <----",
    "Please leave a message and make me feel more important than I already am.",
    "My owner is not here, so stop writing to me.",
    "If I were here, \ nI would tell you where I am. \ N \ nBut it's not me, \ when I come back ask me ...",
    "I'm away! \ NI don't know when I'll be back! \ NI hope a few minutes later!",
    "My owner is not available at the moment. If you give your name, number and address, I can send it to him and so when he returns.",
    "Sorry, my owner is not here. You can talk to me until he arrives. \ NThe owner will return to you later.",
    "I bet you were expecting a message!",
    "Life is too short, there are so many things to do ... \ nI am doing one of them ...",
    "I'm not here right now .... \ n but if I am ... \ n \ n wouldn't that be great?",
]

UNAPPROVED_MSG = ("`Hey,` {mention}`! This is a Devil Userbot. Do not worry.\n\n`"
                  "`My owner didn't give you permission to PM so get lost Or ja ke gand marwa. `"
                  "`Please wait for my owner to be active, she will usually confirm PMs.\n\n`"
                  "`As far as I know My Master doesn't allow people to PM.`")

DB = connect("learning-data-root.check")
CURSOR = DB.cursor()
CURSOR.execute("""SELECT * FROM BRAIN1""")
ALL_ROWS = CURSOR.fetchall()
INVALID_PH = '\nHATA: The phone number entered is invalid' \
             '\n  Ipucu: Enter your number using your country code' \
             '\n       Check your phone number again'

for i in ALL_ROWS:
    BRAIN_CHECKER.append(i[0])
connect("learning-data-root.check").close()

def extractCommands(file):
    FileRead = open(file, 'r').read()
    
    if '/' in file:
        file = file.split('/')[-1]

    Pattern = re.findall(r"@register\(.*pattern=(r|)\"(.*)\".*\)", FileRead)
    Komutlar = []

    if re.search(r'CmdHelp\(.*\)', FileRead):
        pass
    else:
        dosyaAdi = file.replace('.py', '')
        CmdHelp = userbot.cmdhelp.CmdHelp(dosyaAdi, False)

        # Komutları Alıyoruz #
        for Command in Pattern:
            Command = Command[1]
            if Command == '' or len(Command) <= 1:
                continue
            Komut = re.findall("(^.*[a-zA-Z0-9şğüöçı]\w)", Command)
            if (len(Komut) >= 1) and (not Komut[0] == ''):
                Komut = Komut[0]
                if Komut[0] == '^':
                    KomutStr = Komut[1:]
                    if KomutStr[0] == '.':
                        KomutStr = KomutStr[1:]
                    Komutlar.append(KomutStr)
                else:
                    if Command[0] == '^':
                        KomutStr = Command[1:]
                        if KomutStr[0] == '.':
                            KomutStr = KomutStr[1:]
                        else:
                            KomutStr = Command
                        Komutlar.append(KomutStr)

            # DevilPY
            Devilpy = re.search('\"\"\"DEVILPY(.*)\"\"\"', FileRead, re.DOTALL)
            if not Devilpy == None:
                Devilpy = Devilpy.group(0)
                for Satir in Devilpy.splitlines():
                    if (not '"""' in Satir) and (':' in Satir):
                        Satir = Satir.split(':')
                        Isim = Satir[0]
                        Deger = Satir[1][1:]
                                
                        if Isim == 'INFO':
                            CmdHelp.add_info(Deger)
                        elif Isim == 'WARN':
                            CmdHelp.add_warning(Deger)
                        else:
                            CmdHelp.set_file_info(Isim, Deger)
            for Komut in Komutlar:
                # if re.search('\[(\w*)\]', Komut):
                    # Komut = re.sub('(?<=\[.)[A-Za-z0-9_]*\]', '', Komut).replace('[', '')
                CmdHelp.add_command(Komut, None, 'This plugin has been installed externally. No description is defined.')
            CmdHelp.add()

try:
    bot.start()
    idim = bot.get_me().id
    Devilbl = requests.get('https://gitlab.com/Quiec/asen/-/raw/master/asen.json').json()
    if idim in asenabl:
        bot.disconnect()

    # Let's Set Up ChromeDriver #
    try:
        chromedriver_autoinstaller.install()
    except:
        pass
    
    # Values ​​for the gallery
    GALERI = {}

    # WE ADJUST THE PLUGIN MESSAGES
    PLUGIN_MESSAGES = {}
    ORJ_PLUGIN_MESAJLAR = {"alive": "`Devil Zinda hai so Devil Userbot is working.`", "afk": f"`{str(choice(AFKSTR))}`", "kickme": "`i am going to leave this chutiya group`🤠", "pm": UNAPPROVED_MSG, "da": str(choice(DIZCILIK_STR)), "ban": "{mention}`, Prohibited! By Devil Userbot`", "mute": "{mention}`, eske muh me dal diya aabh nhi bolega yeh bsdk!`", "approve": "{mention}`, you can send me a message!`", "disapprove": "{mention}`, you can no longer send me a message bcuz you are chutiya abh nikal ja and gand marwa!`", "block": "{mention}`, you are blocked bcuz teri gand pad gye a mre fuck se!`"}

    PLUGIN_MESAJLAR_TURLER = ["alive", "afk", "kickme", "pm", "da", "ban", "mute", "approve", "disapprove", "block"]
    for mesaj in PLUGIN_MESAJLAR_TURLER:
        dmsj = MSJ_SQL.getir_mesaj(mesaj)
        if dmsj == False:
            PLUGIN_MESAJLAR[mesaj] = ORJ_PLUGIN_MESAJLAR[mesaj]
        else:
            if dmsj.startswith("MEDIA_"):
                media = int(dmsj.split("MEDIA_")[1])
                media = bot.get_messages(PLUGIN_CHANNEL_ID, ids=media)

                PLUGIN_MESAJLAR[mesaj] = media
            else:
                PLUGIN_MESAJLAR[mesaj] = dmsj
    if not PLUGIN_CHANNEL_ID == None:
        LOGS.info("Plugins Loading")
        try:
            KanalId = bot.get_entity(PLUGIN_CHANNEL_ID)
        except:
            KanalId = "me"

        for plugin in bot.iter_messages(KanalId, filter=InputMessagesFilterDocument):
            if plugin.file.name and (len(plugin.file.name.split('.')) > 1) \
                and plugin.file.name.split('.')[-1] == 'py':
                Split = plugin.file.name.split('.')

                if not os.path.exists("./userbot/modules/" + plugin.file.name):
                    dosya = bot.download_media(plugin, "./userbot/modules/")
                else:
                    LOGS.info("Bu Plugin Zaten Yüklü " + plugin.file.name)
                    extractCommands('./userbot/modules/' + plugin.file.name)
                    dosya = plugin.file.name
                    continue 
                
                try:
                    spec = importlib.util.spec_from_file_location("userbot.modules." + Split[0], dosya)
                    mod = importlib.util.module_from_spec(spec)

                    spec.loader.exec_module(mod)
                except Exception as e:
                    LOGS.info(f"`Upload failed! Plugin is incorrect.\n\nHata: {e}`")

                    try:
                        plugin.delete()
                    except:
                        pass

                    if os.path.exists("./userbot/modules/" + plugin.file.name):
                        os.remove("./userbot/modules/" + plugin.file.name)
                    continue
                extractCommands('./userbot/modules/' + plugin.file.name)
    else:
        bot.send_message("me", f '' Please make sure that plugins are permanent. PLUGIN_CHANNEL_ID'i ayarlayın.`")
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

async def FotoDegistir (foto):
    FOTOURL = GALERI_SQL.TUM_GALERI[foto].foto
    r = requests.get(FOTOURL)

    with open(str(foto) + ".jpg", 'wb') as f:
        f.write(r.content)    
    file = await bot.upload_file(str(foto) + ".jpg")
    try:
        await bot(functions.photos.UploadProfilePhotoRequest(
            file
        ))
        return True
    except:
        return False

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info("Your bot is running! Test it by typing .alive in any chat. "
          "If you need help, come to our Support group and abh nacchoo bhencho t.me/deviluserbot")
LOGS.info(f"Bot sürümünüz: Devil {DEVIL_AS_VERSION}")

"""
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
"""
bot.run_until_disconnected()
