import tkinter as tk
from PIL import ImageTk, Image
import serial.tools.list_ports






root = tk.Tk()
#creating an instance of the window frame

image = Image.open("jakub-pabis-lQknQP3R1yc-unsplash.jpg")
bg_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.geometry("" + str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight()) + "")
root.title("Feeding and Lighting System")
label = tk.Label(root, text="Welcome to Light and Feeding Management System", font=('Times New Roman', 40, 'bold'))
label.pack(padx=20, pady=50)


#entry field for first name
#disappearing words when focus in on target field FirstName
def on_entry_click(event):
   if firstNameEntryField.get() == "Enter Your FirstName here":
       firstNameEntryField.delete(0, "end") # delete all the text in the entry
       firstNameEntryField.insert(0, '') #Insert blank for user input


firstNameEntryField = tk.Entry(root, width=30, font=('Times New Roman', 30))
firstNameEntryField.insert(0, "Enter Your FirstName here")
firstNameEntryField.bind('<FocusIn>', on_entry_click)
firstNameEntryField.pack()

#disappearing words when focus in on target field LastName
def on_entry_clickLast(event):
    if LastNameEntryField.get() == "Enter Your LastName here":
       LastNameEntryField.delete(0, "end")
       LastNameEntryField.insert(0, '')
#entry field for last name
LastNameEntryField = tk.Entry(root, width=30, font=('Times New Roman', 30))
LastNameEntryField.insert(0, "Enter Your LastName here")
LastNameEntryField.bind('<FocusIn>', on_entry_clickLast)
LastNameEntryField.pack(pady = 20)

#destroy current frame






#button functionality
def checkData():
    import firebase_admin
    from firebase_admin import credentials, firestore

    # Initialize Firebase app
    cred = credentials.Certificate("C:\\Users\\Makoba Ngulube\\Desktop\\Project\\FinalYearProject\\finalyearproject-33d65-firebase-adminsdk-56scw-68db4b5227.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # Retrieve data from Firestore
    doc_ref = db.collection("admins").document("names")
    doc = doc_ref.get()

    # Check if document exists
    if doc.exists:
        data = doc.to_dict()
        first_name = data.get('firstname')
        last_name = data.get('lastname')

        # Check if fields exist and are not empty
        if first_name and last_name and firstNameEntryField.get() and LastNameEntryField.get():

            #Check if the fields match the document data
            if firstNameEntryField.get() == first_name and LastNameEntryField.get() == last_name:
                root.destroy()
                from dashboard import StartProgram
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

#button to log into system
button = tk.Button(root, text="Login", font=('Arial', 18), bg="grey", command=checkData)
button.pack()

root.mainloop()

