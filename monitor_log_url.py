#imports
import re
import logging
import time
from pynput import keyboard
import requests

#get input from user
url_input = input("[Start] - Please enter a valid URL, that schould be checked: ")

#set regex
url_regex = "^https?:\\/\\/(?:www\\.)?"

#validate url pattern
def validate_url(url):
    if re.findall(url_regex, url):
        print("[Info] - Valid URL pattern")
    else:
        global url_input
        url_input = input("[Info] - Invalid URL pattern! \n[Info] - Please enter a valid URL, that schould be checked: ")
        validate_url(url_input)

validate_url(url_input)

#identify if a key is pressed
break_program = False
def on_press(key):
    global break_program
    try:
        print('[Info] - alphanumeric key "' + key.char + '" pressed')
        print("[Info] - please wait until the process is fully terminated")
        break_program = True
        return False
    except AttributeError:
        print('[Info] - special key', key, 'pressed')
        print("[Info] - please wait until the process is fully terminated")
        break_program = True
        return False

#configure log file
logging.basicConfig(filename="log.txt", filemode="w", level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%Y %H:%M:%S')

#return info to exit by pressing any key
print("[Exit] -", url_input, "is being monitored and logged, press any key to exit...")

#run until key is pressed
with keyboard.Listener(on_press=on_press) as listener:
    while break_program == False:
        # check if the url is up
        try:
            get = requests.get(url_input)
            if get.status_code == 200:
                url_up = "reachable!"
            else:
                url_up = "not reachable!"
        except:
            url_up = "not reachable!"

        logging.info(url_input + " -> " + url_up)
        #repeat every 30 seconds
        time.sleep(30)
    listener.join()

#return info that process has been terminated
print("[Stop] - process successfully terminated")



