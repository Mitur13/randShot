from tkinter import *
import webbrowser
import random
import string
import keyboard
import time

window = Tk()
window.title('Random LightShot')
window.geometry('300x80')

def get_random_string(size=2, chars=string.ascii_lowercase):	#define function to create random sting
    return ''.join(random.choice(chars) for i in range(size))	#return the string	

def openlink():
	keyboard.press_and_release('alt+tab')
	time.sleep(.5)
	keyboard.press_and_release('ctrl+w')
	two_letters = get_random_string(2)		#get string of 2 letters
	numbers = str(format(random.randint(0,9999), '04d'))
	mylink = ["http://prnt.sc/", two_letters, numbers]
	full_link = "".join(mylink)		#combining the list to create a link
	webbrowser.open(full_link)		#open a link in the browser
	print(full_link)

btnopenlink = Button(window,text="Open Random LightShot screenshot!", width=30,height=2,command=openlink).pack()

window.mainloop()