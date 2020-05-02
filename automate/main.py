from selenium.common.exceptions import NoSuchWindowException,NoSuchElementException,WebDriverException,SessionNotCreatedException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import bs4 as bs
import pandas as pd
from colorama import Fore,Style
from console_progressbar import ProgressBar
import time

VERSION = '1.0.0'

def PROGRESS_BAR(prompt):
    print(Fore.LIGHTYELLOW_EX+Style.BRIGHT)
    pb = ProgressBar(total=100, prefix=prompt, suffix='progress', decimals=2, length=50, fill='*',
                     zfill='-')
    pb.print_progress_bar(10)
    time.sleep(.900)
    pb.print_progress_bar(25)
    time.sleep(.800)
    pb.print_progress_bar(90)
    time.sleep(2)
    pb.print_progress_bar(100)
    print(Style.RESET_ALL)

# Login Details

try:
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
except FileNotFoundError:

        file = open('logindetails.txt', 'w+')
        temp = file.readlines()
        file.close()







url = 'https://login.gitam.edu/Login.aspx'

# MAIN CRAWLER CODE
def main(control_flow):


    if(control_flow == '01'):
        driver = webdriver.Chrome()

        WEB_AUTOMATE(driver)



    elif (control_flow == '10'):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Last I checked this was necessary.
        driver = webdriver.Chrome(options=options)
        WEB_AUTOMATE(driver)





