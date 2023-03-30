import tkinter as tk
from tkinter import *
import serial

def StartProgram():
    #create an instance of the frame
    root = tk.Tk()

    #giving the frame its geometric parameters
    root.geometry("1368x768")

    #frame title
    root.title("Feeding and Lighting System")

    #label for text within the frame
    label = tk.Label(root, text="Welcome to Light and Feeding Management System Dashboard", font=('Times New Roman', 25, 'bold'))

    # logout functionality
    def logout():
        root.destroy()

    #logout button
    logoutButton = tk.Button(root, text="Logout", font=('Times New Roman', 12, 'bold'), command=logout)
    logoutButton.pack(padx=70, pady=0)




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

        if selectedOption == options[1]:
            serialInst = serial.Serial();
            serialInst.baudrate = 9600
            serialInst.port = 'COM12'
            serialInst.open()
            # create label outside of loop
            label = tk.Label(root, text="Light is OFF", font=('Times New Roman', 12, 'bold'))
            label.pack(padx=10, pady=0)
            while True:
                if serialInst.in_waiting > 0:
                    packet = serialInst.readline().decode('utf')
                    if "ON" in packet:
                        ledState = "ON"
                    else:
                        ledState = "OFF"
                    # update label text instead of creating new label
                    label.config(text="Light is " + ledState)
                    root.update()  # update the GUI to show the new label text

    startButton = tk.Button(root, text="Start", font=('Arial', 18), command=start)
    startButton.pack()
