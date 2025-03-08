from colorama import Fore, Style

# Content to be displayed
content = """This tool is made by coder prasant
Telegram- @witchshophub"""

# ASCII Art Border
border = """
**************************************
*                                    *
*                                    *
*                                    *
**************************************
"""

# Print the border and content in green
print(Fore.GREEN + border)
print(content.center(38))  # Center the content within the border
print(border + Style.RESET_ALL)