def WEB_AUTOMATE(driver):

    try:

        driver.get(url=url)
        PROGRESS_BAR('Accessing Account')
        # login
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath='//*[@id="txtusername"]').send_keys(temp[0])
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath='//*[@id="password"]').send_keys(temp[1])
        time.sleep(0.5)
        print(Fore.RED + 'Login Status ~ ', end='')
        try:
            driver.find_element_by_xpath(xpath='//*[@id="Submit"]').click()
        except NoSuchElementException:
            pass

        if(driver.title == 'GITAM | Student portal'):
            print(Fore.GREEN + Style.BRIGHT+'Successful')


        # Attendance
        PROGRESS_BAR('Fetching Data')
        driver.find_element_by_xpath(xpath='//*[@id="MainContent_ad"]/a/img').click()

        # total Attendance
        tot_attendance = driver.find_element_by_id('MainContent_lbltotal').text
        print(Fore.CYAN + '\nTotal Attendance-Percentage ~ '+Style.BRIGHT+Fore.GREEN+ tot_attendance, Style.RESET_ALL)

        # progress bar

        # M E N U
        driver.minimize_window()

        iteration_count=0

        while True:
            iteration_count +=1
            if(iteration_count >1):
                press_key = input(Fore.GREEN+"Press " + Fore.RED+Style.BRIGHT +'Enter ' +Style.RESET_ALL+Fore.GREEN+"to continue . . .")
                if (press_key == True or press_key == False):
                    continue
                    

            print('\n\n')
            print(Fore.BLUE + Style.BRIGHT + '____________________________________________')
            print(Fore.BLUE + Style.BRIGHT + '_______________O P T I O N S________________')
            print(Fore.RED + 'Action/Fetch{:>32}'.format('Code'))
            print(Fore.BLUE + Style.BRIGHT + '____________________________________________')
            print(Fore.WHITE + '* By Subject{:>37}'.format(Fore.RED + ' [ 1 ]'))
            print(Fore.WHITE + '* Today{:>42}'.format(Fore.RED + ' [ 2 ]'))
            print(Fore.WHITE + '* Yesterday{:>38}'.format(Fore.RED + ' [ 3 ]'))
            print(Fore.WHITE + '* Exit-Code{:>38}'.format(Fore.RED + ' [ y ]'))
            print(Fore.BLUE + Style.BRIGHT + '____________________________________________')

            option = input(Fore.BLUE + 'E N T E R  C O D E >> ')

            print('\n\n')



            dict = {
                1: 'Ｂｙ Ｓｕｂｊｅｃｔ',
                2: 'Ｔｏｄａｙ',
                3: 'Ｙｅｓｔｅｒｄａｙ',
                'y': 0,

            }
            pd.options.display.width = None
            if (option == '1'):
                print('Action/Fetch ~{:>32}'.format(dict[1]))
                # By Subject
                soup_level0 = bs.BeautifulSoup(driver.page_source, 'lxml')
                driver.find_element_by_xpath(xpath='//*[@id="MainContent_Button4"]').click()
                html0 = driver.page_source
                df0 = pd.read_html(html0, header=0)
                PROGRESS_BAR("By_Subject-Data")
                try:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT)
                    print(pd.DataFrame(df0[1]))
                    print('\n\n\n')

                except IndexError:

                    print(Fore.RED + 'STATUS = ', end='')
                    print(Fore.RED + driver.find_element_by_xpath('//*[@id="MainContent_lblcal"]').text,
                          Style.RESET_ALL)
                    print('\n\n\n')



            elif (option == '2'):
                # Today
                print('Action/Fetch ~{:>32}'.format(dict[2]))
                driver.find_element_by_xpath(xpath='//*[@id="MainContent_Button1"]').click()
                soup_level1 = bs.BeautifulSoup(driver.page_source, 'lxml')
                html1 = driver.page_source
                df1 = pd.read_html(html1, header=0)
                PROGRESS_BAR("Today-Data")
                try:

                    print(pd.DataFrame(df1[1]))
                    print('\n\n\n')

                except IndexError:

                    print(Fore.RED + 'STATUS = ', end='')
                    print(Fore.RED + Style.BRIGHT + driver.find_element_by_xpath('//*[@id="MainContent_lblcal"]').text,
                          Style.RESET_ALL)
                    print('\n\n\n')

            elif (option == '3'):
                # Yesterday
                print('Action/Fetch ~{:>32}'.format(dict[2]))
                driver.find_element_by_xpath(xpath='//*[@id="MainContent_Button1"]').click()
                soup_level2 = bs.BeautifulSoup(driver.page_source, 'lxml')
                html2 = driver.page_source
                df2 = pd.read_html(html2, header=0)
                PROGRESS_BAR('Yesterday-Data')
                try:

                    print(pd.DataFrame(df2[1]))
                    print('\n\n\n')

                except IndexError:

                    print(Fore.RED + 'STATUS = ', end='')
                    print(Fore.RED + Style.BRIGHT + driver.find_element_by_xpath('//*[@id="MainContent_lblcal"]').text,
                          Style.RESET_ALL)
                    print('\n\n\n')

            elif (option == 'Y' or option == 'y'):
                print(Fore.RED+Style.BRIGHT+'Closing Browser . . . ')
                driver.quit()
                print(Fore.RED + Style.BRIGHT + 'Exiting Code . . . \n')

                exit(0)

            else:
                print(Fore.RED+Style.BRIGHT+'\n------Wrong Input Enter Again . . . . \n')
                continue




    except (NoSuchWindowException,WebDriverException):
        print(Fore.RED + Style.BRIGHT + "\nBrowser Window Closed . . . ")
        print(Fore.RED + Style.BRIGHT + "\nPlease RE-EXECUTE  the script\n")
        print(Style.RESET_ALL)


    except SessionNotCreatedException:
        print(
            Fore.RED + Style.BRIGHT + "Chrome-Driver --version and Chrome --version are not Sychronised ..\n -- Please read the Documentation --  ")
        print(
            Fore.RED + Style.BRIGHT + 'Visit the url to Download Chrome-Driver' + Fore.CYAN + Style.BRIGHT + 'https://chromedriver.chromium.org/downloads')
        print(Style.RESET_ALL)
        
    except KeyboardInterrupt:
        print(Fore.RED+Style.BRIGHT +'\n Keyboard Interruption !\nExiting Code . . .\n')
        print(Style.RESET_ALL)












