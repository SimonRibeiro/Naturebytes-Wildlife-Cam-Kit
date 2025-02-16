'''
Version 1.01 Dec 11th 2015
@author: Naturebytes My Submissions | Based on Burkhard Python GUIs
'''
#======================
# We plan to update these these basic GUIs to pull data directly from the Naturebytes website / community in the future.
# Naturebytes is an open and we release all our of hardware and software under Creative Commons licencing.
# If you'd like to help us update these GUIs and support the community please get in touch - info@naturebytes.org
#======================

#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import messagebox as mBox

# Creating an instance of tkinter
win = tk.Tk()   

# Adding a title       
win.title("My Submissions | Naturebytes")

# Adding our tabs -----------------------------------------
tabControl = ttk.Notebook(win)          # Defining our tab control

tab1 = ttk.Frame(tabControl)            # Define a tab ID to a frame 
tabControl.add(tab1, text='My Submissions')    # Add a tab and give it a title

tabControl.pack(expand=1, fill="both")  # Pack to make visible

# Next, we create a container frame to hold the tab's content
submissions_frame = ttk.LabelFrame(tab1, text=' Submit your photos to the Naturebytes website ') # Add a label  to the frame
submissions_frame.grid(column=0, row=0, padx=5, pady=12) # Add a little padding

# Add content (graphics) to the container frames we defined above (and add all the others)
photo1 = tk.PhotoImage(file="my_submissions.png") # Use PhotoImage to show a .png
ttk.Label(submissions_frame, image=photo1).grid(column=0, row=0, sticky='W') # Adding our photos to frames
        
# Exit the GUI cleanly
def _quit():
    win.quit()
    exit() 
    
# Creating a menu bar
menuBar = Menu(tab1)
win.config(menu=menuBar)

# Adding menu items to the bar
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

# Display a message box with our version     
def _msgbox():
 mBox.showinfo('About', 'Naturebytes | Version 1.01 2015')

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgbox)
menuBar.add_cascade(label="Help", menu=helpMenu)

#======================
# Start the GUI
#======================
win.mainloop()
