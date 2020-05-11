import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException,NoSuchWindowException,WebDriverException,SessionNotCreatedException
from selenium.webdriver.support.ui import Select
import datetime
import calendar
import time
from colorama import Fore,Style
from tabulate import tabulate
from PIL import Image
import os

from console_progressbar import ProgressBar

VERSION = ' ~ 1.0.0'

KEYBOARDPROMPTS_Yy = ['Y', 'y']
KEYBOARDPROMPTS_Nn = ['N', 'n']

value_list = []
for x in range(4, 22):
    value_list.append(float(x))
    value_list.append(float(x + 0.30))
    value_list.append(float(x + 0.45))
value_list = value_list[:-1]
TIMES_DICTIONARY = {}
TIMES = ['04:00AM', '04:30AM', '04:45AM', '05:00AM', '05:30AM', '05:45AM', '06:00AM', '06:30AM', '06:45AM',
             '07:00AM', '07:30AM', '07:45AM', '08:00AM', '08:30AM', '08:45AM', '09:00AM', '09:30AM', '09:45AM',
             '10:00AM', '10:30AM', '10:45AM', '11:00AM', '11:30AM', '11:45AM', '12:00(NOON)', '12:30PM', '12:45PM',
             '01:00PM', '01:30PM', '01:45PM', '02:00PM', '02:30PM', '02:45PM', '03:00PM', '03:30PM', '03:45PM',
             '04:00PM', '04:30PM', '04:45PM', '05:00PM', '05:30PM', '05:45PM', '06:00PM', '06:30PM', '06:45PM',
             '07:00PM', '07:30PM', '07:45PM', '08:00PM', '08:30PM', '08:45PM', '09:00PM', '09:30PM'
             ]

for x in range(len(value_list)):
    key = value_list[x]
    TIMES_DICTIONARY[key] = TIMES[x]


#handeling the Calendar
months = {'1': 'Janauary',
             '2': 'February',
             '3': 'March',
             '4': 'April',
             '5': 'May',
             '6': 'June',
             '7': 'July',
             '8': 'August',
             '9': 'September',
             '10': 'October',
             '11': 'November',
             '12': 'December'    }

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

