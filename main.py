import tkinter as tk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials, firestore, auth

root = tk.Tk()

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


# Sign up function
def signUp():
    # Initialize Firebase app
    # Check if Firebase app has already been initialized
    if not firebase_admin._apps:
        cred = credentials.Certificate("C:\\Users\\Makoba Ngulube\\Desktop\\Project\\FinalYearProject\\finalyearproject-33d65-firebase-adminsdk-56scw-68db4b5227.json")
        firebase_admin.initialize_app(cred)

    db = firestore.client()

        # Check if any input fields are empty
    if not firstname.get() or not lastname.get() or not email.get():
        messagebox.showerror("Error", "All fields are required.")
        return
    try:
        user = auth.create_user(
            email=email.get(),
            password="password123", # Set a default password
            display_name=firstname.get() + " " + lastname.get()
        )
        print("Successfully created new user: {0}".format(user.uid))

        # Store user data in Firestore
        user_ref = db.collection("admins").document(user.uid)
        user_ref.set({
            "firstname": firstname.get(),
            "lastname": lastname.get(),
            "email": email.get()
        })
        print("Successfully stored user data in Firestore")


    except Exception as e:
        print("Error creating new user:", e)






def login():
    root.destroy()
    from login import beginProgramExecution
    beginProgramExecution()




button_frame = tk.Frame(root)
button_frame.pack()

# Sign up button
button = tk.Button(button_frame, text="Sign Up", font=('Arial', 18), bg="grey", command=signUp)
button.pack(side=tk.LEFT)

# Login button
login_button = tk.Button(button_frame, text="Login", font=('Arial', 18), bg="grey", command=login)
login_button.pack(side=tk.LEFT, padx=10) # Add some padding between the buttons

root.mainloop()
