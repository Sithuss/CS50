from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    tt = choice(fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" or sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    else:
        tt = sys.argv[2]
        
else:
    sys.exit("Invalid usage")

figlet.setFont(font=tt)

text = input("Input: ").strip()
print(figlet.renderText(text))
