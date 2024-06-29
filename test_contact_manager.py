import unittest
from tkinter import Tk
from contact_manager import add_contact, view_contact, update_contact, delete_contact, search_contact, contacts, update_contact_listbox

class TestContactManager(unittest.TestCase):

    def setUp(self):
        # Set up a root window for the dialog functions
        self.root = Tk()
        self.root.withdraw()  # Hide the root window
        # Clear contacts list before each test
        contacts.clear()

    def tearDown(self):
        self.root.destroy()

    def test_add_contact(self):
        self.root.after(100, lambda: self.root.quit())
        add_contact()
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0]['contact_name'], 'Contact1')
        self.assertEqual(contacts[0]['phone_number'], '1234567890')

    def test_view_contact(self):
        contacts.append({"contact_name": "Contact1", "phone_number": "1234567890", "email": "email@example.com", "address": "Address1"})
        self.root.after(100, lambda: self.root.quit())
        view_contact()

    def test_update_contact(self):
        contacts.append({"contact_name": "Contact1", "phone_number": "1234567890", "email": "email@example.com", "address": "Address1"})
        self.root.after(100, lambda: self.root.quit())
        update_contact()
        self.assertEqual(contacts[0]['contact_name'], 'UpdatedStore')
        self.assertEqual(contacts[0]['phone_number'], '0987654321')

    def test_delete_contact(self):
        contacts.append({"contact_name": "Contact1", "phone_number": "1234567890", "email": "email@example.com", "address": "Address1"})
        self.root.after(100, lambda: self.root.quit())
        delete_contact()
        self.assertEqual(len(contacts), 0)

    def test_search_contact(self):
        contacts.append({"contact_name": "Contact1", "phone_number": "1234567890", "email": "email@example.com", "address": "Address1"})
        self.root.after(100, lambda: self.root.quit())
        search_contact()
        

if __name__ == '__main__':
    unittest.main()
