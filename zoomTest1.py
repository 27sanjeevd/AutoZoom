from datetime import datetime, timedelta
from threading import Timer
import pyautogui 
import time

x=datetime.now()

date = str(datetime.date(x))
val1 = date.split("-")

time1 = str(datetime.time(x));
print(time)
times = time1.split(":")
print(times)


a_day = ("", "", "", "") #Insert Time periods of A Days
b_day = ("", "", "") # Insert Time periods of B Days

a_logins = ("", "", "", "") #A-day zoom logins
a_passwords = ("", "", "", "") #A-day zoom passwords

b_logins = ("", "", "") #B-day zoom logins               
b_passwords = ("", "", "") #B-day zoom passwords            

  
day_val = ()
day_logins = ()
day_passwords = ()

which_day = str(input("what day? ")) #Checks if A-Day of B-Day

if which_day == "a":
    day_val = a_day
    day_logins = a_logins
    day_passwords = a_passwords
else:
    day_val = b_day;
    day_logins = b_logins
    day_passwords = b_passwords

counter1 = 0

def function1(val):
    
    meet_id = day_logins[val]
    
    pyautogui.press('esc',interval=0.1)
    
    time.sleep(0.2)
    
    pyautogui.press('win',interval=0.1)
    pyautogui.write('zoom')
    pyautogui.press('enter',interval=0.5)

    time.sleep(3)

    x,y = pyautogui.locateCenterOnScreen('joinButton.png')
    pyautogui.click(x,y)
    
    pyautogui.press('enter',interval=1)
    
    pyautogui.write(meet_id)
    pyautogui.press('enter',interval=1)

    password = day_passwords[counter1]

    time.sleep(3)
    pyautogui.press('enter',interval=1)
    pyautogui.write(password)
    pyautogui.press('enter',interval = 1)

while counter1 < len(day_val):
    time2 = day_val[counter1]
    print(time2)
    time3 = time2.split(":")
    meeting_time = (int(time3[0]) * 3600) + (int(time3[1]) * 60) + round(float(time3[2]), 2)

    current_time = (int(times[0]) * 3600) + (int(times[1]) * 60) + round(float(times[2]), 2)
    print(int(meeting_time - current_time - 300))
    if (current_time < meeting_time - 300):
        t = Timer(int(meeting_time - current_time - 300), function1(counter1))
        t.start()


    
    counter1 += 1
