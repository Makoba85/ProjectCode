import tkinter as tk
from tkinter import *

def StartProgram():
    #create an instance of the frame
    root = tk.Tk()

    #giving the frame its geometric parameters
    root.geometry("1368x768")

    #frame title
    root.title("Feeding and Lighting System")

    #label for text within the frame
    label = tk.Label(root, text="Welcome to Light and Feeding Management System Dashboard", font=('Times New Roman', 25, 'bold'))

    #set label positioning for x and y axis
    label.pack(padx=20, pady=50)

    #drop down menu options list
    options = ["1 - 6 weeks old", "7 - 8 weeks old", "9 - 12 weeks old", "Above 12 weeks old"]
    #set the dropdown menu to the frame
    var = StringVar(root)
    #set default text for the dropdown menu
    var.set("Enter Chicken Age")

    #create an options menu and add the dropdown to the current frame. Set all the options from the options variable as the optins for the dropdown menu
    dropdown_menu = OptionMenu(root, var, *options)
    #add the dropdown menu to the frame
    dropdown_menu.pack()

    def start():
        selectedOption = var.get()
        print("Selected Option: ", selectedOption)

    startButton = tk.Button(root, text="Start", font=('Arial', 18), command=start)
    startButton.pack()
