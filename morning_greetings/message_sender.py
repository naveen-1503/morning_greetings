#message_sender.py
import datetime

#Sending the message to the user
def send_message(email, message): 
    if not email: 
        raise ValueError("Email address is missing")
    if not '@' in email:
        raise ValueError("Invalid Email")
        
    print(f"Sending message to {email}: {message}")

if __name__ == "__main__":
    try:
        message = "Good Morning, Alice! Have a great day!"
        send_message("alice@example.com", message)
    except ValueError as ve:
        print(f"Error: {ve}")