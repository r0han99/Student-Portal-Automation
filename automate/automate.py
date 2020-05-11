from main import *
from material import *
from status import *
from permission import *
from permissionstatus import *
from prediction import *
import urllib.request
from colorama import Fore, Style
import os
import time

VERSION = '~ 1.0.0'

BANNER = Fore.GREEN + '''

    Student Portal ''' + Fore.RED + '''
                                                                               ,,
              db                 mm                                     mm     db
             ;MM:                MM                                     MM
            ,V^MM.  `7MM  `7MM mmMMmm ,pW"Wq.`7MMpMMMb.pMMMb.   ,6"Yb.mmMMmm `7MM  ,pW"Wq.`7MMpMMMb.
           ,M  `MM    MM    MM   MM  6W'   `Wb MM    MM    MM  8)   MM  MM     MM 6W'   `Wb MM    MM
           AbmmmqMA   MM    MM   MM  8M     M8 MM    MM    MM   ,pm9MM  MM     MM 8M     M8 MM    MM
          A'     VML  MM    MM   MM  YA.   ,A9 MM    MM    MM  8M   MM  MM     MM YA.   ,A9 MM    MM
        .AMA.   .AMMA.`Mbod"YML. `Mbmo`Ybmd9'.JMML  JMML  JMML.`Moo9^Yo.`Mbmo.JMML.`Ybmd9'.JMML  JMML.''' + Fore.GREEN + VERSION + '''



                                                                                            - 𝘽𝙮 𝙍𝙤𝙝𝙖𝙣 '''
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

# BANNER
print(Style.BRIGHT + BANNER)
print(Style.RESET_ALL)

Graphical = ['graphical', 'Graphical', 'G', 'g']
Spider = ['Spider', 'spider', 'S', 's']
MATERIAL_SCRIPT_CODE = ['Material', 'material', 'M', 'm']
STATUS_SCRIPT_CODE = ['Status', 'status', 'S', 's']
PREDICTORS_SCRIPT_CODE = ['Predictor', 'predictor', 'P', 'p']
ATTENDANCE_SCRIPT_CODE = ['Automate', 'automate', 'A', 'a']
PERMISSION_APPLY_CODE = ['Apply', 'apply', 'ap', 'Ap', 'aP', 'AP']
PERMISSION_STATUS_CODE = ['Pstat', 'pstat', 'PSTAT', 'ps', 'Ps', 'pS']
EXIT_CODE = ['EXE', 'exe', 'e', 'E']


try:
    # NETWORK STATUS
    def CONNECTION_CHECK():
        try:
            urllib.request.urlopen('https://www.gitam.edu/')
            return True
        except:
            return False


    print('\n')

    print(Fore.LIGHTCYAN_EX + "Checking Internet Connectivity STATUS ~", end="")

    time.sleep(2)

    if (CONNECTION_CHECK()):

        print(Fore.GREEN + Style.BRIGHT + ' CONNECTION ESTABLISHED!')
        print(Style.RESET_ALL)
        # CALLING THE MAIN FUNCTION

        while True:
            print('\n\n')

            print(Fore.BLUE + Style.BRIGHT + '_____________________________Scripts_____________________________')
            print(Fore.RED + 'Script_Action{:>50}'.format('C o d e'))

            print(Fore.BLUE + Style.BRIGHT + '_________________________________________________________________')
            print(Fore.RED + '[ * ]' + Fore.WHITE + ' G-learn Materials{:>52}'.format(
                Fore.RED + 'Material || M'))

            print(Fore.RED + '[ * ]' + Fore.WHITE + ' Academic Attendance Status{:>41}'.format(
                Fore.RED + 'Status || S'))

            print(Fore.RED + '[ * ]' + Fore.WHITE + ' Attendance Analysis{:>51}'.format(
                Fore.RED + 'Predictor || P'))

            print(Fore.RED + '[ * ]' + Fore.WHITE + ' Attendance Automate{:>50}'.format(
                Fore.RED + 'Automate || A'))

            print(Fore.RED + '[ * ]' + Fore.WHITE + ' Apply for a Permission(VSP){:>40}'.format(
                Fore.RED + 'Apply || ap'))

            print(Fore.RED + '[ * ]' + Fore.WHITE + ' Permission Status{:>50}'.format(
                Fore.RED + 'pstat || ps'))

            print(Fore.RED + '[ * ]' + Fore.WHITE + ' Exit Code{:>56}'.format(
                Fore.RED + 'exe || e'))

            print('\n')
            option = input(Fore.BLUE + 'E N T E R  C O D E >> ').lower()

            print('\n\n')
            if option in ATTENDANCE_SCRIPT_CODE:
                while True:
                    control_flow = input(
                        'Enter ' + Fore.LIGHTCYAN_EX + Style.BRIGHT + "'Graphical||G'" + Style.RESET_ALL + ' for ' + Style.RESET_ALL + Fore.RED + 'Graphical Action,' + Style.RESET_ALL + Fore.LIGHTBLUE_EX + Style.BRIGHT + " 'Spider'||'S' " + Style.RESET_ALL + 'to deploy' + Fore.RED + " WebSpider : ").lower()
                    if control_flow in Graphical:
                        control_flow = '01'
                        main(control_flow)
                        break
                    elif control_flow in Spider:
                        control_flow = '10'
                        main(control_flow)
                        break
                    else:
                        print(Fore.RED + "Invalid input.\nRe-enter.")
                        continue


            elif option in MATERIAL_SCRIPT_CODE:
                MATERIAL_PY()
                break

            elif option in STATUS_SCRIPT_CODE:
                STATUS_PY()
                break
            elif option in PERMISSION_APPLY_CODE:
                PERMISSION_APPLY()
            elif option in PERMISSION_STATUS_CODE:
                PERMISSION_STAT()
            elif option in PREDICTORS_SCRIPT_CODE:

                print(Fore.RED+Style.BRIGHT+'\nNote ~ '+Fore.BLUE+" Deploying this script in 'Graphical-Mode' will be slower that anticipated.\n")

                while True:
                    control_flow = input(
                        'Enter ' + Fore.LIGHTCYAN_EX + Style.BRIGHT + "'Graphical||G'" + Style.RESET_ALL + ' for ' + Style.RESET_ALL + Fore.RED + 'Graphical Action,' + Style.RESET_ALL + Fore.LIGHTBLUE_EX + Style.BRIGHT + " 'Spider'||'S' " + Style.RESET_ALL + 'to deploy' + Fore.RED + " WebSpider : ").lower()
                    if control_flow in Graphical:
                        control_flow = '01'
                        PREDICTION(control_flow)
                        break
                    elif control_flow in Spider:
                        control_flow = '10'
                        PREDICTION(control_flow)
                        break
                    else:
                        print(Fore.RED + "Invalid input.\nRe-enter")
                        continue


            elif option in EXIT_CODE:
                print(Fore.RED + Style.BRIGHT + 'Exiting Code .. ')
                exit()

            else:
                print(Fore.RED + Style.BRIGHT + 'Invalid Script C0de ... ')
                continue






    else:
        print(Fore.RED + Style.BRIGHT + ' NO INTERNET')
        print(Fore.RED + Style.BRIGHT + 'Exiting Code ...\n')
        exit()


except KeyboardInterrupt:
    print(Fore.RED + Style.BRIGHT + '\n\nKeyboard Interruption !\nExiting Code . . .\n')


print(Style.RESET_ALL)



















