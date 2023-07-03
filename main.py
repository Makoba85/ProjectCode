import tkinter as tk
from tkinter import messagebox
from login import beginProgramExecution
import firebase_admin
from firebase_admin import credentials, firestore, auth

backgroundcolor = '#90EE90'
root = tk.Tk()
root.configure(bg=backgroundcolor)
root.geometry("500x400") # Set the size of the root window
root.resizable(False, False) # Disable resizing of the window
root.title("Registration Form") # Set the title of the window
root.attributes('-alpha', 2) # Set the opacity of the window

# Set the border radius of the root window
root.configure(borderwidth=10, relief="ridge")

# Add label at the top of the frame
title_label = tk.Label(root, text="Sign Up/Login", font=('Arial', 24, 'bold'), bg=backgroundcolor)
title_label.pack(pady=20)



# Create new user
def on_entry_click(event, entry):
    if entry.get() == "Enter Your {} here".format(entry.name):
        entry.delete(0, "end") # delete all the text in the entry
        entry.insert(0, '') #Insert blank for user input

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.bind('<FocusIn>', self.on_entry_click)
        self.bind('<FocusOut>', self.on_focus_out)
        self.insert(0, self.placeholder)
        self.config(fg='grey')

    def on_entry_click(self, event):
        if self.get() == self.placeholder:
            self.delete(0, "end")
            self.config(fg='black')

    def on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg='grey')

# First name entry
firstname = EntryWithPlaceholder(root, name="firstName", width=30, font=('Times New Roman', 30), placeholder="Enter Your FirstName here")
firstname.pack()

# Last name entry
lastname = EntryWithPlaceholder(root, name="lastName", width=30, font=('Times New Roman', 30), placeholder="Enter Your LastName here")
lastname.pack(pady=20)

# Email entry
email = EntryWithPlaceholder(root, name="email", width=30, font=('Times New Roman', 30), placeholder="Enter Your Email here")
email.pack(pady=20)

#text widget for displaying the text
text_label = tk.Label(root, text='Click the login if you already have an account', font=('Arial', 14), bg=backgroundcolor)
text_label.pack(padx=15)


# Sign up function
def signUp():
    # Initialize Firebase app
    # Check if Firebase app has already been initialized
    if not firebase_admin._apps:
        cred = credentials.Certificate("C:\\Users\\Makoba Ngulube\\Desktop\\Project\\FinalYearProject\\fir-vue-72fd8-firebase-adminsdk-ibkku-05e683ef03.json")
        firebase_admin.initialize_app(cred)

    db = firestore.client()

        # Check if any input fields are empty
    if not firstname.get() or not lastname.get() or not email.get() or firstname.get() == firstname.placeholder or lastname.get() == lastname.placeholder or email.get() == email.placeholder:
        messagebox.showerror("Error", "All fields are required.")
        return
    try:
        user = auth.create_user(
            email=email.get().lower(),
            # password="password123", # Set a default password
            display_name=firstname.get().lower() + " " + lastname.get().lower()
        )
        print("Successfully created new user: {0}".format(user.uid))

        # Store user data in Firestore
        user_ref = db.collection("admins").document(user.uid)
        user_ref.set({
            "firstname": firstname.get().lower(),
            "lastname": lastname.get().lower(),
            "email": email.get().lower()
        })
        messagebox.showinfo("Registration Status" , "Registration successful")
        root.destroy()
        beginProgramExecution()

    except Exception as e:
        messagebox.showerror("Registration Status", "Error creating new user:"+str(e))


def login():
    root.destroy()
    beginProgramExecution()

button_frame = tk.Frame(root)
button_frame.pack()

# Sign up button
button = tk.Button(button_frame, text="Sign Up", font=('Arial', 18), bg="grey", command=signUp)
button.pack(side=tk.LEFT, padx=10)

# Login button
login_button = tk.Button(button_frame, text="Login", font=('Arial', 18), bg="grey", command=login)
login_button.pack(side=tk.LEFT, padx=10) # Add some padding between the buttons

root.mainloop()
