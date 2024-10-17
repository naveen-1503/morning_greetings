import datetime
#generating a message
def generate_message(name):
    if not name:
        raise ValueError("Name needed to generate message")
    
    return f"Good Morning, {name}! Have a great day!"

# Logging the generated message to the message_log file
def log_generate_message(contact, log_file="message_log.txt"):
    message = generate_message(contact)
    try:
        with open ('message_log.txt', "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} Generated message: {message}\n")
    except IOError as e:
        print(f"Filed to write to log file: {e}")

if __name__ == "__main__":
    try:
        message = generate_message("Alice")
        print(message)
    except ValueError as ve:
        print(f"Error: {ve}")