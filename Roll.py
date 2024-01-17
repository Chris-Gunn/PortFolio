import keyboard

def on_key_press(event):
    if event.name == 'a':  # Replace 'a' with your desired key
        print("Button 'a' pressed!")
        # Perform your desired actions here

keyboard.on_press(on_key_press)  # Register the callback function

# Main program execution
while True:
    # Your main program logic here
    pass