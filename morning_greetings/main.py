from contacts_manager import contactsManager
import message_generator
import message_sender
import logger

def main():
    contact_manager = contactsManager()

    print("Existing Contacts:")
    contact_manager.list_contacts()

    message_generator.generate_message()
    
        

if __name__ == "__main__":
    main()