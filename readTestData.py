import csv
import random

class create_csv:
    fieldnames=["name", "phone_number", "email", "size", "topping", "time", "special_request"]
    data=[
    ["Alex Example", 5550101, "alex@example.com", "small", "onion", "12:00", "please ring"],
    ["Jamie Example", 5550102, "jamie@example.com", "large", "extra cheese", "11:30", "please knock"],
    ["Taylor Example", 5550103, "taylor@example.com", "small", "bacon", "09:00", "leave at door"]
      ]

    with open('cust-data.csv',mode='w',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(fieldnames) # Write the fieldnames (header) as the first row
        writer.writerows(data)# Write the data rows
    
    print("File will be created if not existing and if existing it will be overwritten with the above data")



class CsvRead:
    def __init__(self, file):
        '''
        Initializes the CsvRead object.
        Tries to open the file provided as an argument.
        If the file is not found, it catches the FileNotFoundError and prints an error message.
        '''
        try:
            self.file = open(file)  # Try to open the file
            self.reader = csv.DictReader(self.file)  # Initialize the CSV DictReader to read the file
        except FileNotFoundError:
            print("File not found")  # Print message if file doesn't exist
            self.file = None  # Set file to None if it wasn't opened
            self.reader = None  # Set reader to None if it wasn't initialized

    def read(self):
        '''
        Randomly selects and returns a row from the CSV file if it's open and readable.
        If the file is not found, it returns None.
        '''
        if self.file is None or self.reader is None:
            print("No file to read from.")  # Notify if file doesn't exist or couldn't be opened
            return None  # Return None if no file to read from
        
        return random.choice(list(self.reader))  # If file is found, return a random row