def PERMISSION_APPLY():
    try:
        BANNER = Fore.RED + Style.BRIGHT + '''


        A ᴜ ᴛ ᴏ ᴍ ᴀ ᴛ ᴇ''' + Fore.BLUE + Style.BRIGHT + '''
                                                        Y8P                   Y8P

                88888b.   .d88b.  888d888 88888b.d88b.  888 .d8888b  .d8888b  888  .d88b.  88888b.
                888 "88b d8P  Y8b 888P"   888 "888 "88b 888 88K      88K      888 d88""88b 888 "88b
                888  888 88888888 888     888  888  888 888 "Y8888b. "Y8888b. 888 888  888 888  888
                888 d88P Y8b.     888     888  888  888 888      X88      X88 888 Y88..88P 888  888
                88888P"   "Y8888  888     888  888  888 888  88888P'  88888P' 888  "Y88P"  888  888
                888
                888
                888
                                                                                                ''' + Fore.GREEN + Style.BRIGHT + VERSION

        temp = CREDENTIALS()

        print(BANNER + Style.RESET_ALL)

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(options=options)

        url = 'https://login.gitam.edu/Login.aspx'

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
        else:
            print(Fore.RED + Style.BRIGHT + 'Failed')
            driver.quit()
            print(Fore.RED + '\nThere might be a driver-error, Please re-execute the script.\n\n')
            print(Style.RESET_ALL)
            exit()


        driver.find_element_by_xpath(xpath='// *[ @ id = "MainContent_vsp"] / a').click()


        time.sleep(1)

        def DATE_ENTRY(input_month_number, input_year, input_month_data):

            DATE_NOW = str(datetime.datetime.now())[:10]
            DATE_NOW = int(DATE_NOW[-2:])

            while True:
                ENTRY_DATE = int(input(Fore.GREEN + '\nEnter' + Fore.BLUE + Style.BRIGHT + ' a Date - '))
                if(ENTRY_DATE< DATE_NOW):
                    print(Fore.RED+Style.BRIGHT+"\nYou can apply for a permission in the PAST!\n")
                    continue
                elif (ENTRY_DATE in input_month_data):

                    break

                else:
                    print(Fore.RED + Style.BRIGHT + 'Invalid Date, Re-Enter .. ')
                    continue

            input_month_number_d = str(input_month_number).zfill(2)
            ENTRY_DATE = str(ENTRY_DATE).zfill(2)
            input_year = str(input_year)
            date = ENTRY_DATE + ' ' + input_month_number_d + ' ' + input_year
            DAY_NAME = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            DAY = datetime.datetime.strptime(date, '%d %m %Y').weekday()
            RESULT_DAYNAME = DAY_NAME[DAY]
            xpath = RESULT_DAYNAME + ', ' + str(
                months.get(str(input_month_number))) + ' ' + ENTRY_DATE + ', ' + input_year
            xpath_title_segment = '// *[ @ title = "' + xpath + '"]'
            driver.find_element_by_xpath(xpath=xpath_title_segment).click()

            return xpath

        def TIME_DROPDOWN_MENU():
            while True:
                INPUT_TIME_0 = float(input(
                    Fore.GREEN + '\nChoose' + Fore.BLUE + Style.BRIGHT + ' FROM TIME,' + Style.RESET_ALL + Fore.GREEN + ' from the ' + Fore.RED + Style.BRIGHT + "Time Values" + Style.RESET_ALL + Fore.GREEN + ' column : '))
                if (INPUT_TIME_0 in TIMES_DICTIONARY.keys()):
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + 'Invalid, Re-Enter')
                    continue

            while True:

                INPUT_TIME_1 = float(input(
                    Fore.GREEN + '\nChoose' + Fore.BLUE + Style.BRIGHT + ' TO TIME,' + Style.RESET_ALL + Fore.GREEN + ' from the ' + Fore.RED + Style.BRIGHT + "Time Values" + Style.RESET_ALL + Fore.GREEN + ' column : '))
                if (INPUT_TIME_1 in TIMES_DICTIONARY.keys()):
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + 'Invalid,Re-Enter')
                    continue
            print(Fore.GREEN + '\n  -- Setting Values .. \n')
            time.sleep(2)
            return INPUT_TIME_0, INPUT_TIME_1

        def PERMISSION():
            print()
            # Reason Entry
            time.sleep(4)
            while True:
                REASON = input(
                    Fore.GREEN + Style.BRIGHT + '\nEnter' + Fore.BLUE + Style.BRIGHT + ' the Reason : ' + Style.RESET_ALL)
                if (len(REASON) < 4):
                    print(Fore.RED + Style.BRIGHT + '\nEnter a Valid Reason ! ' + Style.RESET_ALL)
                    continue
                else:
                    break

            driver.find_element_by_xpath(xpath='//*[@id="MainContent_txtreason"]').send_keys(REASON)
            print()

            # TRAVEL BY
            select = Select(driver.find_element_by_id('MainContent_ddltrans'))

            print(
                Fore.RED + Style.BRIGHT + 'Travel By Options.. ' + Fore.BLUE + Style.BRIGHT + '\n[1]' + Fore.RED + Style.BRIGHT + ' -- Air.' + Fore.BLUE + Style.BRIGHT + '\n[2]' + Fore.RED + Style.BRIGHT + ' -- Bus.' + Fore.BLUE + Style.BRIGHT + '\n[3]' + Fore.RED + Style.BRIGHT + ' -- Train.' + Fore.BLUE + Style.BRIGHT + '\n[4]' + Fore.RED + Style.BRIGHT + ' -- Vehicle.')

            TRAVEL_BY_OPTIONS = {
                1: 'Air',
                2: 'Bus',
                3: 'Train',
                4: 'Vehicle',
            }
            OPTION_CODES = list(map(str, list(range(1, 5))))

            while True:
                TRAVEL_BY = input(
                    Fore.GREEN + Style.BRIGHT + "\nEnter" + Fore.BLUE + Style.BRIGHT + ' TRAVEL BY' + Fore.GREEN + Style.BRIGHT + " number : " + Style.RESET_ALL)
                if TRAVEL_BY in OPTION_CODES:

                    print(Fore.RED + '\nSelected Option ~ ' + Fore.BLUE + TRAVEL_BY_OPTIONS.get(int(TRAVEL_BY)))
                    print()
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + ' - - Invalid option - -\nRe-Enter >')
                    continue

            select.select_by_visible_text(TRAVEL_BY_OPTIONS.get(int(TRAVEL_BY)))

            TRAVEL_INFO = input(
                Fore.GREEN + Style.BRIGHT + "Enter the" + Fore.BLUE + Style.BRIGHT + " Travelling Information (Destination) : ")

            driver.find_element_by_xpath(xpath='//*[@id="MainContent_txtdestination"]').send_keys(TRAVEL_INFO)
            print()

            print('\n')
            df = pd.DataFrame(pd.Series(months).T)
            df.columns = ['Month Names']
            df.index.name = 'Month Number'
            print(Fore.BLUE + Style.BRIGHT + tabulate(df, headers='keys', tablefmt='rst') + Style.RESET_ALL)
            print('\n')
            PROGRESS_BAR('Handling Calendar')
            print('\n')
            # Click on Calendar
            driver.find_element_by_xpath(xpath='//*[@id="txtdate1"]').click()
            current_month = driver.find_element_by_xpath(xpath='//*[@id="MainContent_CalendarExtender2_title"]').text
            current_month, current_year = current_month.split(', ')
            VALID_YEARS = list(range(int(current_year), 2021))
            datetimeobj = datetime.datetime.strptime(current_month, "%B")
            current_month_number = datetimeobj.month
            print(Fore.BLUE + 'Current Month ~ ' + Fore.RED + Style.BRIGHT + current_month)
            print(Fore.BLUE + 'Current Year ~ ' + Fore.RED + Style.BRIGHT + current_year)

            while True:
                input_month_number = input(
                    Fore.GREEN + Style.BRIGHT + '\nEnter' + Fore.BLUE + Style.BRIGHT + ' the month number : ')
                input_year = input('Enter year : ')
                print('\n')
                if (int(input_month_number) < current_month_number):
                    print(Fore.RED + Style.BRIGHT + '\nYou cannot Apply a leave in the Past!..')
                    continue
                elif (input_month_number in months.keys() and int(input_year) in VALID_YEARS):
                    break
                else:
                    print(
                        Fore.RED + "You've either entered" + Style.BRIGHT + " Invalid Month number" + Style.RESET_ALL + " or " + Fore.RED + Style.BRIGHT + " an Invalid Year ..")
                    print(Fore.RED + Style.BRIGHT + '\nRe-Enter')
                    continue

            # Resetting D-Types
            input_year = int(input_year)
            input_month_number = int(input_month_number)

            while True:

                if (input_month_number in list(map(int, months.keys())) and input_year in VALID_YEARS):
                    if (input_month_number == current_month_number and input_year == int(current_year)):
                        cal = calendar.Calendar()
                        input_month_data = [d for d in cal.itermonthdays(input_year, input_month_number) if d != 0]
                        print(Fore.BLUE + Style.BRIGHT + 'Input Month ~ ' + Fore.GREEN + Style.BRIGHT + months.get(
                            str(input_month_number)))
                        print(Fore.BLUE + Style.BRIGHT + 'Dates in \n' + months.get(str(input_month_number)) + ' ~ ',
                              input_month_data, end=' ')
                        FILE_NAME = DATE_ENTRY(input_month_number, input_year, input_month_data)
                        break

                    elif (current_month_number < input_month_number and int(input_year) == int(current_year)):
                        for clicks in range(input_month_number - current_month_number):
                            driver.find_element_by_id(id_='MainContent_CalendarExtender2_nextArrow').click()
                            time.sleep(1)
                        cal = calendar.Calendar()
                        input_month_data = [d for d in cal.itermonthdays(input_year, input_month_number) if d != 0]
                        print(Fore.BLUE + Style.BRIGHT + '\nInput Month ~ ' + Fore.GREEN + Style.BRIGHTmonths.get(
                            str(input_month_number)))
                        print(Fore.BLUE + Style.BRIGHT + 'Dates in \n' + months.get(str(input_month_number)) + ' ~ ',
                              input_month_data, end=' ')
                        print('\n')
                        FILE_NAME = DATE_ENTRY(input_month_number, input_year, input_month_data)
                        break
                    elif int(input_year) < int(current_year):
                        print(
                            Fore.RED + "\nyou " + Style.BRIGHT + "can't Apply Permission" + Style.RESET_ALL + " for a" + Style.BRIGHT + " PAST DATE")
                        print(Fore.RED + Style.BRIGHT + "\nPlease Re-Enter the inputs :")
                        continue

            PROGRESS_BAR('Fetching Time values')
            df = pd.DataFrame(pd.Series(TIMES_DICTIONARY).T)
            df.index.name = 'Time Values'
            df.columns = ['TIMES']
            print('\n')
            print(Fore.BLUE + Style.BRIGHT + tabulate(df, headers='keys', tablefmt='rst') + Style.RESET_ALL)
            print('\n')
            while True:
                INPUT_TIME_0, INPUT_TIME_1 = TIME_DROPDOWN_MENU()
                if (INPUT_TIME_0 < INPUT_TIME_1):
                    print(Fore.BLUE + Style.BRIGHT + '\nFrom Time ~ ' + Fore.RED + TIMES_DICTIONARY[INPUT_TIME_0])
                    print(Fore.BLUE + Style.BRIGHT + '\nTO Time ~ ' + Fore.RED + TIMES_DICTIONARY[INPUT_TIME_1])

                    break
                else:
                    print(Fore.RED + Style.BRIGHT + '\bTo TIME Cannot be lesser than FROM TIME !')
                    continue
            time.sleep(1)
            # From Date
            select_from_time = Select(driver.find_element_by_id('MainContent_cboFromtime'))
            select_from_time.select_by_visible_text(TIMES_DICTIONARY[INPUT_TIME_0])
            select_to_time = Select(driver.find_element_by_id('MainContent_cbototime'))
            select_to_time.select_by_visible_text(TIMES_DICTIONARY[INPUT_TIME_1])

            # CHECK BOX
            CHECK_BOX_TEXT = Fore.GREEN + '\n\n **' + Fore.RED + Style.BRIGHT + "'I am leaving the hostel on my own risk and responsibility until I come back.'" + Style.RESET_ALL + Fore.GREEN + ' **\n\n'

            print(Fore.CYAN + Style.BRIGHT + "\nCheck Box ~ " + CHECK_BOX_TEXT, end=' ')

            press_key = input(
                Fore.GREEN + "Press " + Fore.RED + Style.BRIGHT + 'Enter ' + Style.RESET_ALL + Fore.GREEN + "to continue . . .")
            if (press_key == True or press_key == False):
                print()

            # Check box click ..
            PERMISSION_TYPE = 'Permission'

            driver.find_element_by_xpath(xpath='//*[@id="MainContent_Chk"]').click()
            if not os.path.exists('Screenshots'):
                os.makedirs('Screenshots')
            print(Fore.GREEN + '\n   -- Opening Image Preview of the Application..')
            driver.save_screenshot(
                './Screenshots/' + PERMISSION_TYPE + '-' + FILE_NAME + '.png')  # saves screenshot of entire page

            image = Image.open('./Screenshots/' + PERMISSION_TYPE + '-' + FILE_NAME + '.png')

            image.show()

            print(Fore.CYAN + '\n   -- Saving the Picture under, /Screenshots .. ')
            time.sleep(1)

            while True:
                ABORT_INPUT = input(
                    Fore.GREEN + '\nEnter' + Fore.BLUE + ' [Y/y] to' + Style.BRIGHT + ' Submit,' + Style.RESET_ALL + Fore.BLUE + ' [N/n] to' + Style.BRIGHT + ' ABORT Application : ')
                if (ABORT_INPUT in KEYBOARDPROMPTS_Yy):
                    break
                elif (ABORT_INPUT in KEYBOARDPROMPTS_Nn):
                    print(Fore.RED + Style.BRIGHT + '\nAborting Progress . . ')
                    print(Fore.RED + Style.BRIGHT + 'Closing Browser .. ')
                    driver.quit()
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + 'Invalid Input, \nRe-Enter ..')
                    continue

            print(Fore.GREEN+Style.BRIGHT+'\nSubmit Done.[[-run-permission-status-Script-to-verify-]]\n')

            #SUBMIT BUTTON
            driver.find_element_by_xpath(xpath='//*[@id="MainContent_Button1"]').click()
            driver.quit()
            print(Style.RESET_ALL)
            exit()

        PERMISSION()




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

