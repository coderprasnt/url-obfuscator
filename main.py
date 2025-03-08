from colorama import Fore, Style

content = """This tool is made by coder prasant
Telegram- @witchshophub"""

border = """
**************************************
*                                    *
*                                    *
*                                    *
**************************************
"""

print(Fore.GREEN + border)
print(content.center(38)) 
print(border + Style.RESET_ALL)
