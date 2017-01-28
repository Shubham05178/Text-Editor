#Author Shubham Nagaria. ShubhamLabs.
#Coder.
#subhamnagaria@gmail.com        

import tkinter
from tkinter import *
from tkinter import Tk, scrolledtext, filedialog, messagebox

root = Tk(className=" TextEditor-ShubhamLabs") #name your texteditor in quotes
textPad = scrolledtext.ScrolledText(root, width=100, height=80)

#Defining Menu bar and sub-commands
def about():
	win = Tk()
	win.wm_title("About")
	frame1 = Frame(
    	master = win,
    	bg = '#800000'
		)
	
	frame1.pack(fill='both', expand='yes')
	editArea = Text(
        master = frame1,
    	wrap   = WORD,
    	width  = 30,
		height = 15)
	#Don't use widget.place(), use pack or grid instead, since
	# They behave better on scaling the window -- and you don't
	# have to calculate it manually!
	editArea.pack(padx=10, pady=10, fill=BOTH, expand=True)
	# Adding some text in About.
	editArea.insert(INSERT,
	"""
	This Software was created by Shubham Nagaria as a final year undergrad at GLA University,Mathura. This software was programmed in Python 3.5. Tkinter was used to create GUI version. subhamnagaria@gmail.com, mail me for doubts, queries or any other stuff.
	""")
	editArea.configure(state='disable') #To make ScrolledText read-only, unlike our root window.
	win.mainloop()


def save_file():
    file = filedialog.asksaveasfile(mode='w')
    if file != None:
    # chop the last character from get, as an added extra return
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()
        
def open_file():
        file = filedialog.askopenfile(parent=root,mode='rb',title='Select file')
        if file != None:
            contents = file.read()
            textPad.insert('1.0',contents)
            file.close()
            
def exit_file():
    if messagebox.askokcancel("Exit", """Are you sure you want to exit?
Shubhamlabs thanks you for using our Code."""):
        root.destroy()



def begin(): #just to ensure code is running correctly.
    print ("Shubhamlabs thanks you for using our code.")

#Adding menus to our text editor.
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=begin)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_file)
help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

textPad.pack()#we pack everything :P

root.mainloop() #we run script in loop.
