import os
import colorama
import json
import string
import time
colorama.init()
python_keywords = [
    "def", "return", "if", "elif", "else", "for", "while",
    "break", "continue", "pass", "in", "is", "not", "and", "or",
    "import", "from", "as", "class", "with", "try", "except",
    "finally", "raise", "lambda", "yield", "global", "nonlocal",
    "assert", "del"
]
python_types = [
    "int", "float", "str", "bool", "list", "tuple", "dict", "set",
    "None", "object", "type", "range", "bytes"
]
python_builtins = [
    "print", "len", "range", "type", "input", "open", "dir",
    "abs", "sum", "min", "max", "round", "isinstance", "id",
    "help", "sorted", "map", "filter", "zip", "enumerate",
    "any", "all", "eval", "exec", "chr", "ord", "bin", "hex"
]
python_literals = ["True", "False", "None"]
commandlist = ["/back","//back","/help","/edit","/backb","/editb","/autosave","/save","/load","/new","/quit","/run",":menu",":create",":change",":edit"]
alive = True
insertmode = False
text = ""
filename = ""
textsplitted = text.split(" ")
codesofar = []
# default config
keywordscon = 1
literalscon = 4
typescon = 2
builtinscon = 3
shortcutcon = ""
configusing = "cfg.ini"

def configloader(config):
    global keywordscon
    global builtinscon
    global typescon
    global shortcutcon
    global literalscon
    global configusing
    try:
        with open(config, "r") as cfg:
            keywordscon = data['keywords']
            typescon =  data['types']
            literalscon = data['literals']
            builtinscon = data['builtins']
            shortcutcon = data['shortcut']
    except:
        print("Wrong config name!")
        input()

def startup():
    global keywordscon
    global builtinscon
    global typescon
    global shortcutcon
    global literalscon
    global configusing
    try:
        with open("def.cfg", "r") as cfg:
            configusing = cfg.read()
    except Exception as e:
        with open("def.cfg", "w") as cfg:
            cfg.write("cfg.ini")
    try:
        with open(configusing, "w") as cfg:
            keywordscon = data['keywords']
            typescon = data['types']
            literalscon = data['literals']
            builtinscon = data['builtins']
            shortcutcon = data['shortcut']
    except:
        with open(configusing, "w") as cfg:
            data = {
                'keywords': keywordscon,
                'types': typescon,
                'literals': literalscon,
                'builtins': builtinscon,
                'shortcut': shortcutcon
            }
            json.dump(data, cfg)
            keywordscon = data['keywords']
            typescon = data['types']
            literalscon = data['literals']
            builtinscon = data['builtins']
            shortcutcon = data['shortcut']
    base_path = os.path.dirname(os.path.abspath("def.cfg"))
    path = os.path.join(base_path, "projects")
    os.makedirs(path,exist_ok=True)
def highligting(textspit = ""):
    for line in textspit:
        for word in line:
            stripp = word.strip(string.punctuation)
            if stripp in python_keywords:
                print(coloring(keywordscon,word))
            elif stripp in python_literals:
                print(coloring(literalscon,word))
            elif stripp in python_builtins:
                print(coloring(builtinscon,word))
            elif stripp in python_types:
                print(coloring(typescon,word))
            else:
                print(word, end=" ")
        print("")

def ui():
    print(f" Menu type :menu | WIDE | Help type /help")
def clearscren():
    os.system("cls" if os.name == "nt" else "clear")


def colorchanger(text):
    if (text == "1"):
        return 1
    if (text == "2"):
        return 2
    if (text == "3"):
        return 3
    if (text == "4"):
        return 4
    if (text == "5"):
        return 5
    if (text == "6"):
        return 6
    else:
        print("Unknown symbol")
        input()
        clearscren()
        return 5


def textchanger(text):
    if (text == "1"):
        return colorama.Fore.RED + "red" + colorama.Fore.RESET
    if (text == "2"):
        return colorama.Fore.BLUE + "blue" + colorama.Fore.RESET
    if (text == "3"):
        return colorama.Fore.GREEN + "green" + colorama.Fore.RESET
    if (text == "4"):
        return colorama.Fore.YELLOW + "yellow" + colorama.Fore.RESET
    if (text == "5"):
        return colorama.Fore.RESET + "white" + colorama.Fore.RESET
    if (text == "6"):
        return colorama.Fore.MAGENTA + "magenta" + colorama.Fore.RESET
def coloring(num , word):
    if (num == 1):
        return colorama.Fore.RED + word + colorama.Fore.RESET
    if (num == 2):
        return colorama.Fore.BLUE + word + colorama.Fore.RESET
    if (num == 3):
        return colorama.Fore.GREEN + word + colorama.Fore.RESET
    if (num == 4):
        return colorama.Fore.YELLOW + word + colorama.Fore.RESET
    if (num == 5):
        return colorama.Fore.RESET + word + colorama.Fore.RESET
    if (num == 6):
        return colorama.Fore.MAGENTA + word + colorama.Fore.RESET

