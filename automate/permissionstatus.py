import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException,NoSuchWindowException,WebDriverException,SessionNotCreatedException
import time
from colorama import Fore,Style
from tabulate import tabulate
from console_progressbar import ProgressBar
import os
VERSION = ' ~ 1.0.0'

def PROGRESS_BAR(prompt):
    print(Fore.CYAN+Style.BRIGHT)
    pb = ProgressBar(total=100, prefix=prompt, suffix='progress', decimals=2, length=50, fill='*',
                     zfill='-')
    pb.print_progress_bar(19)
    time.sleep(.700)
    pb.print_progress_bar(54)
    time.sleep(.600)
    pb.print_progress_bar(97)
    time.sleep(1)
    pb.print_progress_bar(100)
    print(Style.RESET_ALL)


def CREDENTIALS():
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

    return temp

def PERMISSION_STAT():
    try:
        BANNER = Fore.LIGHTCYAN_EX + Style.BRIGHT + '''                                                                     
                      ___               _       _            ___ _        _                                             
                     | _ \___ _ _ _ __ (_)_____(_)___ _ _   / __| |_ __ _| |_ _  _ ___                                  
                     |  _/ -_| '_| '  \| (_-(_-| / _ | ' \  \__ |  _/ _` |  _| || (_-<                                  
                     |_| \___|_| |_|_|_|_/__/__|_\___|_||_| |___/\__\__,_|\__|\_,_/__/                                  
                                                                                  ''' + Fore.GREEN + Style.BRIGHT + VERSION

        print('\n\n' + BANNER + Style.RESET_ALL)

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(options=options)

        url = 'https://login.gitam.edu/Login.aspx'

        # Login Creds
        temp = CREDENTIALS()

        driver.get(url=url)
        # LOGIN
        # username
        driver.find_element_by_id('txtusername').send_keys(temp[0])
        # password
        driver.find_element_by_id('password').send_keys(temp[1])
        # submit
        try:
            driver.find_element_by_xpath(xpath='//*[@id="Submit"]').click()
        except NoSuchElementException:
            pass

        PROGRESS_BAR('Accessing Account')
        print(Fore.BLUE + Style.BRIGHT + 'Login Status ~ ', end='')
        if (driver.title == 'GITAM | Student portal'):
            print(Fore.GREEN + Style.BRIGHT + 'Successful')

        # Permissions and Leave
        pd.options.display.width = None

        PROGRESS_BAR('Fetching Required Data')

        driver.find_element_by_xpath(xpath="//a[@href='Permissionsvsp.aspx']").click()

        driver.find_element_by_xpath(xpath='//*[@id="MainContent_Button6"]').click()
        time.sleep(2)
        dfs = pd.read_html(driver.page_source)
        try:
            under_process_df = pd.DataFrame(dfs[1])
        except IndexError:
            print(Fore.RED + Style.BRIGHT + '\nNo applications Found .. ')

        driver.find_element_by_xpath(xpath='//*[@id="MainContent_Button7"]').click()
        time.sleep(2)
        dfs = pd.read_html(driver.page_source)
        try:
            approved_df = pd.DataFrame(dfs[1])
        except IndexError:
            print(Fore.RED + Style.BRIGHT + '\nNo Applications Found .. ')

        time.sleep(2)
        driver.find_element_by_xpath(xpath='//*[@id="MainContent_btnhistory"]').click()
        time.sleep(2)
        dfs = pd.read_html(driver.page_source)
        try:
            history_df = pd.DataFrame(dfs[1])
        except IndexError:
            print(Fore.RED + Style.BRIGHT + '\nNo Applications Found .. ')
        driver.quit()

        print(Fore.GREEN + Style.BRIGHT + '\n -- Organising Data .. ')
        print('\n\n')
        print(
            Fore.RED + Style.BRIGHT + '[ 1 ]' + Fore.BLUE + Style.BRIGHT + ' Permission\n' + Fore.RED + Style.BRIGHT + '[ 2 ]' + Fore.BLUE + Style.BRIGHT + ' Leave ')
        while True:
            PERMISSION_TYPE = input(Fore.GREEN + '\nEnter' + Fore.BLUE + Style.BRIGHT + ' Permission Type : ')
            if (PERMISSION_TYPE == '1'):
                TYPE = 'Permission'
                break
            elif (PERMISSION_TYPE == '2'):
                TYPE = 'Leave'
                break
            else:
                print(Fore.RED + Style.BRIGHT + 'Invalid Input,\nRe-Enter .. ')
                continue

        permission_type_df = history_df[history_df['Type'] == TYPE]
        print(Fore.GREEN + Style.BRIGHT + '\n   -- All the Applications, Under the Mentioned Type : ', TYPE)
        print('\n' + Fore.BLUE + Style.BRIGHT)
        print(permission_type_df)
        print(Style.RESET_ALL + '\n')
        while True:
            REASON = input(Fore.GREEN + 'Enter' + Fore.BLUE + Style.BRIGHT + ' REASON to sort :')
            if (REASON in list(dict(history_df['Reason']).values())):
                break
            else:
                print(Fore.RED + Style.BRIGHT + '\nEnter a Valid Reason ..')
                continue

        value_counts = dict(history_df['Reason'].value_counts())

        if (value_counts[REASON] > 1):
            print(Fore.RED + '\n  -- There are Multiple Results of the SAME REASON -- \n')
            reason_df = history_df[history_df['Reason'] == REASON]
            while True:
                dd = input(Fore.GREEN + 'Enter' + Fore.BLUE + Style.BRIGHT + ' Date : ').zfill(2)
                mm = input(Fore.GREEN + 'Enter' + Fore.BLUE + Style.BRIGHT + ' Month : ').zfill(2)
                yyyy = input(Fore.GREEN + 'Enter' + Fore.BLUE + Style.BRIGHT + ' Year : ')
                date_string = dd + '-' + mm + '-' + yyyy
                DATE_STRING_VAL = date_string + ' 00:00:00'
                try:
                    REASON = reason_df.loc[reason_df['From date'] == DATE_STRING_VAL].iat[0, 0]
                    break
                except IndexError:
                    print(Fore.RED + Style.BRIGHT + '\nNo Records Found for the Input Date !\n')
                    continue

        if (under_process_df[under_process_df['Reason'] == REASON].empty == False):
            print(Fore.RED + Style.BRIGHT + '\nNot Approved yet .. ')
        else:
            print(Fore.RED + '\nNo results found in the Under Process List  ')
            print(Fore.GREEN + '\n  -- Application might be either' + Fore.BLUE + ' Approved or rejected ..')
            print(Fore.CYAN + Style.BRIGHT + '\n  --Checking in Approvals List.. \n')
            permission_type_df1 = approved_df[approved_df['Type'] == TYPE]
            if (approved_df[approved_df['Reason'] == REASON].empty == False):
                print(approved_df[approved_df['Reason'] == REASON])
                print(Fore.GREEN + Style.BRIGHT + '\nApproved .. \n')
                driver.quit()
            else:
                print(
                    Fore.RED + Style.BRIGHT + '\nSorry, it Seems like your application either got rejected or data might be  miss-placed ..[ Please Conduct a Manual Verification]. ')
                driver.quit()



    except (NoSuchWindowException, WebDriverException):
        print(Fore.RED + Style.BRIGHT + "\nBrowser Window Closed . . . ")
        print(Fore.RED + Style.BRIGHT + "\nPlease RE-EXECUTE  the script\n")
        print(Fore.RED+'\nNote ~ This Abnormal exit of the browser is either because you, the user are from a different CAMPUS or a Non-resident Student \nIf not,')


    except SessionNotCreatedException:
        print(
            Fore.RED + Style.BRIGHT + "Chrome-Driver --version and Chrome --version are not Sychronised ..\n -- Please read the Documentation --  ")
        print(
            Fore.RED + Style.BRIGHT + 'Visit the url to Download Chrome-Driver' + Fore.CYAN + Style.BRIGHT + 'https://chromedriver.chromium.org/downloads')

    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + '\nKeyboard Interruption !\nExiting Code . . .\n')



