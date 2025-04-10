import os
import colorama
import time
import string
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
alive = True
insertmode = False
text = ""
filename = ""
textsplitted = text.split(" ")
codesofar = []

def highligting(textspit = ""):
    for line in textspit:
        for word in line:
            stripp = word.strip(string.punctuation)
            if stripp in python_keywords:
                print(colorama.Fore.RED + word + colorama.Fore.RESET, end=" ")
            elif stripp in python_literals:
                print(colorama.Fore.YELLOW + word + colorama.Fore.RESET, end=" ")
            elif stripp in python_builtins:
                print(colorama.Fore.GREEN + word + colorama.Fore.RESET, end=" ")
            elif stripp in python_types:
                print(colorama.Fore.BLUE + word + colorama.Fore.RESET, end=" ")
            else:
                print(word, end=" ")
        print("")

def ui():
    print(f" Welcome to Wide | Insert Mode: {insertmode} | Help: type /help")
def clearscren():
    os.system("cls" if os.name == "nt" else "clear")




while alive:
    clearscren()
    ui()
    highligting(codesofar)
    text = input()
    if text not in ["/back","//back","/help","/edit","/backb","/editb","/autosave","/save","/load","/new","/quit","/run"]:
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
                filename = input("name of the file or save this one type /undo to exit")
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
            name = input("Name.py (doesnt have to be py but its py editor so i guess py)")
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
            name = input("Name.py (doesnt have to be py but its py editor so i guess py)")
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

