import math, json, random as rand, sys, subprocess, time, os, webbrowser

def clamp(x, low=0, high=100):
    return max(low, min(x, high))

try:
    with open('settings.json', 'r') as f:
        settings = json.load(f)
        settingsFound = True
except FileNotFoundError:
    settingsFound = False
    settings = {
        "engine": "google"
    }
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

def save_config():
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

def info():
    clear_terminal()
    print('-~-~-~-~ System Info ~-~-~-~-')
    print('')
    print('Computer name:')
    os.system('hostname')
    print('')
    print('System Information:')
    os.system('systeminfo')
    print('')
    print('Network Information:')
    os.system('ipconfig /all')
    print('')
    check = input('Would you like to exit? (y/n)')
    if check == 'y':
        Main()
    else:
        print('Reanalysing data')
        time.sleep('1')
        info()


def browser():
    clear_terminal()
    engine = ('')
    if settingsFound == True:
        engine = settings["engine"]
    else:
        engine = "google"
    while True:
        print('-~-~-~-~ BOWSER THE BROWSER ~-~-~-~-')
        print('')
        print('Your current engine is', engine + '!')
        print('this can be changes with ![engine name]')
        print('')
        query = input('Search or URL: ').strip()

        if '.' in query:
            if not query.startswith("http://") and not query.startswith("https://"):
                query = "https://" + query
            webbrowser.open(query)
        elif '!' in query:
            engine = query.replace('!', '')
            settings["engine"] = engine
            save_config()
            clear_terminal()
            continue
        else:
            url = "https://www." + engine + ".com/search?q=" + query.replace(" ", "+")
            webbrowser.open(url)
        break
    Main()

def calc():
    clear_terminal()
    print('-~-~-~-~ TERMOS CALCULATOR ~-~-~-~-')
    print('')
    while True:
        num1 = float(input('Input your first number: '))
        num2 = float(input('Input your second number: '))
        operator = input('What operation do you want to do? (+,-,/,^,*,sqrt): ')

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '^':
            result = num1 ** num2
        elif operator == '*':
            result = num1 * num2
        elif operator == 'sqrt':
            result = math.sqrt(num1)
            print('sqrt has removed num2 from the equation due to it being unnessissary')
        
        if operator == 'sqrt':
            print('')
            print(str(operator) + '(' + str(num1) + ')', '=', result)
        else:
            print(num1, operator, num2, '=', result)

        check = input('Would you like to exit? (y/n)')
        if check == 'y':
            Main()
        else:
            continue

def appDir():
    clear_terminal()
    while True:
        print('-~-~-~-~ TERMOS APP DIRECTORY ~-~-~-~-')
        print('')
        print('[0] Home')
        print('[1] Calculator')
        print('[2] Bowser Browser')
        print('[3] Terminal')
        print('[4] Notepad')
        print('[5] Viewpoint')
        print('[6] Rule34dle')
        print('[7] Geoguessr')
        print('[8] Wordle')
        a = str(input('Input an application: ')).lower()
        if a in ["1", 'calc', 'calculator']:
            calc()
        elif a in ['0', 'home']:
            Main()
        elif a in ['2', 'browser', 'bowser', 'bowser browser']:
            browser()
        elif a in ["3", "terminal", 'console', 'cmd']:
            clear_terminal()
            try:
                subprocess.Popen(['C:\\Windows\\System32\\cmd.exe']) 
            except FileNotFoundError:
                print("Application not found at the specified path.")
        elif a in ['4', 'notes', 'note', 'notepad']:
            try:
                subprocess.Popen(['C:\\Windows\\notepad.exe']) 
                continue
            except FileNotFoundError:
                print("Application not found at the specified path.")
        elif a in ['5', 'vp', 'viewpoint']:
            webbrowser.open("https://suvicorpo.github.io")
            continue
        elif a in ['6', 'rule34dle']:
            webbrowser.open("https://rule34dle.vercel.app")
            continue
        elif a in ['7', 'geoguessr']:
            webbrowser.open("https://www.geoguessr.com/")
            continue
        elif a in ['8', 'wordle']:
            webbrowser.open("https://www.nytimes.com/games/wordle/index.html")
            continue
        else:
            check = input('Would you like to exit? (y/n)')
            if check == 'y':
                Main()
            else:
                continue

def restart():
    clear_terminal()
    subprocess.Popen([sys.executable] + sys.argv)
    sys.exit()

def clear_terminal():
    os.system('clear')

def Main():
    clear_terminal()
    print(' ______   ______     ______     __    __     ______     ______    ')
    print('/\__  _\ /\  ___\   /\  == \   /\ "-./  \   /\  __ \   /\  ___\   ')
    print('\/_/\ \/ \ \  __\   \ \  __<   \ \ \-./\ \  \ \ \/\ \  \ \___  \  ')
    print('   \ \_\  \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\  \/\_____\ ')
    print('    \/_/   \/_____/   \/_/ /_/   \/_/  \/_/   \/_____/   \/_____/ ')
    print('')
    print('               -~-~-~-~ WELCOME TO TERMOS ~-~-~-~-')
    print('')
    cmd = input('Input a command (Type "help" for a list of commands): ')
    if cmd.startswith("cmd."):
        command = cmd[4:]
        os.system(command)
        time.sleep(1)
        Main()
        return
    
    if cmd.startswith("shell."):
        command = cmd[4:]
        os.system(command)
        time.sleep(1)
        Main()
        return
    
    if cmd == '':
        conf = input('Are you sure? (y/n) ')
        if conf == 'y':
            print('Closing TermOS')
            time.sleep(1)
            sys.exit()
        else: Main()
    elif cmd == 'rule34dle':
        webbrowser.open("https://rule34dle.vercel.app")
        Main()
    elif cmd == 'viewpoint' or cmd == 'vp':
        webbrowser.open("https://suvicorpo.github.io")
        Main()
    elif cmd == 'cmd':
        clear_terminal()
        try:
            subprocess.Popen(['C:\\Windows\\System32\\cmd.exe']) 
        except FileNotFoundError:
            print("Application not found at the specified path.")
    elif cmd == 'note':
        try:
            subprocess.Popen(['C:\\Windows\\notepad.exe']) 
        except FileNotFoundError:
            print("Application not found at the specified path.")
    elif cmd == 'help':
        clear_terminal()
        print('-~-~-~-~ TERMOS HELP ~-~-~-~-')
        print('')
        print('Commands:')
        print('"help" - Opens this dialogue')
        print('"info" - displays the system info')
        print('"app" - Opens the TermOS app launcher')
        print('Windows commands can be run with "cmd.[command]"')
        print('')
        input('Press [Enter] to return home')
        Main()
    elif cmd == 'info':
        info()
    elif cmd == 'restart' or cmd == 'reboot':
        conf = input('Are you sure? (y/n) ')
        if conf == 'y':
            restart()
        else:
            Main()
    elif cmd == 'web':
        browser()
    #elif cmd == 'floof':
    #    webbrowser.open() ## need add link to a photo of Louis
    #    Main()
    elif cmd == 'calc':
        calc()
    elif cmd == 'app':
        appDir()
    else:
        print('ERROR: Command not found')
        time.sleep(1)
        Main()

def Load():
    clear_terminal()
    loaded = 0
    loaded = clamp(loaded, 0, 100)
    while loaded <= 100:
        print('Loading:', str(loaded) + '%')
        loaded += rand.randint(0, 6)
        time.sleep(rand.randint(0, 1))
    if loaded >= 100:
        print('Loaded 100% - Starting TermOS')
        time.sleep(2)
        Main()

Load()