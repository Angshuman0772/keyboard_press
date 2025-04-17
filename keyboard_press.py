# Install the keyboard library if not already installed:
# pip install keyboard

import keyboard
import threading
import time

# Function to simulate holding a key
def hold_key(key):
    while key_pressed[key]:
        keyboard.press(key)
        time.sleep(0.1)  # Simulate holding the key with a small delay

# Dictionary to track the state of keys
key_pressed = {}

def toggle_key(key):
    global key_to_toggle
    if key not in key_pressed or not key_pressed[key]:
        # Start holding the key
        key_pressed[key] = True
        threading.Thread(target=hold_key, args=(key,), daemon=True).start()
        print(f"Started holding '{key}'")
    else:
        # Stop holding the key
        key_pressed[key] = False
        print(f"Stopped holding '{key}'")
        key_to_toggle = None  # Reset the toggle key

# Main script
if __name__ == "__main__":
    key_to_toggle = None

    while True:
        if key_to_toggle is None:
            print("Press any key to set it as the toggle key...")
            while True:
                event = keyboard.read_event()  # Wait for a key event
                if event.event_type == "down":  # Only react to key press events
                    key_to_toggle = event.name  # Get the name of the key pressed
                    break
            print(f"Key '{key_to_toggle}' selected. Press it to toggle holding the key.")
        
        keyboard.wait(key_to_toggle)  # Wait for the key press
        toggle_key(key_to_toggle)