import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []
current_contact_index = None

# contacts management
def add_contact():
    global contacts
    store_name = simpledialog.askstring("Contact Name", "Enter Contact Name:")
    phone_number = simpledialog.askstring("Phone Number", "Enter Phone Number:")
    email = simpledialog.askstring("Email", "Enter Email:")
    address = simpledialog.askstring("Address", "Enter Address:")

    if store_name and phone_number:
        contact = {"contact_name": store_name, "phone_number": phone_number, "email": email, "address": address}
        contacts.append(contact)
        update_contact_listbox()

def view_contact():
    global contacts, current_contact_index
    if current_contact_index is not None:
        contact = contacts[current_contact_index]
        messagebox.showinfo("Contact Details", f"Contact Name: {contact['contact_name']}\nPhone Number: {contact['phone_number']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
    else:
        messagebox.showwarning("No Selection", "Please select a contact to view.")

def update_contact():
    global contacts, current_contact_index
    if current_contact_index is not None:
        contact = contacts[current_contact_index]
        store_name = simpledialog.askstring("Contact Name", "Enter Contact Name:", initialvalue=contact['contact_name'])
        phone_number = simpledialog.askstring("Phone Number", "Enter Phone Number:", initialvalue=contact['phone_number'])
        email = simpledialog.askstring("Email", "Enter Email:", initialvalue=contact['email'])
        address = simpledialog.askstring("Address", "Enter Address:", initialvalue=contact['address'])

        if store_name and phone_number:
            updated_contact = {"contact_name": store_name, "phone_number": phone_number, "email": email, "address": address}
            contacts[current_contact_index] = updated_contact
            update_contact_listbox()
    else:
        messagebox.showwarning("No Selection", "Please select a contact to update.")

def delete_contact():
    global contacts, current_contact_index
    if current_contact_index is not None:
        del contacts[current_contact_index]
        update_contact_listbox()
    else:
        messagebox.showwarning("No Selection", "Please select a contact to delete.")

def search_contact():
    global contacts
    query = simpledialog.askstring("Search Contact", "Enter name or phone number:")
    results = [contact for contact in contacts if query.lower() in contact["contact_name"].lower() or query in contact["phone_number"]]

    if results:
        search_results = "\n".join([f"{contact['contact_name']} - {contact['phone_number']}" for contact in results])
        messagebox.showinfo("Search Results", search_results)
    else:
        messagebox.showinfo("Search Results", "No contacts found.")

def on_contact_select(event):
    global current_contact_index
    if contact_listbox.curselection():
        current_contact_index = contact_listbox.curselection()[0]

def update_contact_listbox():
    global contacts, contact_listbox
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['contact_name']} - {contact['phone_number']}")

root = tk.Tk()
root.title("Contact Manager")
root.geometry("600x400")
root.configure(bg='pink')

# Title Label
title_label = tk.Label(root, text="Contact Manager", font=("Arial", 20), bg='pink')
title_label.pack()

# List
contact_listbox = tk.Listbox(root, height=15, width=50, bg='light pink')
contact_listbox.pack()
contact_listbox.bind('<<ListboxSelect>>', on_contact_select)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact, bg='pink')
add_button.pack(pady=5)

view_button = tk.Button(root, text="View Contact", command=view_contact, bg='pink')
view_button.pack(pady=5)

update_button = tk.Button(root, text="Update Contact", command=update_contact, bg='pink')
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, bg='pink')
delete_button.pack(pady=5)

search_button = tk.Button(root, text="Search Contact", command=search_contact, bg='pink')
search_button.pack(pady=5)


root.mainloop()
