import asyncio
import os
import sys
import time
import random

from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError, PasswordHashInvalidError, PhoneNumberInvalidError
from telethon.network import ConnectionTcpAbridged
from telethon.utils import get_display_name
from telethon.sessions import StringSession

try:
   import requests
   import bs4
except:
   print("[!] Requests Not found. Loading...")
   print("[!] Bs4 Not found. Loading...")

   if os.name == 'nt':
      os.system("python3.8 -m pip install requests")
      os.system("python3.8 -m pip install bs4")
   else:
      os.system("pip3 install requests")
      os.system("pip3 install bs4")


# Original Source https://github.com/LonamiWebs/Telethon/master/telethon_examples/interactive_telegram_client.py #
loop = asyncio.get_event_loop()

class InteractiveTelegramClient(TelegramClient):
    def __init__(self, session_user_id, api_id, api_hash,
                 telefon=None, proxy=None):
        super().__init__(
            session_user_id, api_id, api_hash,
            connection=ConnectionTcpAbridged,
            proxy=proxy
        )
        self.found_media = {}
        print('Welcome to AsenaUserBot String Receiver')
        print('[i] Connecting to Telegram's Servers...')
        try:
            loop.run_until_complete(self.connect())
        except IOError:
            print('[!] An error occurred while connecting. Trying again...')
            loop.run_until_complete(self.connect())

        if not loop.run_until_complete(self.is_user_authorized()):
            if telefon == None:
               user_phone = input('[?] Your telephone number (Sample: +91xxxxxxxxxx): ')
            else:
               user_phone = telephone
            try:
                loop.run_until_complete(self.sign_in(user_phone))
                self_user = None
            except PhoneNumberInvalidError:
                print("[!] You Have Entered An Invalid Number, Enter As Example. Sample: +91xxxxxxxxxx")
                exit(1)
            except ValueError:
               print("[!] You Have Entered An Invalid Number, Enter As Example. Sample: +91xxxxxxxxxx")
               exit(1)

            while self_user is None:
                code = input('[?] Five From Telegram (5) Enter Digit Code: ')
                try:
                    self_user =\
                        loop.run_until_complete(self.sign_in(code=code))
                except PhoneCodeInvalidError:
                    print("[!] You typed the code incorrectly. Please try again. [Experimenting Causes You to Eat Ban]")
                except SessionPasswordNeededError:
                    pw = input('[i] Two-step verification detected. '
                                 '[?] Enter Your Password: ')
                    try:
                        self_user =\
                            loop.run_until_complete(self.sign_in(password=pw))
                    except PasswordHashInvalidError:
                        print("[!] 2 You Wrote Your Progressive Password Incorrectly. Please Try Again. [Experimenting Causes You to Eat Ban]")


if __name__ == '__main__':
   print("[i] Devil String AS\n@DevilUserBot\n\n")
   print("[1] Automatic API ID/HASH Receiver")
   print("[2] String Receiver\n")
   
   try:
      selection = int(input("[?] Make a selection: "))
   except:
      print("[!] Please Enter Numbers Only!")

   if secim == 2:
      API_ID = input('[?] API ID\'get off [Leave the Ready Keys Blank to Use]: ')
      if API_ID == "":
         print("[i] Using Preset Keys...")
         API_ID = 4
         API_HASH = "014b35b6184100b085b0d0572f9b5103"
      else:
         API_HASH = input('[?] API HASH\'iniz: ')

      client = InteractiveTelegramClient(StringSession(), API_ID, API_HASH)
      print("[i] String Your Key Is Below!\n\n\n" + client.session.save())
    secim = 1:
      numara = input("[?] Your telephone number: ")
      try:
         rastgele = requests.post("https://my.telegram.org/auth/send_password", data={"phone": numara}).json()["random_hash"]
      except:
         print("[!]Failed to Send Code. Check Your Phone Number.")
         exit(1)
      
      sifre = input("[?] Write the Code From Telegram: ")
      try:
         cookie = requests.post("https://my.telegram.org/auth/login", data={"phone": numara, "random_hash": rastgele, "password": sifre}).cookies.get_dict()
      except:
         print("[!] Probability You Spelled The Code Incorrectly. Please Restart the Script.")
         exit(1)
      app = requests.post("https://my.telegram.org/apps", cookies=cookie).text
      soup = bs4.BeautifulSoup(app, features="html.parser")

      if soup.title.string == "Create new application":
         print("[i] You Have No App. Creating...")
         hashh = soup.find("input", {"name": "hash"}).get("value")
         AppInfo = {
            "hash": hashh,
            "app_title":"Devil UserBot",
            "app_shortname": "Devilian" + str(random.randint(9, 99)) + str(time.time()).replace(".", ""),
            "app_url": "",
            "app_platform": "android",
            "app_desc": ""
         }
         app = requests.post("https://my.telegram.org/apps/create", data=AppInfo, cookies=cookie).text
         print(app)
         print("[i] The application was created successfully!")
         print("[i] API ID/HASH getting...")
         newapp = requests.get("https://my.telegram.org/apps", cookies=cookie).text
         newsoup = bs4.BeautifulSoup(newapp, features="html.parser")

         g_inputs = newsoup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
         app_id = g_inputs[0].string
         api_hash = g_inputs[1].string
         print("[i] Information Brought! Please Note These.\n\n")
         print(f"[i] API ID: {app_id}")
         print(f"[i] API HASH: {api_hash}")
         try:
            stringonay = int(input("[?] String Almak İster Misiniz? [Evet için 1 Yazınız]: "))
         except:
            print("[!] Please Enter Only Number!")

         if stringonay == 1:
            client = InteractiveTelegramClient(StringSession(), app_id, api_hash, numara)
            print("[i] String Your Key Is Below!\n\n\n" + client.session.save())
         else:
            print("[i] Script Stopping...")
            exit(1)
      elif  soup.title.string == "App configuration":
         print("[i] You Have Already Created an Application. API ID/HASH Withdrawing...")
         g_inputs = soup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
         app_id = g_inputs[0].string
         api_hash = g_inputs[1].string
         print("[i] Information Brought! Please Note These.\n\n")
         print(f"[i] API ID: {app_id}")
         print(f"[i] API HASH: {api_hash}")
         try:
            stringonay = int(input("[?] Would You Like To Buy A String? [Write 1 for Yes]: "))
         except:
            print("[!] Please Enter Only Number!")

         if stringonay == 1:
            client = InteractiveTelegramClient(StringSession(), app_id, api_hash, numara)
            print("[i] String Your Key Is Below!\n\n\n" + client.session.save())
         else:
            print("[i] Script Stopping...")
            exit(1)
      else:
         print("[!] Something went wrong.")
         exit(1)
   else:
      print("[!] Unknown choice.")
