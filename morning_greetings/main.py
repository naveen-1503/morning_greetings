from contacts_manager import contactsManager
from message_generator import generate_message, log_generate_message
from message_sender import send_message
from logger import log_message

from datetime import datetime, timedelta
import time

#Calculates the time until preferred time
def seconds_until_preferred_time(preferred_time):
    current_time = datetime.now()

    #Formats the preferred date to just time
    try:
        preferred_time_dt = datetime.strptime(preferred_time, "%H:%M").replace(
            year=current_time.year, month=current_time.month, day=current_time.day
        )
    except ValueError as e:
        raise ValueError(f"Invalid time format '{preferred_time}'. Use 'HH:MM' format.") from e

    #If the time has past, put it to the next day
    if preferred_time_dt < current_time:
        preferred_time_dt += timedelta(days=1)


    time_difference = (preferred_time_dt - current_time).total_seconds()

    #The difference in seconds
    return max(0, int(time_difference))
 
def main():
    try:
        contact_manager = contactsManager()

        #List existing contacts
        print("Existing Contacts:")
        contact_manager.list_contacts()

        contacts = contact_manager.get_contacts()

        if not contacts:
            raise ValueError("Contact list is empty. No messages to send.")

        #Looping through the contacts
        for contact in contacts:
            
            #Generating and logging message
            message =  generate_message(contact['name'])
            log_generate_message(contact['name'])
            
            #Wait time until message being sent
            wait_time = seconds_until_preferred_time(contact['preferred_time'])
            print(f"Waiting {wait_time} seconds to send message to {contact['name']} at {contact['preferred_time']}")

            #Make the script sleep until the next message
            if wait_time > 0:
                time.sleep(wait_time)
        
            #Sending and logging message
            send_message(contact['email'], message)
            log_message(contact, message)
            
            
            

    except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred while running the automation task: {e}")