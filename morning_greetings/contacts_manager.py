#contacts_manager.py
class contactsManager:
    def __init__(self):
        self.contacts = [
            {"name": "Alice", "email": "abc@example.com", "preferred_time": "15:40"},
            {"name": "Bob", "email": "bcd@example.com", "preferred_time": "15:45"},
            {"name": "Charlie", "email": "cde@example.com", "preferred_time": "15:50"}
        ]

    def add_contact(self, name, email, preferred_time="08:00"):
        if not name or not email:
            raise ValueError("Both name and email is required for a personalized message")
        
        if '@' not in email:
            raise ValueError("Invalid email format added")
        
        contact = {'name': name,
                   'email': email,
                   'preferred_time': preferred_time
        }
        self.contacts.append(contact)
    
    def remove_contact(self, name):
        if not self.contacts:
            raise ValueError("No contacts to remove")
        
        initial_length = len(self.contacts)
        self.contacts = [c for c in self.contacts if c['name'] != name]
        if len(self.contacts) == initial_length:
            raise ValueError(f"Contact {name}, not found")
        
    def get_contacts(self):
        return self.contacts
    
    def list_contacts(self):
        if not self.contacts:
            raise ValueError("List is empty")
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")

if __name__ == "__main__":
    manager = contactsManager()
    manager.add_contact("Alice", "alice@example.com", "09:00")
    manager.add_contact("Bob", "bob@example.com")
    manager.remove_contact("Charlie")
    manager.list_contacts()