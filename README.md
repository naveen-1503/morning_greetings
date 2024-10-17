# Morning_greetings

This Python package automates the process of sending personalized morning greeting messages to contacts via email. The program is designed to generate messages based on each contact's preferred greeting time and log significant events, such as message generation and sending.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Error Handling](#error-handling)

## Features
- Add, remove, and list contacts with their preferred greeting times and email addresses.
- Generate personalized greeting messages.
- Send messages to contacts at their preferred times.
- Log all message generation and sending events to a text file.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/naveen-1503/morning_greetings.git
   cd morning_greetings

2. Install the package using pip
    pip install .

3. Enure that you have Python 3 installed

## Usage
1. Run the automation task: The automation task can be manually trigged by running the main script
    Python3 main.py
2. Add contacts: Contacts can be added by modifying the self.contacts list in contacts_manager.py

3. Message that are generated and sent will be logged in message_log.txt

## Directory Structure 

morning_greetings/
│
├── main.py                  # Entry point for the program
├── contacts_manager.py      # Module for managing contacts
├── message_generator.py      # Module for generating messages
├── message_sender.py         # Module for sending messages
├── logger.py                 # Module for logging events
Setup.py                      #Installation script for the package

## Error Handling
The package includes error handling for many scenarios, for example:
    
    Trying to send message to a list without any contacts
    Invalid contact information

## My experience
My exprience with this project is that is was alright. Making the different modules interacting with each other was fairly easy, but making the script send a message at different times did create problems. Also don't know if I made the project run daily, or if it stops after running through all the contacts. I also didn't use the contacts.py module because it wasnt needed and got all I needed from the contact_manager module. 
