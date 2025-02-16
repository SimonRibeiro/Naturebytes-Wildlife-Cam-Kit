'''
Version 1.01 Dec 11th 2015
@author: Naturebytes | Based on Burkhard Python GUIs
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
win.title("My Cam Kit | Naturebytes")

# Adding our tabs -----------------------------------------
tabControl = ttk.Notebook(win)          # Defining our tab control

tab1 = ttk.Frame(tabControl)            # Define a tab ID to a frame 
tabControl.add(tab1, text='Welcome')    # Add a tab and give it a title

tab2 = ttk.Frame(tabControl)            
tabControl.add(tab2, text='Inventory')   

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Test PIR')

tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text='Test Camera')

tab5 = ttk.Frame(tabControl)
tabControl.add(tab5, text='Placement')

tab6 = ttk.Frame(tabControl)
tabControl.add(tab6, text='Power')

tab7 = ttk.Frame(tabControl)
tabControl.add(tab7, text='Online')

tabControl.pack(expand=1, fill="both")  # Pack to make visible

# Next, we create a container frame to hold the tab's content
welcome_frame = ttk.LabelFrame(tab1, text=' Welcome ') # Add a label  to the frame
welcome_frame.grid(column=0, row=0, padx=5, pady=12) # Add a little padding

invent_frame = ttk.LabelFrame(tab2, text=' Inventory ')
invent_frame.grid(column=0, row=0, padx=5, pady=12)

testpir_frame = ttk.LabelFrame(tab3, text=' Test PIR ')
testpir_frame.grid(column=0, row=0, padx=5, pady=12)

testcam_frame = ttk.LabelFrame(tab4, text=' Test Camera ')
testcam_frame.grid(column=0, row=0, padx=5, pady=12)

placement_frame = ttk.LabelFrame(tab5, text=' Placement ')
placement_frame.grid(column=0, row=0, padx=5, pady=12)

power_frame = ttk.LabelFrame(tab6, text=' Power Management ')
power_frame.grid(column=0, row=0, padx=5, pady=12)

online_frame = ttk.LabelFrame(tab7, text=' Online ')
online_frame.grid(column=0, row=0, padx=5, pady=12)

# Add content (graphics) to the container frames we defined above (and add all the others)
photo1 = tk.PhotoImage(file="welcome.png") # Use PhotoImage to show a .png
ttk.Label(welcome_frame, image=photo1).grid(column=0, row=0, sticky='W') # Adding our photos to frames

photo2 = tk.PhotoImage(file="inventory.png")
ttk.Label(invent_frame, image=photo2).grid(column=0, row=0, sticky='W')

photo3 = tk.PhotoImage(file="testpir.png")
ttk.Label(testpir_frame, image=photo3).grid(column=0, row=0, sticky='W')

photo4 = tk.PhotoImage(file="testcamera.png")
ttk.Label(testcam_frame, image=photo4).grid(column=0, row=0, sticky='W')

photo5 = tk.PhotoImage(file="placement.png")
ttk.Label(placement_frame, image=photo5).grid(column=0, row=0, sticky='W')

photo6 = tk.PhotoImage(file="power.png")
ttk.Label(power_frame, image=photo6).grid(column=0, row=0, sticky='W')

photo7 = tk.PhotoImage(file="online.png")
ttk.Label(online_frame, image=photo7).grid(column=0, row=0, sticky='W')
        
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
