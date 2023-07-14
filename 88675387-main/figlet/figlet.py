

from pyfiglet import Figlet
import random
import sys
figlet = Figlet()
font_l=figlet.getFonts()

if len(sys.argv)<2:
    fnt=random.choice(font_l)
    figlet.setFont(font=fnt)

elif len(sys.argv)>=2:
     if sys.argv[1] == '-f':
        if sys.argv[2] in font_l :
            figlet.setFont(font=(sys.argv[2]))
        else:
            sys.exit('Invalid usage')

     elif sys.argv[1] == '--font' :
        if sys.argv[2] in font_l :
            figlet.setFont(font=(sys.argv[2]))
        else:
            sys.exit('Invalid usage')
     else:
        sys.exit('Invalid usage')

word=input('ur string:  ')
print(figlet.renderText(word))