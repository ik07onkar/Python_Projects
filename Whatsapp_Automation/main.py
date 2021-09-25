# pip install pyautogui <-- python library which we can use to automate our mouse and keyboard actions
import webbrowser  #Built-In library that I will use to open link in browser(here - whatsapp web)
import pyautogui
import time #we can apply some delay using this library
from datetime import datetime # we will use this module to fetch current time

def seconds_cal(end_hh, end_mm): #calculating seconds from current time --to--> time of delever the message
    minutes = 0
    current = datetime.now()
    start_hh = current.hour
    start_mm = current.minute
    if end_hh > start_hh:
        minutes += ((end_hh-start_hh-1)*60) + (60-start_mm) + end_mm
    elif end_hh == start_hh and end_mm > start_mm:
        minutes += end_mm - start_mm
    else:
        minutes += ((23-start_hh)*60) + (60-start_mm) + (end_hh*60) + end_mm
    return minutes*60-current.second

person_name = input('Enter person name to Message : ')
message = input('Enter what you want to send : ')

hh, mm = input('Enter time when to send message (HH:MM) : ').split(':')
hh = int(hh)
mm = int(mm)
delay_time = seconds_cal(hh, mm)
print('Your message will be delever at ',hh,':',mm,',after',delay_time,'seconds.')
time.sleep(delay_time)

webbrowser.open('https://web.whatsapp.com/')
time.sleep(15) #Waiting 15sec. to open whatsapp in browser

#For finding position of any coordinate we use ----> print(pyautogui.position())
#search for person
pyautogui.click(333, 253) #(333, 253) is position of search bar in whatsapp
pyautogui.typewrite(person_name) #We will put the name of person in the search bar
time.sleep(3) #After writing person name in search bar we have to wait a little to get search result
pyautogui.click(244, 433) #(244, 433) is position of search result(person name)
pyautogui.click(812, 980) #(812, 980) is position of Chatting bar, where we want to type the message
pyautogui.write(message, interval= 0.02) #We will put the message in the chatting bar with the time interval of 0.02sec
pyautogui.click(1786, 979) #(1786, 979) is position, where we have our send arrow to delever the message
