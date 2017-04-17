from tkinter import *
from textbox import TextBox
from button import CButton

# Define the frame
top = Tk()
top.resizable(width=False, height=False)
top.geometry('{}x{}'.format(400, 256)) # Formatted as W * H
top.wm_title("DATBOI v0.5.0")
top["background"] = "#263238"

buttons = []

graphics = [] # Button graphics
graphics.append(PhotoImage(file="assets/gears.png"))
graphics.append(PhotoImage(file="assets/wifi.png"))
graphics.append(PhotoImage(file="assets/about.png"))
graphics.append(PhotoImage(file="assets/debug.png"))

# Canvas items
canvas_items = list()

# Logo thing
datBoi = PhotoImage(file="assets/datboi.png")

# Create tab buttons
for i in range(len(graphics)):
	configButton = Button(top, border=0, highlightthickness=0)
	configButton["background"] = "#37474F"
	configButton["activebackground"] = "#37474F"
	configButton["highlightbackground"] = "#37474F"
	configButton["relief"] = "flat"
	configButton.config(image=graphics[i])
	configButton.place(x=0, y=i*32, width=32, height=32)
	canvas_items.append(list())
	buttons.append(configButton)

# Create canvas to render on
renderCanvas = Canvas(top, highlightthickness=0)
renderCanvas["background"] = "#263238"
renderCanvas.place(x=32, width=368, height=256)

# Current tab
currentTab = 0

# Automated fun stuff. Disable all other button 
# elements from showing except the current tab
def checkOpen(button):
	for i in range(len(graphics)):
		if i != button:
			buttons[i]["background"] = "#37474F"
			buttons[i]["activebackground"] = "#37474F"
			
			for j in range(len(canvas_items[i])):
				renderCanvas.itemconfig(canvas_items[i][j], state=HIDDEN)

		else:
			buttons[button]["background"] = "#263238"
			buttons[button]["activebackground"] = "#263238"

			for j in range(len(canvas_items[button])):
				renderCanvas.itemconfig(canvas_items[button][j], state=NORMAL)

			global currentTab 
			currentTab = button

# Add an item with its ID from the 
# canvas to the object array
def add_item(item, indx=currentTab):
	canvas_items[currentTab].append(item)

####MAIN TAB
renderCanvas.create_image(270, 130, image=datBoi)

add_item(renderCanvas.create_text(30, 24, fill="#FFFFFF", text="Access Point Configuration", anchor="w", font=("assets/Roboto-Regular", 18, "normal")))
	
ssid_textbox = TextBox(renderCanvas, 112, 80, "SSID Name")
passwd_textbox = TextBox(renderCanvas, 112, 145, "Password", True)

for item in ssid_textbox.get_items():
	add_item(item)

for item in passwd_textbox.get_items():
	add_item(item)

start_button = CButton(renderCanvas, 172, 210, lambda: print("ayy"))
add_item(start_button.get_tag())
###END MAIN

# Left click mouse events
def click(event):
	x, y = event.x, event.y
	if currentTab == 0:
		if ssid_textbox.click(x, y):
			ssid_textbox.set_active(True, True)
		else:
			ssid_textbox.set_active(False, False)

		if passwd_textbox.click(x, y):
			passwd_textbox.set_active(True, True)
		else:
			passwd_textbox.set_active(False, False)
		
		if start_button.click(x, y):
			start_button.func()

# Keybinding events
def key(event):
	if currentTab == 0:
		if ssid_textbox.get_active():
			ssid_textbox.key(event)
		elif passwd_textbox.get_active():
			passwd_textbox.key(event)

top.bind_all("<Key>", key)	
top.bind("<Button-1>", click)

# Tab opening functions
def openMain(button):
	checkOpen(button)

def openClients(button):
	checkOpen(button)

def openAbout(button):
	checkOpen(button)

def openDebug(button):
	checkOpen(button)

# Spacing stuff for fanciness
strip = Label(top)
strip.place(y=4 * 32, width=32, height=128)
strip["background"] = "#37474F"

# Set button commands
buttons[0]["command"] = lambda: openMain(0)
buttons[1]["command"] = lambda: openClients(1)
buttons[2]["command"] = lambda: openAbout(2)
buttons[3]["command"] = lambda: openDebug(3)

# Open to the Main tab by default
buttons[0].invoke()

# Run the main window
top.mainloop()