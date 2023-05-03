#all the import statements
import tkinter as tk
from PIL import ImageTk, Image
import serial.tools.list_ports
from dashboard import StartProgram

def beginProgramExecution():

    # creating an instance of the window frame
    root = tk.Tk()

    image = Image.open("jakub-pabis-lQknQP3R1yc-unsplash.jpg")
    bg_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    root.geometry("" + str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight()) + "")
    root.title("Feeding and Lighting System")
    label = tk.Label(root, text="Welcome to Light and Feeding Management System", font=('Times New Roman', 40, 'bold'))
    label.pack(padx=20, pady=50)

    # entry field for first name
    # disappearing words when focus in on target field FirstName
    def on_entry_click(event, entry):
        if entry.get() == "Enter Your {} here".format(entry.name):
            entry.delete(0, "end")  # delete all the text in the entry
            entry.insert(0, '')  # Insert blank for user input

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

    firstNameEntryField = EntryWithPlaceholder(root, name="firstNameEntryField",width=30, font=('Times New Roman', 30), placeholder="Enter your firstname here")
    firstNameEntryField.pack()

    # disappearing words when focus in on target field LastName


    # entry field for last name
    EmailEntryField = EntryWithPlaceholder(root, name="email", width=30, font=('Times New Roman', 30), placeholder="Enter your email here")
    EmailEntryField.pack()

    # destroy current frame

    # button functionality
    def checkData():
        import firebase_admin
        from firebase_admin import credentials, firestore

        # Initialize Firebase app
        # Check if Firebase app has already been initialized
        if not firebase_admin._apps:
            # Initialize Firebase app
            cred = credentials.Certificate(
                "C:\\Users\\Makoba Ngulube\\Desktop\\Project\\FinalYearProject\\finalyearproject-33d65-firebase-adminsdk-56scw-68db4b5227.json")
            firebase_admin.initialize_app(cred)
        db = firestore.client()

        # Retrieve data from Firestore
        doc_ref = db.collection("admins").get()


        # Check if document exists
        for doc in doc_ref:
            data = doc.to_dict()
            first_name = data.get('firstname')
            email = data.get('email')

            # Check if fields exist and are not empty
            if first_name and email and firstNameEntryField.get() and EmailEntryField.get():

                # Check if the fields match the document data
                if firstNameEntryField.get() == first_name and EmailEntryField.get() == email:
                    root.destroy()
                    StartProgram()

                else:
                    popup = tk.Toplevel()
                    popup.title("Response")
                    popup.geometry("350x350")
                    label = tk.Label(popup, text="Invalid name")
                    label.pack()
                    button = tk.Button(popup, text="close", command=popup.destroy)
                    button.pack()
            else:
                popup = tk.Toplevel()
                popup.title("Response")
                popup.geometry("350x350")
                label = tk.Label(popup, text="Missing name fields")
                label.pack()
                button = tk.Button(popup, text="close", command=popup.destroy)
                button.pack()
        else:
            popup = tk.Toplevel()
            popup.title("Response")
            popup.geometry("350x350")
            label = tk.Label(popup, text="Document not found")
            label.pack()
            button = tk.Button(popup, text="close", command=popup.destroy)
            button.pack()

    # button to log into system
    button = tk.Button(root, text="Login", font=('Arial', 18), bg="grey", command=checkData)
    button.pack()

    root.mainloop()

