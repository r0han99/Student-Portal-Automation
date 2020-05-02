from main import *
from material import *
from status import *
from permission import *
from permissionstatus import *
from prediction import *
import urllib.request
from colorama import Fore, Style

import time

VERSION = '~ 1.0.0'

BANNER = Fore.GREEN+ '''

    Student Portal '''+Fore.RED+'''
                                                                               ,,
              db                 mm                                     mm     db
             ;MM:                MM                                     MM
            ,V^MM.  `7MM  `7MM mmMMmm ,pW"Wq.`7MMpMMMb.pMMMb.   ,6"Yb.mmMMmm `7MM  ,pW"Wq.`7MMpMMMb.
           ,M  `MM    MM    MM   MM  6W'   `Wb MM    MM    MM  8)   MM  MM     MM 6W'   `Wb MM    MM
           AbmmmqMA   MM    MM   MM  8M     M8 MM    MM    MM   ,pm9MM  MM     MM 8M     M8 MM    MM
          A'     VML  MM    MM   MM  YA.   ,A9 MM    MM    MM  8M   MM  MM     MM YA.   ,A9 MM    MM
        .AMA.   .AMMA.`Mbod"YML. `Mbmo`Ybmd9'.JMML  JMML  JMML.`Moo9^Yo.`Mbmo.JMML.`Ybmd9'.JMML  JMML.'''+Fore.GREEN+VERSION+ '''
        
                                                                                                        
                                                                                                      
                                                                                            - 𝘽𝙮 𝙍𝙤𝙝𝙖𝙣 '''


# BANNER
print(Style.BRIGHT+BANNER)
print(Style.RESET_ALL)

Graphical = ['graphical', 'Graphical','G','g']
Spider= ['Spider', 'spider','S','s']
MATERIAL_SCRIPT_CODE = ['Material', 'material', 'M', 'm']
STATUS_SCRIPT_CODE = ['Status', 'status', 'S', 's']
PREDICTORS_SCRIPT_CODE = ['Predictor', 'predictor', 'P', 'p']
ATTENDANCE_SCRIPT_CODE = ['Automate', 'automate', 'A', 'a']
PERMISSION_APPLY_CODE = ['Apply','apply','ap','Ap','aP','AP']
PERMISSION_STATUS_CODE = ['Pstat','pstat','PSTAT','ps','Ps','pS']
EXIT_CODE = ['EXE','exe','e','E']


# NETWORK STATUS
def CONNECTION_CHECK():
    try:
        urllib.request.urlopen('https://www.gitam.edu/')
        return True
    except:
        return False

print('\n')



print(Fore.LIGHTCYAN_EX+"Checking Internet Connectivity STATUS ~",end="")

time.sleep(2)


try:
    if (CONNECTION_CHECK()):

        print(Fore.GREEN + Style.BRIGHT + ' CONNECTION ESTABLISHED!')
        print(Style.RESET_ALL)
        # CALLING THE MAIN FUNCTION

        while True:
            print('\n\n')

            print(Fore.BLUE + Style.BRIGHT + '_____________________________Scripts_____________________________')
            print(Fore.RED + 'Script_Action{:>50}'.format('C o d e'))

            print(Fore.BLUE + Style.BRIGHT + '_________________________________________________________________')
            print(Fore.RED + '[ * ]' + Fore.WHITE + ' 𝗚-𝗟𝗲𝗮𝗿𝗻 𝗠𝗮𝘁𝗲𝗿𝗶𝗮𝗹𝘀{:>49}'.format(
                Fore.RED + '𝗠𝗮𝘁𝗲𝗿𝗶𝗮𝗹 || 𝗠'))

            print(Fore.RED + '[ * ]' + Fore.WHITE + ' 𝗔𝗰𝗮𝗱𝗲𝗺𝗶𝗰 𝗦𝘁𝗮𝘁𝘂𝘀{:>49}'.format(
                Fore.RED + '𝗦𝘁𝗮𝘁𝘂𝘀 || 𝗦'))

            print(Fore.RED + '[ * ]' + Fore.WHITE + ' 𝗔𝘁𝘁𝗲𝗻𝗱𝗮𝗻𝗰𝗲 𝗣𝗿𝗲𝗱𝗶𝗰𝘁𝗼𝗿{:>47}'.format(
                Fore.RED + '𝗣𝗿𝗲𝗱𝗶𝗰𝘁𝗼𝗿 || 𝗣'))

            print(Fore.RED + '[ * ]' + Fore.WHITE + ' 𝗔𝘁𝘁𝗲𝗻𝗱𝗮𝗻𝗰𝗲 𝗔𝘂𝘁𝗼𝗺𝗮𝘁𝗲{:>47}'.format(
                Fore.RED + '𝗔𝘂𝘁𝗼𝗺𝗮𝘁𝗲 || 𝗔'))

            print(Fore.RED + '[ * ]' + Fore.WHITE + ' 𝗔𝗽𝗽𝗹𝘆 𝗳𝗼𝗿 𝗣𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻{:>44}'.format(
                Fore.RED + '𝗔𝗽𝗽𝗹𝘆 || 𝗮𝗽'))

            print(Fore.RED + '[ * ]' + Fore.WHITE + ' 𝗣𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻 𝗦𝘁𝗮𝘁𝘂𝘀{:>47}'.format(
                Fore.RED + '𝗽𝘀𝘁𝗮𝘁 || 𝗽𝘀'))

            print(Fore.RED + '[ * ]' + Fore.WHITE + ' 𝗘𝘅𝗶𝘁 𝗖𝗼𝗱𝗲{:>52}'.format(
                Fore.RED + '𝗲𝘅𝗲 || 𝗲'))

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
                print(Style.RESET_ALL)
                exit()

            else:
                print(Fore.RED + Style.BRIGHT + 'Invalid Script C0de ... ')
                continue






    else:
        print(Fore.RED + Style.BRIGHT + ' NO INTERNET')
        print(Fore.RED + Style.BRIGHT + 'Exiting Code ...\n')
        exit()


except KeyboardInterrupt:
    
   
    print(Fore.RED + Style.BRIGHT + '\nKeyboard Interruption !\nExiting Code . . .\n')




















