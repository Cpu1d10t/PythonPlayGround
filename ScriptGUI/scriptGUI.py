# Trying to add Multiple .py scripts to Buttons in the Gui also adding a prompt and a Image
 

#         _          __________                              _,
#     _.-(_)._     ."          ".      .--""--.          _.-{__}-._
#   .'________'.   | .--------. |    .'        '.      .:-'`____`'-:.
#  [____________] /` |________| `\  /   .'``'.   \    /_.-"`_  _`"-._\
#  /  / .\/. \  \|  / / .\/. \ \  ||  .'/.\/.\'.  |  /`   / .\/. \   `\
#  |  \__/\__/  |\_/  \__/\__/  \_/|  : |_/\_| ;  |  |    \__/\__/    |
#  \            /  \            /   \ '.\    /.' / .-\                /-.
#  /'._  --  _.'\  /'._  --  _.'\   /'. `'--'` .'\/   '._-.__--__.-_.'   \
# /_   `""""`   _\/_   `""""`   _\ /_  `-./\.-'  _\'.    `""""""""`    .'`\
#(__/    '|    \ _)_|           |_)_/            \__)|        '       |   |
#  |_____'|_____|   \__________/   |              |;`_________'________`;-'
#   '----------'    '----------'   '--------------'`--------------------`




import sys
import os
from tkinter import *
import HelloWorld
import GoodBye
import tkinter as tk 

window=Tk()
window.title("Running Python Script")
#window.geometry('400x200')
prompt='SELECT A PYTHON SCRIPT!'        
label=tk.Label(window,text=prompt, bg='white')
label.grid(row=0, column=0)
image = tk.PhotoImage(file="Excited Mob.gif")
label1 = tk.Label(window,image=image)
label1.grid(row=0, column=4)
def Hello():
    HelloWorld.Hello()   
def main():
    GoodBye.main()

btn = Button(window, text="Click Me", bg="black", fg="white",command=Hello)
btn.grid(column=0, row=1)
btn2 = Button(window, text='Click Me', bg = 'green', fg='white', command=main)
btn2.grid(column=0, row=2)
window.mainloop()


