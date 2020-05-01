from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, WebDriverException, \
    SessionNotCreatedException
from colorama import Fore, Style
from console_progressbar import ProgressBar
import pandas as pd
import datetime
import calendar
import time

VERSION = '~ 1.0.0'

KEYBOARDPROMPTS_Yy = ['Y', 'y']
KEYBOARDPROMPTS_Nn = ['N', 'n']


def PROGRESS_BAR(prompt):
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT)
    pb = ProgressBar(total=100, prefix=prompt, suffix='progress', decimals=2, length=50, fill='*',
                     zfill='-')
    pb.print_progress_bar(15)
    time.sleep(.900)
    pb.print_progress_bar(45)
    time.sleep(.800)
    pb.print_progress_bar(96)
    time.sleep(2)
    pb.print_progress_bar(100)
    print(Style.RESET_ALL)


def STATUS_PY():
    try:

        BANNER = Fore.RED + Style.BRIGHT + '''

            𝘼𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙤𝙣''' + Fore.CYAN + Style.BRIGHT + '''
                      _____ ______   ____  ______  __ __  _____        ____  __ __ 
                     / ___/|      | /    ||      ||  |  |/ ___/       |    \|  |  |
                    (   \_ |      ||  o  ||      ||  |  (   \_  _____ |  o  )  |  |
                     \__  ||_|  |_||     ||_|  |_||  |  |\__  ||     ||   _/|  ~  |
                     /  \ |  |  |  |  _  |  |  |  |  :  |/  \ ||_____||  |  |___, |
                     \    |  |  |  |  |  |  |  |  |     |\    |       |  |  |     |
                      \___|  |__|  |__|__|  |__|   \__,_| \___|       |__|  |____/ 

                                                                                 ''' + Style.RESET_ALL + Fore.MAGENTA + VERSION

        print(BANNER+Style.RESET_ALL)
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        # args =
        driver = webdriver.Chrome(options=options)

        # Login Details
        file = open('logindetails.txt', 'r+')
        content = file.readlines()
        if (content == []):
            print('E N T E R  Y O U R  L O G I N  D E T A I L S : ')

            print('\n')

            detail1 = input('R E G I S T R A T I O N  I D :')
            print('\n')
            detail2 = input('P A S S W O R D :')
            file.write(detail1 + "\n" + detail2)
            file = open('logindetails.txt', 'r+')
            temp = file.readlines()
            file.close()


        else:

            file = open('logindetails.txt', 'r+')
            temp = file.readlines()
            file.close()

        url = 'https://login.gitam.edu/Login.aspx'

        driver.get(url=url)
        PROGRESS_BAR('Accessing Account')
        # username
        driver.find_element_by_id('txtusername').send_keys(temp[0])
        # password
        driver.find_element_by_id('password').send_keys(temp[1])
        # submit
        try:
            driver.find_element_by_xpath(xpath='//*[@id="Submit"]').click()
        except NoSuchElementException:
            pass
        print(Fore.CYAN + Style.BRIGHT + 'Login Status ~ ', end='')
        if (driver.title == 'GITAM | Student portal'):
            print(Fore.GREEN + Style.BRIGHT + 'Successful')
        # attendance

        driver.find_element_by_xpath('//*[@id="MainContent_ad"]/a').click()

        PROGRESS_BAR("Fetching-Today's-Data")
        # today

        driver.find_element_by_xpath('//*[@id="MainContent_Button1"]').click()

        TODAY_DF = pd.read_html(driver.page_source)

        try:

            print(pd.DataFrame(TODAY_DF[1]))
            print('\n\n\n')

        except IndexError:

            print(Fore.CYAN + 'Data Fetch Status = ', end='')
            print(Fore.RED + Style.BRIGHT + driver.find_element_by_xpath('//*[@id="MainContent_lblcal"]').text)
            if (datetime.datetime.now().strftime('%H') != '07'):
                print(Fore.CYAN + '\n\n-- Current Time ~ ' + Fore.RED + Style.BRIGHT + datetime.datetime.now().strftime(
                    '%H:%M:%S'))
                print(
                    Style.RESET_ALL + Fore.RED + '-- According to the protocol, Attendance is to be updated online by ' + Style.BRIGHT + '07:00:00pm.\n')

            print('\n\n')

        def GET_STATUS_DF(ENTRY_DATE, parsed_month):
            xpath_segment = ""

            xpath_segment = ENTRY_DATE + " " + parsed_month

            print(xpath_segment)

            segment0 = '''//*[@title="'''
            segment1 = '''"]'''

            driver.find_element_by_xpath(xpath=segment0 + xpath_segment + segment1).click()

            dfs = pd.read_html(driver.page_source, header=0)

            try:
                status_df = pd.DataFrame(dfs[3])
                pd.options.display.width = None
                print(status_df.drop('Date and time', axis=1))
                absent_stat = status_df[status_df['Status'] == 'Absent']
                present_stat = status_df[status_df['Status'] == 'Present']

                if (not present_stat.empty):
                    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '\nPresent, Subjects : \nDate : ', end='')
                    print(present_stat.iat[0, 0][:-5])
                    print('\n', present_stat.drop('Date and time', axis=1).reset_index(drop=True))
                    print(Style.RESET_ALL)
                else:
                    print(
                        Fore.GREEN + "\nSeems like you are either " + Fore.RED + Style.BRIGHT + 'Absent ' + Style.RESET_ALL + Fore.GREEN + "for all the Classes or" + Fore.RED + Style.BRIGHT + " 'No Present Records Found!'")

                if (not absent_stat.empty):
                    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '\nAbsent, Subjects : \nDate : ', end='')
                    print(present_stat.iat[0, 0][:-5])
                    print('\n', absent_stat.drop('Date and time', axis=1))
                    print(Style.RESET_ALL)
                else:
                    print(
                        Fore.GREEN + "\nSeems like you are either " + Fore.RED + Style.BRIGHT + 'Present ' + Style.RESET_ALL + Fore.GREEN + "for all the Classes or" + Fore.RED + Style.BRIGHT + " 'No Absent Records Found!'")

            except IndexError:
                print(Fore.LIGHTBLUE_EX + 'Data Fetch STATUS ~ ', end='')
                print(Fore.RED + Style.BRIGHT + driver.find_element_by_xpath('//*[@id="MainContent_lblcal"]').text)

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
                Fore.RED + Style.BRIGHT + '\nNOTE' + Style.RESET_ALL + Fore.RED + ' ~ Enter the month number as Number of months back\nExample :- If you want February 2020, Enter  how many months its back to the current month \n')

            while True:
                month_input = input(
                    Fore.GREEN + 'Enter the month number as ' + Fore.RED + Style.BRIGHT + ' Number of months back :')
                if (month_input.isdigit()):
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + '\nInvalid input, Re-Enter : ')
                    continue
            print(Fore.GREEN + '\nParsing ...')
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

            while True:
                ENTRY_DATE = input(
                    Fore.GREEN + "\nEnter..\n[ * ]" + Fore.RED + Style.BRIGHT + " a Date " + Fore.GREEN + "or,\n[ * ]" + Fore.RED + Style.BRIGHT + " '0' to Exit " + Fore.GREEN + "or,\n[ * ] " + Fore.RED + Style.BRIGHT + "'99' to go_back to picking Month.\n" + Fore.GREEN + Style.BRIGHT + "Pick >> ")
                print('\n')
                if (int(ENTRY_DATE) == 0):
                    print(
                        Fore.GREEN + Style.BRIGHT + '\nI think you are satisfied, .. \n' + Fore.RED + ' Exiting Code .. ')
                    driver.quit()
                    exit()
                elif (int(ENTRY_DATE) == 99):
                    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '\n -- Re-setting the Calendar to Initial Postion .. ')
                    for clicks in range(int(month_input)):
                        driver.find_element_by_xpath(
                            xpath='//*[@id="MainContent_d1"]/tbody/tr[1]/td/table/tbody/tr/td[3]/a').click()
                    STATUS_CALENDAR()
                elif int(ENTRY_DATE) in parsed_month_data:

                    GET_STATUS_DF(ENTRY_DATE, parsed_month)

                else:
                    print(Fore.RED + Style.BRIGHT + '\nInvalid Entry..\nRe-Enter : ')
                    continue

        while True:
            OPTION_KEY = input(
                Fore.CYAN + "Enter " + Fore.RED + Style.BRIGHT + "Y/y" + Style.RESET_ALL + Fore.CYAN + " to Fetch " + Style.BRIGHT + Fore.RED + "Attendance Status" + Style.RESET_ALL + Fore.CYAN + " for an Input-Date\ " + Fore.RED + Style.BRIGHT + "N/n to quit()  : ")
            if (OPTION_KEY in KEYBOARDPROMPTS_Yy):
                # Calendar Button
                driver.find_element_by_xpath(xpath='//*[@id="MainContent_Button3"]').click()
                STATUS_CALENDAR()
                break
            elif (OPTION_KEY in KEYBOARDPROMPTS_Nn):
                driver.quit()
                print(Fore.RED + Style.BRIGHT + '\nExiting Code . . .\n')
                exit()
            else:
                print(Fore.RED + Style.BRIGHT + '\nInvalid Key..\nRe-Enter : ')
                continue








    except (NoSuchWindowException, WebDriverException):

        print(Fore.RED + Style.BRIGHT + "\n\nBrowser Window Closed . . . ")

        print(Fore.RED + Style.BRIGHT + "\n\nPlease RE-EXECUTE  the script\n")



    except SessionNotCreatedException:

        print(

            Fore.RED + Style.BRIGHT + "\nChrome-Driver --version and Chrome --version are not Sychronised ..\n -- Please read the Documentation --  ")

        print(

            Fore.RED + Style.BRIGHT + '\nVisit the url to Download Chrome-Driver' + Fore.CYAN + Style.BRIGHT + 'https://chromedriver.chromium.org/downloads')


    except KeyboardInterrupt:

        print(Fore.RED + Style.BRIGHT + '\n\nKeyboard Interruption !\nExiting Code . . .\n')




