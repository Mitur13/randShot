from tkinter import *
import tkinter.messagebox
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
	keyboard.press_and_release('alt+tab')	#focus back on browser window
	time.sleep(.5)
	keyboard.press_and_release('ctrl+w')	#close the previous browser tab (works with Edge)
	two_letters = get_random_string(2)		#get string of 2 letters
	numbers = str(format(random.randint(0,9999), '04d'))	#generate string of digits 0000-9999
	mylink = ["http://prnt.sc/", two_letters, numbers]	
	global full_link			#makes it possible to pull full_link outside this function
	full_link = "".join(mylink)		#combining the list to create a link
	webbrowser.open(full_link)		#open a link in the browser
	print(full_link)		#print the link in the command line (history)


def savelink():			#saves the current link to .txt file
	fin = open("Saved_Links.txt", "a")

	savelink = Tk()	#open new window asking for user input

	# savelink.title("Add comment")
	#comment = Entry

	tkinter.messagebox.showinfo("Link saved", "Link succefully saved to Saved_Links.txt")	### Popup with text input window - 'Add note to the link' - save in file along the link
	fin.write(full_link + comment)	#pass input to 
	fin.close()
	savelink.mainloop()

btnopenlink = Button(window,text="Open Random LightShot screenshot!", width=30,height=2,command=openlink).pack()

btnsavelink = Button(window,text="Save current link", width=25,height=1,command=savelink)
btnsavelink.place(relx=0.5, y=60, anchor=CENTER)

window.mainloop()