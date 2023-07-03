import tkinter as tk
from tkinter import *
import serial
import serial.tools.list_ports

def StartProgram():
    root = tk.Tk()
    root.configure(bg='lightblue')
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.title("Dashboard")

    label = tk.Label(root, text="Welcome to Light and Feeding Management System User Interface", font=('Times New Roman', 25, 'bold'),bg='wheat', borderwidth=3, relief="groove", highlightthickness=3, highlightbackground="white")
    label.pack(padx=20, pady=50)

    # Define a list of options
    options = ["1 - 4 weeks", "5 - 8 weeks", "Above 8 weeks"]





    # Create a variable to store the selected option
    var = StringVar(root)
    var.set(options[0])  # Set the default selected option

    dropdown_menu = OptionMenu(root, var, *options)

    # Place the options menu widget in the root window
    dropdown_menu.pack()

    #checking the selected option
    def start():
        selectedOption = var.get()
        print('You selected '+selectedOption)

        if(selectedOption == 'Above 8 weeks'):
            # Configure the serial port
            ser = serial.Serial('COM12', 9600, timeout=1)

            while True:
                # Read data from the serial port
                data = ser.readline().decode().strip()

                if data:
                    if data == 'ON':
                        lightStatus.config(text='Poultry light is ON')
                    elif data == 'OFF':
                        lightStatus.config(text='Poultry light is OFF')
                    elif data == 'Turning':
                        feedingStatus.config(text='Feeding')
                    elif data == 'Done':
                        feedingStatus.config(text='Done Feeding')
                    elif data == "":
                        lightStatus.config(text='No data for lighting')
                        feedingStatus.config(text='No data for the feeding')
                root.update()

    button = tk.Button(root, text='Monitor', font=('Times New Roman', 25, 'bold'), command=start)
    button.pack(pady=30)

    lightLabel = tk.Label(root, text="Lighting Status", font=('Times New Roman', 25, 'bold'), borderwidth=5, relief="ridge")
    lightLabel.pack(side='left', padx=55)
    lightStatus = tk.Label(root, text="", font=('Times New Roman', 18))
    lightStatus.pack(side='left', pady=78)

    feedingLabel = tk.Label(root, text="Feeding Status", font=('Times New Roman', 25, 'bold'), borderwidth=5, relief="ridge")
    feedingLabel.pack(side="right", padx=55, pady=75)
    feedingStatus = tk.Label(root, text="", font=('Times New Roman', 18))
    feedingStatus.pack(side='right', padx=55, pady=90)


    root.mainloop()