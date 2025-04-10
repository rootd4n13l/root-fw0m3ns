import pystyle
from pystyle import Colors, Colorate, Center
from ipwhois import IPWhois
import requests
import webbrowser

banner = """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
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
fuckosint = """
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || | _____  _____ | || |     ______   | || |  ___  ____   | || |              | || |     ____     | || |    _______   | || |     _____    | || | ____  _____  | || |  _________   | |
| | |_   ___  |  | || ||_   _||_   _|| || |   .' ___  |  | || | |_  ||_  _|  | || |              | || |   .'    `.   | || |   /  ___  |  | || |    |_   _|   | || ||_   \|_   _| | || | |  _   _  |  | |
| |   | |_  \_|  | || |  | |    | |  | || |  / .'   \_|  | || |   | |_/ /    | || |    ______    | || |  /  .--.  \  | || |  |  (__ \_|  | || |      | |     | || |  |   \ | |   | || | |_/ | | \_|  | |
| |   |  _|      | || |  | '    ' |  | || |  | |         | || |   |  __'.    | || |   |______|   | || |  | |    | |  | || |   '.___`-.   | || |      | |     | || |  | |\ \| |   | || |     | |      | |
| |  _| |_       | || |   \ `--' /   | || |  \ `.___.'\  | || |  _| |  \ \_  | || |              | || |  \  `--'  /  | || |  |`\____) |  | || |     _| |_    | || | _| |_\   |_  | || |    _| |_     | |
| | |_____|      | || |    `.__.'    | || |   `._____.'  | || | |____||____| | || |              | || |   `.____.'   | || |  |_______.'  | || |    |_____|   | || ||_____|\____| | || |   |_____|    | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""
choicing = """
.---.
| 1 | IP Analyze
'---'

.---.  
| 2 | Number Analyze
'---'

.---.  
| 3 | Telegram Analyze.
'---'

.---.    
| 4 | Image Analyze.              
'---'
"""

def imageanalyze():
    imageurlosint = "https://search4faces.com/"
    webbrowser.open(imageurlosint)


def ipanalyze(ip):
    result = {}

    try:
        geo = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719").json()
        result["Info (ip-api.com)"] = geo
    except Exception as e:
        result["Info (ip-api.com)"] = f"Error: {e}"

    try:
        obj = IPWhois(ip)
        whois = obj.lookup_rdap(depth=1)
        result["WHOIS Info (ipwhois)"] = whois
    except Exception as e:
        result["WHOIS Info (ipwhois)"] = f"Error during WHOIS lookup: {e}"

    return result

def main():
    print(Colorate.Horizontal(Colors.green_to_black, Center.XCenter(banner)))
    print(Colorate.Horizontal(Colors.green_to_black, Center.XCenter(fuckosint)))
    print(Colorate.Horizontal(Colors.green_to_black, Center.XCenter(choicing)))

    choice = input(Colorate.Horizontal(Colors.green_to_black, Center.XCenter("Enter your choice > ")))

    if choice == "1":
        ip = input(Colorate.Horizontal(Colors.green_to_black, Center.XCenter("Enter IP > ")))
        ipinfo = ipanalyze(ip)

        for section, data in ipinfo.items():
            print(f"\n== {section} ==")
            if isinstance(data, dict):
                for key, value in data.items():
                    print(f"{key}: {value}")
            else:
                print(data)
    elif choice == "2":
        print("In developing")
    elif choice == "3":
        print("In developing")
    elif choice == "4": 
        imageanalyze()

if __name__ == "__main__":
    main()
