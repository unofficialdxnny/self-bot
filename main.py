import time 
import pyautogui as pag
import os
## import math 
import random
import keyboard as kb
import mouse

class bcolors:
    HEADER = '\033[93m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

banner = '''

\033[93m ╔═╗╔═╗╦  ╔═╗ \033[94m  ╔╗ ╔═╗╔╦╗                           
\033[93m ╚═╗║╣ ║  ╠╣──\033[94m──╠╩╗║ ║ ║                            
\033[93m ╚═╝╚═╝╩═╝╚   \033[94m  ╚═╝╚═╝ ╩                            
\033[93m ┌┐ ┬ ┬ \033[94m ┬ ┬┌┐┌┌─┐┌─┐┌─┐┬┌─┐┬┌─┐┬  ┌┬┐─┐ ┬┌┐┌┌┐┌┬ ┬
\033[93m ├┴┐└┬┘  \033[94m│ │││││ │├┤ ├┤ ││  │├─┤│   ││┌┴┬┘││││││└┬┘
\033[93m └─┘ ┴   \033[94m└─┘┘└┘└─┘└  └  ┴└─┘┴┴ ┴┴─┘─┴┘┴ └─┘└┘┘└┘ ┴ 
'''

os.system('color 1')

os.system('cls')

print(banner)

x = int(input('Please type in the X axis : '))
print('')
y = int(input('Please type in the Y axis : '))
print('')
amount = float(input('Type in number for this to run'))
print('')
while True:
    os.system('cls')
    print(banner)
    pag.dragTo(x, y)
    mouse.click()
    kb.write('''
  
trading retro star platinum over heaven,
volcanic golden experience requiem,
tusk act four and ender king crimson; No 🤡 offers    

    ''')
    amount -= 1
    print(f'Finished one cycle. {amount} left to go.')
    t = random.randint(420, 540)
    time.sleep(t)
