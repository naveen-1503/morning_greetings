#logger.py
import datetime

#Logging the sent message
def log_message(contact, message):
    try:
        with open ('message_log.txt', "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} Sent to {contact['name']}: {message}\n")
    except IOError as e:
        print(f"Filed to write to log file: {e}")

if __name__ == "__main__":
    contact = {"name": "Alice", "email": "alice@example.com"}
    message = "Good Morning, Alice! Have a great day!"
    log_message(contact, message)