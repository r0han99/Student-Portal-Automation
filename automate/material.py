from selenium.common.exceptions import WebDriverException,NoSuchWindowException,SessionNotCreatedException
from bs4 import BeautifulSoup
from webbot import Browser
import pandas as pd
from colorama import Fore,Style
import os
VERSION = '~ 1.0.0'

import time

def MATERIAL_PY():
    BANNER = Fore.RED+Style.BRIGHT+"""
    𝘼𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙤𝙣 """+"""
             ___ ___   ____  ______    ___  ____   ____   ____  _             ____  __ __ 
            |   |   | /    ||      |  /  _]|    \ |    | /    || |           |    \|  |  |
            | _   _ ||  o  ||      | /  [_ |  D  ) |  | |  o  || |     _____ |  o  )  |  |
            |  \_/  ||     ||_|  |_||    _]|    /  |  | |     || |___ |     ||   _/|  ~  |
            |   |   ||  _  |  |  |  |   [_ |    \  |  | |  _  ||     ||_____||  |  |___, |
            |   |   ||  |  |  |  |  |     ||  .  \ |  | |  |  ||     |       |  |  |     |
            |___|___||__|__|  |__|  |_____||__|\_||____||__|__||_____|       |__|  |____/ 


                                                                                    """+Fore.MAGENTA+Style.BRIGHT+VERSION
    print('\n\n'+BANNER+Style.BRIGHT)

    web = Browser()
    fn = 'logindetails.txt'
    if os.path.exists(fn):
        file = open(fn, "r")
        temp = file.readlines()
        file.close()

    else:
        file = open(fn, "w")
        print('E N T E R  Y O U R  L O G I N  D E T A I L S : ')

        print('\n')

        detail1 = input('R E G I S T R A T I O N  I D :')
        print('\n')
        detail2 = input('P A S S W O R D :')

        file.write(detail1 + "\n" + detail2)
        file.close()
        file = open(fn, 'r')
        temp = file.readlines()
        file.close()

    url = 'https://login.gitam.edu/Login.aspx'

    def SUBJECT_PANEL():

        print()

        print(
            Fore.CYAN + Style.BRIGHT + 'Navigate to the any subject panel segment of your choice to access Material  '+Style.RESET_ALL)

        print('\n')
        time.sleep(1)
        press_key = bool(input(Fore.GREEN+"Enter "+Fore.RED+Style.BRIGHT+ 'Any-Key'+Style.RESET_ALL+ Fore.GREEN + " when you're done  . . . "))

        if (press_key == True or press_key == False):
            print(Fore.CYAN+Style.BRIGHT+"\nI presume, You grabbed everything you needed .."+Fore.RED+Style.BRIGHT+"\n\nExiting Code .. ")
            web.driver.quit()
            print(Style.RESET_ALL)
            exit(1)

    try:
        web.go_to(url=url)

        # login
        web.type(temp[0], id='txtusername')
        web.type(temp[1], id='password')
        web.click('Login', id='Submit')

        # GLEARN
        Current_window = web.driver.window_handles

        web.click('Glearn', xpath="//a[@href='G-Learn.aspx']")

        # courses
        new_window = web.driver.window_handles

        new_window = list(set(new_window) - set(Current_window))[0]

        web.driver.switch_to.window(new_window)

        # - - - - This following code is optional, performance of this code will be updated in the future - - - - #
        dfs = pd.read_html(web.driver.page_source)
        list_dfs = list()
        for df in dfs:
            list_dfs.append(df)

        courses_df = list_dfs[0]
        courses_df = pd.DataFrame(courses_df[0].str[:-32])
        courses_df.rename(columns={0: 'Courses'}, inplace=True)
        courses_df.index.name = 'Option_Code'

        dict_options = {i: courses_df.at[i, 'Courses'] for i in range(courses_df.size)}

        # - - - - - - - - - - - - x x x x - - - - - - - - - - - - - - - - - - - #
        web.driver.minimize_window()
        SUBJECT_PANEL()


    except (NoSuchWindowException, WebDriverException):

        print(Fore.RED + Style.BRIGHT + "\nBrowser Window Closed . . . ")

        print(Fore.RED + Style.BRIGHT + "\nPlease RE-EXECUTE  the script\n")

        print(Style.RESET_ALL)

        exit()



    except SessionNotCreatedException:

        print(

            Fore.RED + Style.BRIGHT + "Chrome-Driver --version and Chrome --version are not Sychronised ..\n -- Please read the Documentation --  ")

        print(

            Fore.RED + Style.BRIGHT + 'Visit the url to Download Chrome-Driver' + Fore.CYAN + Style.BRIGHT + 'https://chromedriver.chromium.org/downloads')

        print(Style.RESET_ALL)

        exit()


    except KeyboardInterrupt:

        print(Fore.RED + Style.BRIGHT + '\n Keyboard Interruption !\nExiting Code . . .\n')

        print(Style.RESET_ALL)

        exit()