startup()
print("loading..")
time.sleep(0.3)
while alive:
    clearscren()
    ui()
    highligting(codesofar)
    text = input()
    if text not in commandlist:
        textsplitted = text.split(" ")
        codesofar.append(textsplitted)
    else:
        if text == "//back":
            codesofar.pop()
        if text == "/quit":
            alive = False
        if text == "/new":
            filename = ""
            codesofar = []
            text = ""
        if text == "/run":
            if filename == "":
                filename = input("name of the file or save this one type /undo to exit: ")
                if filename == "/undo":
                    continue
            exec(open(filename).read())
        if text == "/back":
            last_line = codesofar[-1]
            if last_line:
                last_line.pop()
        if text == "/backb":
            num = input()
            last_line = codesofar[-int(num):]
            if last_line:
                last_line.pop()
        if text == "/edit":
            last_line = codesofar[-1]
            if last_line:
                last_line.pop()
                text = input()
                codesofar[-1].append(text)
        if text == "/editb":
            num = input()
            last_line = codesofar[-int(num):]
            for word in last_line:
                word.pop()
                text = input()
                codesofar[-1].append(text)
        if text == "/save":
            name = input("Name.py (doesnt have to be py but its py editor so i guess py): ")
            filename = name
            with open(name,"w") as f:
                for line in codesofar:
                    f.write(" ".join(line) + " \n")
        if text == "/autosave":
            if filename == "":
                print("no file to save to")
                continue
            with open(filename, "w") as f:
                for line in codesofar:
                    f.write(" ".join(line) + " \n")
        if text == "/load":
            name = input("Name.py (doesnt have to be py but its py editor so i guess py): ")
            filename = name
            codesofar = []
            with open(name,"r") as f:
                for line in f:
                    codesofar.append(line.strip().split())

        if text == "/help":
            print(r"""Commands: 
            /Help explains the commands 
            /back deletes last word 
            /backb deletes [x] last words
            //back deletes last line
            /edit deletes last word and lets you replace it or continue from that point
            /editb deletes [x] last words and lets you replace it or continue from that point
            /save save the file
            /autosave auto saves to the same file
            /load loads the file
            /quit quits the app
            /new creates new file
            /run runs code in python
                                """)
            input("...")
        if text == ":menu":
            print(f"""WIDE 1.5v 
            :create creates new config file
            :change changes the source config file
            :edit lets you edit config file
            :defcfg lets you write the name of the main config (automaticly using after start)
            :cfgreload reloads config
                                """)
            input("...")
        if text == ":create":
            text = input("Name the config: ")
            text = text + ".ini"
            with open(text, "x") as cfg:
                data = {
                    'keywords': 1,
                    'types': 2,
                    'literals': 3,
                    'builtins': 4,
                    'shortcut': "empty"
                }
                json.dump(data, cfg)
        if text == ":defcfg":
            text = input("Name the config: ")
            with open("def.cfg", "w") as cfg:
                cfg.write(text)
        if text == ":cfgreload":
           configloader(configusing)
        if text == ":edit":
            keywords = 1
            keywordstext = colorama.Fore.RED + "red" + colorama.Fore.RESET
            types = 2
            typestext = colorama.Fore.BLUE + "blue" + colorama.Fore.RESET
            builtins = 3
            builtinstext = colorama.Fore.GREEN + "green" + colorama.Fore.RESET
            literals = 4
            literalstext = colorama.Fore.YELLOW + "yellow" + colorama.Fore.RESET
            shortcut = ""
            localalive = True
            while localalive:
                ui()
                print(f"""
    Wide  | Config Editor | 0.1v
                for help type /help
        1.python_keywords: {keywordstext}
        2.python_types: {typestext}
        3.python_builtins: {builtinstext}
        4.python_literals: {literalstext}
        5.shortcuts: {shortcut}    
    
                                    """)
                text = input()
                clearscren()
                if (text == "/help"):
                    ui()
                    print(f"""
    /exit to exit (auto saves)
    
    /save to save
    
    type the number and then number of the color
                    
    [red 1 blue 2 green 3 yellow 4 white 5 magenta 6]
                    
    shortcut name the file
                        """)
                    input()
                if (text == "/exit"):
                    localalive = False
                    with open(f"{configusing}", "w") as cfg:
                        data = {
                            'keywords': keywords,
                            'types': types,
                            'literals': literals,
                            'builtins': builtins,
                            'shortcut': shortcut
                        }
                        json.dump(data, cfg)
                if (text == "/save"):
                    with open(f"{configusing}", "w") as cfg:
                        data = {
                           'keywords': keywords,
                            'types': types,
                            'literals': literals,
                            'builtins': builtins,
                            'shortcut': shortcut
                        }
                        json.dump(data, cfg)
                if (text == "1"):
                    ltext = input()
                    keywords = colorchanger(ltext)
                    keywordstext = textchanger(ltext)
                if (text == "2"):
                    ltext = input()
                    types = colorchanger(ltext)
                    typestext = textchanger(ltext)
                if (text == "3"):
                    ltext = input()
                    builtins = colorchanger(ltext)
                    builtinstext = textchanger(ltext)
                if (text == "4"):
                    ltext = input()
                    literals = colorchanger(ltext)
                    literalstext = textchanger(ltext)
                if (text == "5"):
                    ltext = input("Name of the shortcut file name.shr: ")
                    shortcut = ltext
                    if (ltext == ""):
                        shortcut = "empty"

        if text == ":change":
            text = input("Name the config: ")
            configloader(text)
