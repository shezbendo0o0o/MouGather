# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <shizbendo@gmail.com>
# License: GNU General Public License v3.0

import os
import random
from Core.Support import Font
from Core.Support import Clear
from Core import Searcher
from Core import config
from Core import Searcher_phone
from Core import Searcher_website
from Core import Searcher_person
from Core.Support import DateFormat
from Core import Port_Scanner
from Core import E_Mail
from Core import Update
from Core import Dork
from Core import Decoder
from Core import PDF_Converter as Pdf
from Core import Transfer
from Core import Session
from Core.Support import Database
from Core.Support import Agree
from Core.Support import Language
from datetime import datetime


class Main:

    @staticmethod
    def Checker():
        if os.path.exists("Configuration/Agreement.txt"):
            pass
        else:
            Agree.One_time.Agreement()

    @staticmethod
    def banner():
        Clear.Screen.Clear()
        f = open("Version/Version.txt", "r", newline=None)
        for line in f:
            r = line.replace("\n", "")
        version = f.read() + r
        f.close()
        Quotes = ["Quotes1.txt", "Quotes4.txt", "Quotes3.txt", "Quotes7.txt",
                  "Quotes6.txt", "Quotes2.txt", "Quotes5.txt", "Quotes8.txt",
                  "Quotes9.txt", "Quotes10.txt", "Quotes11.txt", "Quotes12.txt",
                  "Quotes13.txt", "Quotes14.txt", "Quotes15.txt", "Quotes16.txt",
                  "Quotes17.txt", "Quotes18.txt", "Quotes19.txt", "Quotes20.txt"]
        choice = random.choice(Quotes)
        f = open("Quotes/" + choice, "r", newline=None)
        text = f.read()
        f.close() 
        now = datetime.now()
        dataformat = DateFormat.Get.Format2()
        dt_string = now.strftime(dataformat)
        Date1 = str(dt_string)
        Country = DateFormat.Get.Continent()
        Lang = Language.Translation.Get_Language2()
        u = "|" + "MOUGATHER".center(67) + "|"
        print(Font.Color.WHITE +
              "---------------------------------------------------------------------")
        print(Font.Color.WHITE + u)
        def box_line(content="", color=Font.Color.WHITE):
            inner_width = 67
            content = str(content)[:inner_width]
            return color + "|" + content.ljust(inner_width) + Font.Color.WHITE + "|"

        def info_line(label, value, label_color=Font.Color.WHITE):
            inner_width = 67
            value = str(value)
            visible_text = label + value
            spaces = " " * max(0, inner_width - len(visible_text))
            return label_color + "|" + label + Font.Color.GREEN + value + Font.Color.WHITE + spaces + "|"

        clean_version = str(version).strip(" -")
        RED_TEXT = "\033[31m"

        print(Font.Color.WHITE + text.rstrip("\n"))
        print(box_line(""))
        print(box_line("A COMPLETE CYBER OSINT TOOLKIT".center(67), Font.Color.GREEN))
        print(box_line("CODED BY MOAMEN ALSAYED".center(67), RED_TEXT))
        print(box_line(""))
        print(info_line("VERSION      : ", clean_version, Font.Color.YELLOW))
        print(info_line("CURRENT DATE : ", Date1))
        print(info_line("DATE FORMAT  : ", Country))
        print(info_line("CLI LANGUAGE : ", Lang))
        print(Font.Color.WHITE +
              "---------------------------------------------------------------------")

    @staticmethod
    def Mobile_Banner():
        Clear.Screen.Clear()
        f = open("Version/Version.txt", "r", newline=None)
        for line in f:
            r = line.replace("\n", "")
        version = f.read() + r
        f.close()
        list = ["Banners/Banner2.txt", "Banners/Banner4.txt"]
        file_banner = random.choice(list)
        f = open(file_banner, "r", newline=None)
        text = f.read()
        f.close()
        print(Font.Color.GREEN + text)
        print(Font.Color.WHITE + "A COMPLETE OSINT TOOL:)      " +
              Font.Color.BANNER + "CODED BY MOAMEN ALSAYED" + Font.Color.RESET)
        print(Font.Color.WHITE + "\n[+]" +
              Font.Color.GREEN + "VERSION:" + version)
        print(
            Font.Color.YELLOW + "")

    @staticmethod
    def main(Mode):
        while True:
            try:
                Main.Checker()
                filename = Language.Translation.Get_Language()
                filename
                if Mode == "Desktop":
                    Main.banner()
                    option = Language.Translation.Translate_Language(
                        filename, "Main", "Options", "None")
                    Text = Language.Translation.Translate_Language(
                        filename, "Main", "Text", "None")
                else:
                    Main.Mobile_Banner()
                    option = Language.Translation.Translate_Language(
                        filename, "Main", "MobileOptions", "None")
                    Text = Language.Translation.Translate_Language(
                        filename, "Main", "MobileText", "None")
                options = str(option)
                print(Font.Color.GREEN + Text)
                print(Font.Color.WHITE + options)
                sce = int(input(Font.Color.GREEN +
                          "\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                if (sce == 1):
                    print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                          Language.Translation.Translate_Language(filename, "Main", "Alert", "None"))
                    username = str(input(
                        Font.Color.BLUE + "\n[+]" + Font.Color.WHITE +
                        Language.Translation.Translate_Language(filename, "Main", "Username", "None") + Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    while username == "":
                        username = str(input(
                            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Username", "None") + Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    Searcher.mougather.search(username, Mode)

                elif (sce == 2):
                    username = str(input(
                        Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Phone", "None") + Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    while username == "":
                        username = str(input(
                            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Phone", "None") + Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    Searcher_phone.Phone_search.searcher(username, Mode)

                elif sce == 3:
                    username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Site", "None") +
                                   Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    while username == "":
                        username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Site", "None") +
                                       Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    Searcher_website.Web.search(username, Mode)
                elif sce == 4:
                    config.Config.main(Mode)
                elif sce == 5:
                    Database.Controller.Gui()
                elif sce == 6:
                    if os.name == "nt":
                        Update.Downloader.Check_Creds()
                    else:
                        os.system("Core/./update.sh")
                elif sce == 7:
                    username = input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Port", "None") +
                                     Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->")
                    while username == "":
                        username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Port", "None") +
                                       Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    Port_Scanner.Ports.Main(username, Mode)
                elif sce == 8:
                    username = input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Email", "None") +
                                     Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->")
                    while username == "":
                        username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Email", "None") +
                                       Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    E_Mail.Mail_search.Search(username, Mode)
                elif sce == 9:
                    username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Param", "None") +
                                       Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    while username == "":
                        username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Param", "None") +
                                       Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    Dork.List.Main(username, Mode)
                elif sce == 10:
                    username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Param", "None") +
                                       Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    while username == "":
                        username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Param", "None") +
                                       Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    Searcher_person.info.Search(username, Mode)
                elif sce == 11:
                    username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Param", "None") +
                                       Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    while username == "":
                        username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Param", "None") +
                                       Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    Decoder.Menu.Main(username, Mode)
                elif sce == 12:
                    username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Param", "None") +
                                       Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    while username == "":
                        username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Param", "None") +
                                       Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    Pdf.Menu.Main(username, Mode)
                elif sce == 13:
                    username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Param", "None") +
                                       Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    while username == "":
                        username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Param", "None") +
                                       Font.Color.GREEN + "\n\n[#MOUGATHER#]" + Font.Color.WHITE + "-->"))
                    Transfer.Menu.Main(username, Mode)
                elif sce == 14:
                    Session.Options.View()
                elif sce == 15:
                    print(Language.Translation.Translate_Language(
                        filename, "Main", "Exit", "None"))
                    exit()
                elif sce == 0:
                    Main.main(Mode)
                else:
                    print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                          Language.Translation.Translate_Language(filename, "Default", "KeyError", "None"))
                    exit()
            except ValueError as e:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Default", "ValueError", "None") + "{}".format(str(e)))
                exit()
