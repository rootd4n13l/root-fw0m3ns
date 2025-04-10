import os
import pystyle
from pystyle import Colors, Colorate, Center

banner = r"""XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XX                                                                          XX
XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
XX   MMMMMy''                                                    ''yMMMMM   XX
XX   MMMy'                                                          'yMMM   XX
XX   Mh'                                                              'hM   XX
XX   -                                                                  -   XX
XX                                                                          XX
XX   ::                                                                ::   XX
XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
XX                                oo      oo                                XX
XX           oM                 oo          oo                 Mo           XX
XX         oMMo                M              M                oMMo         XX
XX       +MMMM                 s              s                 MMMM+       XX
XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
XX   MMMMMMMM-                                                  -MMMMMMMM   XX
XX   MMMMMMMMM                                                  MMMMMMMMM   XX
XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX
XX                                                                          XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""

fwtext = r""" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || | _____  _____ | || |     ______   | || |  ___  ____   | || |              | || | _____  _____ | || |     ____     | || | ____    ____ | || |  _________   | || | ____  _____  | || |    _______   | |
| | |_   ___  |  | || ||_   _||_   _|| || |   .' ___  |  | || | |_  ||_  _|  | || |              | || ||_   _||_   _|| || |   .'    `.   | || ||_   \  /   _|| || | |_   ___  |  | || ||_   \|_   _| | || |   /  ___  |  | |
| |   | |_  \_|  | || |  | |    | |  | || |  / .'   \_|  | || |   | |_/ /    | || |    ______    | || |  | | /\ | |  | || |  /  .--.  \  | || |  |   \/   |  | || |   | |_  \_|  | || |  |   \ | |   | || |  |  (__ \_|  | |
| |   |  _|      | || |  | '    ' |  | || |  | |         | || |   |  __'.    | || |   |______|   | || |  | |/  \| |  | || |  | |    | |  | || |  | |\  /| |  | || |   |  _|  _   | || |  | |\ \| |   | || |   '.___`-.   | |
| |  _| |_       | || |   \ `--' /   | || |  \ `.___.'\  | || |  _| |  \ \_  | || |              | || |  |   /\   |  | || |  \  `--'  /  | || | _| |_\/_| |_ | || |  _| |___/ |  | || | _| |_\   |_  | || |  |`\____) |  | |
| | |_____|      | || |    `.__.'    | || |   `._____.'  | || | |____||____| | || |              | || |  |__/  \__|  | || |   `.____.'   | || ||_____||_____|| || | |_________|  | || ||_____|\____| | || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
 """

devment = """
 ▪   ▐ ▄     ·▄▄▄▄  ▄▄▄ . ▌ ▐·▄▄▄ .▄▄▌         ▄▄▄·• ▌ ▄ ·. ▄▄▄ . ▐ ▄ ▄▄▄▄▄         
██ •█▌▐█    ██▪ ██ ▀▄.▀·▪█·█▌▀▄.▀·██•  ▪     ▐█ ▄█·██ ▐███▪▀▄.▀·•█▌▐█•██           
▐█·▐█▐▐▌    ▐█· ▐█▌▐▀▀▪▄▐█▐█•▐▀▀▪▄██▪   ▄█▀▄  ██▀·▐█ ▌▐▌▐█·▐▀▀▪▄▐█▐▐▌ ▐█.▪         
▐█▌██▐█▌    ██. ██ ▐█▄▄▌ ███ ▐█▄▄▌▐█▌▐▌▐█▌.▐▌▐█▪·•██ ██▌▐█▌▐█▄▄▌██▐█▌ ▐█▌·         
▀▀▀▀▀ █▪    ▀▀▀▀▀•  ▀▀▀ . ▀   ▀▀▀ .▀▀▀  ▀█▄▀▪.▀   ▀▀  █▪▀▀▀ ▀▀▀ ▀▀ █▪ ▀▀▀  ▀  ▀  ▀
"""

choicing = """
•-----------
|
|
|
|
•______
"""
def secret():
    os.system("python3 tools/osint.py")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_black, Center.XCenter(banner)))
    print(Colorate.Horizontal(Colors.green_to_black, Center.XCenter(fwtext)))
    print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(devment)))
    select = input(Colorate.Horizontal(Colors.red_to_black, Center.XCenter("Enter. to leave...")))
    if select == "tvorozhok":
        secret()

def secret():
    os.system("python3 tools/osint.py")

if  __name__ == "__main__":
    main()
