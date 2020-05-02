from selenium.common.exceptions import NoSuchWindowException, WebDriverException, NoSuchElementException, \
    SessionNotCreatedException
from selenium import webdriver
import pandas as pd
from colorama import Fore, Style
from selenium.webdriver.chrome.options import Options
from console_progressbar import ProgressBar
import time
import calendar
import datetime
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style='darkgrid')

VERSION = '1.0.0'
KEYBOARDPROMPTS_Yy = ['Y', 'y']
KEYBOARDPROMPTS_Nn = ['N', 'n']


def PROGRESS_BAR(prompt):
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT)
    pb = ProgressBar(total=100, prefix=prompt, suffix='progress', decimals=2, length=50, fill='*',
                     zfill='-')
    pb.print_progress_bar(27)
    time.sleep(.900)
    pb.print_progress_bar(68)
    time.sleep(.800)
    pb.print_progress_bar(96)
    time.sleep(2)
    pb.print_progress_bar(100)
    print(Style.RESET_ALL)


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


def PREDICTION(control_flow):
    if (control_flow == '01'):
        driver = webdriver.Chrome()
        DRIVER(driver)


    elif (control_flow == '10'):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
        DRIVER(driver)


def DRIVER(driver):
    BANNER = Fore.RED + Style.BRIGHT + '''                                                                              
                𝘼𝙩𝙩𝙚𝙣𝙙𝙖𝙣𝙘𝙚''' + Fore.LIGHTGREEN_EX + Style.BRIGHT + '''                                                   
                         e                         888                ,e,                                           
                        d8b     888-~88e   /~~~8e  888 Y88b  /  d88~\  "   d88~\                                    
                       /Y88b    888  888       88b 888  Y888/  C888   888 C888                                      
                      /  Y88b   888  888  e88~-888 888   Y8/    Y88b  888  Y88b                                     
                     /____Y88b  888  888 C888  888 888    Y      888D 888   888D                                    
                    /      Y88b 888  888  "88_-888 888   /     \_88P  888 \_88P                                     
                                                       _/                     ''' + Fore.BLUE + Style.BRIGHT + VERSION
    print('\n\n\n')
    print(BANNER + Style.RESET_ALL)

    try:

        # login
        driver.get(url=url)
        # LOGIN
        # username
        PROGRESS_BAR('Accessing-Account')
        driver.find_element_by_id('txtusername').send_keys(temp[0])
        # password
        driver.find_element_by_id('password').send_keys(temp[1])
        # submit
        try:
            driver.find_element_by_xpath(xpath='//*[@id="Submit"]').click()
        except NoSuchElementException:
            pass
        print(Fore.BLUE + Style.BRIGHT + 'Login Status ~ ', end='')

        if (driver.title == 'GITAM | Student portal'):
            print(Fore.GREEN + Style.BRIGHT + 'Successful')

        print(Fore.GREEN + '\n -- Handling a Calendar ..  ')
        driver.find_element_by_xpath(xpath='// *[ @ id = "MainContent_ad"] / a').click()

        # calendar

        driver.find_element_by_xpath(xpath='//*[@id="MainContent_Button3"]').click()

        def GET_STATUS_DF(parsed_month_data, parsed_month):
            xpath_segment = ""
            DATAFRAME = list()
            print(Fore.BLUE + Style.BRIGHT + '\n  -- Calculating the Estimated Time for Scraping Data ... ')
            EST = 6 * len(parsed_month_data) / 60
            print(Fore.GREEN + Style.BRIGHT + '\n  -- Estimated Time to Scrape, EST(minutes) ~ ', round(EST, 2))
            print(Fore.GREEN + Style.BRIGHT + '\nStarting .. ')
            print(Fore.CYAN + Style.BRIGHT)
            for x in parsed_month_data:
                xpath_segment = str(x) + " " + parsed_month

                segment0 = '''//*[@title="'''
                segment1 = '''"]'''

                driver.find_element_by_xpath(xpath=segment0 + xpath_segment + segment1).click()

                # web.driver.implicitly_wait()

                dfs = pd.read_html(driver.page_source, header=0)

                try:
                    print(Fore.GREEN + Style.BRIGHT + '[ * ] ' + Fore.RED + Style.BRIGHT + xpath_segment)
                    DATAFRAME.append(pd.DataFrame(dfs[3]))

                except IndexError:
                    print(Fore.LIGHTBLUE_EX + 'Data Fetch STATUS ~ ', end='')
                    print(Fore.RED + Style.BRIGHT + driver.find_element_by_xpath('//*[@id="MainContent_lblcal"]').text)

                time.sleep(2)
            print(Style.RESET_ALL)

            return DATAFRAME

        def STATUS_CALENDAR():
            # Calendar
            month_numbers = list(range(1, 13))

            current_month = driver.find_element_by_xpath(
                '//*[@id="MainContent_d1"]/tbody/tr[1]/td/table/tbody/tr/td[2]').text
            current_month, current_year = current_month.split()
            datetime_object = datetime.datetime.strptime(current_month, "%B")
            current_month_number = datetime_object.month
            date_timeobj = datetime.datetime.strptime(current_month, "%B")
            current_month_number = date_timeobj.month

            print(Fore.CYAN + '\nCurrent Month ~ ' + Fore.RED + Style.BRIGHT + current_month + Style.RESET_ALL)
            print(
                Style.BRIGHT + Fore.CYAN + 'Current Year ~ ' + Fore.RED + Style.BRIGHT + current_year + Style.RESET_ALL)
            date_timeobj = datetime.datetime.strptime(current_month, "%B")
            current_month_number = date_timeobj.month
            print(Style.BRIGHT + Fore.CYAN + 'Current Month number ~ ' + Fore.RED + Style.BRIGHT + str(
                current_month_number) + Style.RESET_ALL)
            print(
                Fore.RED + Style.BRIGHT + '\nNOTE' + Style.RESET_ALL + Fore.RED + ' ~ Enter the month number as Number of months back\nExample :- If you want February 2020, Enter how many months its back to the current month  \n')

            while True:
                month_input = input(
                    Fore.GREEN + 'Enter the month number as ' + Fore.RED + Style.BRIGHT + ' Number of months back :')
                if (month_input.isdigit()):
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + '\nInvalid input, Re-Enter : ')
                    continue
            print(Fore.GREEN + Style.BRIGHT + 'Parsing .. ')

            for clicks in range(int(month_input)):
                driver.find_element_by_xpath(
                    xpath='//*[@id="MainContent_d1"]/tbody/tr[1]/td/table/tbody/tr/td[1]/a').click()

            parsed_month = driver.find_element_by_xpath(
                '//*[@id="MainContent_d1"]/tbody/tr[1]/td/table/tbody/tr/td[2]').text
            parsed_month, parsed_year = parsed_month.split()
            print(Fore.CYAN + '\nCurrent Month ~ ' + Fore.RED + Style.BRIGHT + parsed_month + Style.RESET_ALL)
            print(
                Style.BRIGHT + Fore.CYAN + 'Current Year ~ ' + Fore.RED + Style.BRIGHT + parsed_year + Style.RESET_ALL)
            while True:
                OPTION_KEY = input(
                    Fore.GREEN + "\nEnter" + Fore.RED + Style.BRIGHT + " Y/y if it is " + Style.RESET_ALL + Fore.GREEN + " the Month of Desire, " + Fore.RED + Style.BRIGHT + " N/n to Change : ")
                if (OPTION_KEY in KEYBOARDPROMPTS_Yy):
                    datetime_object = datetime.datetime.strptime(parsed_month, "%B")
                    parsed_month_number = datetime_object.month
                    break
                elif (OPTION_KEY in KEYBOARDPROMPTS_Nn):
                    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '\n -- Re-setting the Calendar to Initial Postion .. ')
                    for clicks in range(int(month_input)):
                        driver.find_element_by_xpath(
                            xpath='//*[@id="MainContent_d1"]/tbody/tr[1]/td/table/tbody/tr/td[3]/a').click()
                    STATUS_CALENDAR()

                    break
                else:
                    print(Fore.RED + Style.BRIGHT + '\nInvalid Key..\nRe-Enter : ')
                    continue

            cal = calendar.Calendar()
            parsed_month_data = [d for d in cal.itermonthdays(2020, parsed_month_number) if d != 0]
            print(Fore.CYAN + Style.BRIGHT + 'Dates in ~ ' + Fore.GREEN + parsed_month, '\n', parsed_month_data)
            Dataframe_list = GET_STATUS_DF(parsed_month_data, parsed_month)

            return Dataframe_list

        def DATA_ORGANISATION(DATAFRAME_LIST):
            copy_df_list = DATAFRAME_LIST
            if (len(DATAFRAME_LIST) != 0):
                print(Fore.BLUE + Style.BRIGHT + '\nNumber of Days Scraped : ' + Fore.GREEN, len(copy_df_list))
                print('\n')

                print(Fore.GREEN + '\n  -- Organising Data to the Standard format .. ')
                pivot = copy_df_list.pop(0)
                for df in copy_df_list:
                    pivot = pd.concat([pivot, df], axis=0)

                pivot = pivot.reset_index(drop=True)
                pd.options.display.width = None
                print('\n')
                print(Fore.BLUE + Style.BRIGHT + '\nNumber of Valid Records : {}' + Fore.GREEN,
                      len(pivot['Date and time']))
                print('\n')
                return pivot
            else:
                print(Fore.RED + Style.BRIGHT + '\nNo Records Found !')
                print(Fore.RED + Style.BRIGHT + '\nExiting Code .. ')
                return 'EXIT'

        def PREPROCESSING(organised_df):

            Ogdf_copy = organised_df
            subnames = list(np.unique(organised_df['Subject']))
            subacronyms = []
            for sub in subnames:
                subacronyms.append(''.join(w[0].upper() for w in sub.split()))

            SUBJECTS = {subacronyms[i]: subnames[i] for i in range(len(subnames))}
            subs_df = pd.DataFrame(pd.Series(SUBJECTS))
            subs_df.index.name = 'Subject'
            subs_df.columns = ['Acronymns']
            print(tabulate(subs_df, headers='keys'))
            print('\n')
            while True:
                SUBJECT_INPUT = input(
                    Fore.GREEN + 'Enter' + Fore.BLUE + Style.BRIGHT + ' a Subject Acronymn : ').upper()
                if (SUBJECT_INPUT in SUBJECTS.keys()):
                    print(Fore.BLUE + '\n Collecting Data of ~ ' + Fore.GREEN + Style.BRIGHT + SUBJECTS[SUBJECT_INPUT])
                    sub_stat_df = organised_df[organised_df['Subject'] == SUBJECTS[SUBJECT_INPUT]]
                    print(sub_stat_df.reset_index(drop=True))
                    print(Fore.BLUE + Style.BRIGHT + '\nNumber of Total Records : ' + Fore.GREEN, sub_stat_df.shape[0])
                    print(Fore.GREEN + '\n  -- Formatting Data .. ')
                    print(Fore.CYAN + '\n -- close the Graph to know Additional Stats .. ')
                    sub_stat_df = pd.DataFrame([list(sub_stat_df['Status'])],
                                               columns=list(sub_stat_df['Date and time']))
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + 'Invalid Subject Acronym,\nRe-Enter : ')
                    continue

            return sub_stat_df

        def ANALYSIS_PRED(SUBJECT_df):

            # Counts
            df0 = SUBJECT_df.T
            counts = df0[0].value_counts()

            # presetting figure size
            plt.figure(figsize=(10, 3))
            plt.ylim = (0, 20)
            plt.title('Persent & Absent Statistics', size=15)
            plt.ylabel = 'Number of Classes Attended'
            plt.xlabel = 'Stats'
            plt.barh(counts.index, counts.values, color=['lightblue', 'red'], edgecolor='black')

            print('\nAdditional STATS.')
            try:
                PRESENT_PERCENTAGE = (counts['Present'] / sum(counts.values)) * 100
                ABSENT_PERCENTAGE = (counts['Absent'] / sum(counts.values)) * 100

                print(Fore.BLUE + Style.BRIGHT + '\nAbsent Percentage for Subject is : ' + Fore.GREEN,
                      (round(ABSENT_PERCENTAGE, 2)), end='%')
                print(Fore.BLUE + Style.BRIGHT + '\nPercent Percentagge for the Subject is ' + Fore.GREEN,
                      (round(PRESENT_PERCENTAGE, 2)), end='%')
            except KeyError:
                print(Fore.BLUE + Style.BRIGHT + '\nPercent Percentagge for the Subject is ' + Fore.GREEN,
                      (round(PRESENT_PERCENTAGE, 2)), end='%')

                print(Fore.RED + '\nNo Absent Records found ..')

            plt.show()

        df_list = STATUS_CALENDAR()
        print(Fore.GREEN + '\nData Collection Completed .. \n')
        print(Fore.BLUE + '-- Initiating Data Organisation .. ')
        organised_df = DATA_ORGANISATION(df_list)

        try:
            if (organised_df == 'EXIT'):
                print(Fore.LIGHTBLUE_EX + Style.BRIGHT + '\nSeems Like no Records were Found .. ')
                print(Fore.RED + Style.BRIGHT + '\nExiting Code .. ')
            else:
                SUBJECT_DF = PREPROCESSING(organised_df)
        except ValueError:

            SUBJECT_DF = PREPROCESSING(organised_df)

        ANALYSIS_PRED(SUBJECT_DF)


    except (NoSuchWindowException, WebDriverException):
        print(Fore.RED + Style.BRIGHT + "\nBrowser Window Closed . . . ")
        print(Fore.RED + Style.BRIGHT + "\nPlease RE-EXECUTE  the script\n")


    except SessionNotCreatedException:
        print(
            Fore.RED + Style.BRIGHT + "Chrome-Driver --version and Chrome --version are not Sychronised ..\n -- Please read the Documentation --  ")
        print(
            Fore.RED + Style.BRIGHT + 'Visit the url to Download Chrome-Driver' + Fore.CYAN + Style.BRIGHT + 'https://chromedriver.chromium.org/downloads')

    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + '\n Keyboard Interruption !\nExiting Code . . .\n')

