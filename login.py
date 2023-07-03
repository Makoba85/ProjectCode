#all the import statements
import sys
import tkinter as tk
from PIL import ImageTk, Image
from dashboard import StartProgram
from tkinter import messagebox


def beginProgramExecution():

    # creating an instance of the window frame
    root = tk.Tk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.title("Feeding and Lighting System")
    root.resizable(False, False)

    # Adding background image
    image = Image.open("jakub-pabis-lQknQP3R1yc-unsplash.jpg")
    bg_image = ImageTk.PhotoImage(image)
    bg_image
    background_label = tk.Label(root, image=bg_image)
    background_label.place(x=0.5, y=0.5, relwidth=1, relheight=1)

    label = tk.Label(root, text="Welcome to Light and Feeding Management System", font=('Times New Roman', 40, 'bold'),bg='wheat',borderwidth=3, relief="groove", highlightthickness=3, highlightbackground="white")
    label.pack(padx=20, pady=50)

    label.pack(padx=20, pady=50)


    # Remove placeholders
    def removeFirstNamePlaceholders(text):
        if len(text) > 0:
            firstname_placeholder.config(text="")
            firstname_placeholder.place_configure(x=10000)
        else:
            firstname_placeholder.config(text="Enter your First Name")
            firstname_placeholder.place_configure(x=550)


    def removeEmailPlaceholders(text):
        if len(text) > 0:
            email_placeholder.config(text="")
            email_placeholder.place_configure(x=10000)
        else:
            email_placeholder.config(text="Enter your Email Address")
            email_placeholder.place_configure(x=550)

    #FIRSTNAME
    firstNameEntryField = tk.Entry(root, name="firstNameEntryField",width=30, font=('Times New Roman', 30))
    firstNameEntryField.pack(pady=10)
    firstNameEntryField.bind('<KeyRelease>', lambda e: removeFirstNamePlaceholders(firstNameEntryField.get()))



    #enter placeholder for firstname
    placeholderBackgroundColor = 'grey'
    firstname_placeholder = tk.Label(root, text="Enter your first name", fg=placeholderBackgroundColor, font=('Arial', 20))
    firstname_placeholder.place( x=550,y=193)
    firstname_placeholder.bind('<Button-1>', lambda e: firstNameEntryField.focus())






    #EMAIL
    # entry field
    EmailEntryField = tk.Entry(root, name="email", width=30, font=('Times New Roman', 30))
    EmailEntryField.pack(pady=10)
    EmailEntryField.bind('<KeyRelease>', lambda e: removeEmailPlaceholders(EmailEntryField.get()))


    #email address placeholder
    email_placeholder = tk.Label(root, text="Enter your email address", fg=placeholderBackgroundColor,font=('Arial', 20))
    email_placeholder.place(x=535, y=262)
    email_placeholder.bind('<Button-1>', lambda e: EmailEntryField.focus())





    # button functionality
    def checkData():
        import firebase_admin
        from firebase_admin import credentials, firestore

        # Initialize Firebase app
        # Check if Firebase app has already been initialized
        if not firebase_admin._apps:
            # Initialize Firebase app
            cred = credentials.Certificate(
                "C:\\Users\\Makoba Ngulube\\Desktop\\Project\\FinalYearProject\\fir-vue-72fd8-firebase-adminsdk-ibkku-05e683ef03.json")
            firebase_admin.initialize_app(cred)
        db = firestore.client()

        # Retrieve data from Firestore
        doc_ref = db.collection("admins").get()




        if(firstNameEntryField.get() != "" and EmailEntryField.get() != ""):
            #use field data to query firebase
            #Check if document exists
            found = False;
            for doc in doc_ref:
                data = doc.to_dict()
                first_name = data.get('firstname')
                email = data.get('email')
                message = None

                if(firstNameEntryField.get().lower() == first_name and EmailEntryField.get().lower() == email):
                    message = "Welcome Found"
                    found = True
                    break

                else:
                    if(firstNameEntryField.get() != first_name and EmailEntryField.get() == email):
                        message = 'Mismatching first name'
                    elif(firstNameEntryField.get() == first_name and EmailEntryField.get() != email):
                        message = 'does not match any known email'
                    else:
                        message = "Document doesnt exist"

            if(found):
                root.destroy()
                StartProgram()
            else:
                messagebox.showerror("Status", message)

        else:
            messagebox.showerror('Fields', 'Cannot have empty fields')


    # button to log into system
    button = tk.Button(root, text="Login", font=('Arial', 18), bg="grey", command=checkData)
    button.pack()





    root.mainloop()

