# Telegram Automated Bulk Messages

It is a python script that sends the Telegram messages automatically from Telegram desktop application. It can be configured to send advertising messages. It read data from an excel sheet and send a configured message to people.

## Demo
* Video clip on youtube of the script execution. https://youtu.be/EHWqx8r0f2M

## Important Note
* If this repository helped you to understand at least something new please give star this repository which motivates me to work further for the similar kinds for projects.

## Prerequisites

In order to run the python script, your system must have the following programs/packages installed and the contact number should be saved in your phone (You can use bulk contact number saving procedure of email). There is a way without saving the contact number but has the limitation to send the attachment.
* Python 3.8: Download it from https://www.python.org/downloads
* Pandas : Run in command prompt **pip install pandas**
* Xlrd : Run in command prompt **pip install xlrd**
* Pyautogui: Run in command prompt pip install pyautogui
* Telegram Desktop App : Download from https://desktop.telegram.org/

## Approach
* First need to clone this respiratory
* User scans Telegram login QR code to log in into the Telegram Desktop application.
* Run python script script.py using py script.py in the terminal
* The script reads a customized message from an excel sheet.
* The script reads rows one by one and searches that username in the Telegram Desktop Application search box if the username found on Telegram then it will send a configured message otherwise It reads next row. 
* Loop executes until and unless all rows complete.

Note: If you wish to send an image or documents instead of text you can write code to add attachment send functionality.

## Legal
* This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by Telegram or any of its affiliates or subsidiaries. This is an independent and unofficial software. Use at your own risk. Commercial use of this code/repo is strictly prohibited.

## Code
```
# Program to send bulk customized messages through Telegram Desktop application
# Author @inforkgodara & @memeLordo

import pyautogui
import pyperclip
import pandas
import time
from subprocess import Popen


def paste(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v', interval=0.25)


telegramPath = 'C:\\Users\\Sima Forest\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe'
telegram = Popen(telegramPath)
# while telegram.poll() is None:
#     telegram.wait()

excel_data = pandas.read_excel('Recipients data.xlsx', sheet_name='Recipients').fillna('')

print(excel_data)
count = 0

for column in excel_data['Username'].tolist():

    if str(excel_data['Username'][count]) == '':
        print('Empty line on ' + str(count + 2) + ' number')
    else:
        pyautogui.press('esc')
        pyautogui.press('esc')
        time.sleep(0.75)
        pyautogui.hotkey('ctrl', 'j', interval=0.25)
        time.sleep(0.75)
        paste(str(excel_data['Username'][count]))
        time.sleep(0.75)
        pyautogui.press('enter')
        time.sleep(0.75)
        paste(excel_data['Message'][0])
        # print(excel_data['Message'][0])
        time.sleep(0.75)
        pyautogui.press('enter')
    count = count + 1

pyautogui.press('esc')
print('The script executed successfully.')
```
Note: The script may not work in case if the accessibility of Telegram changed.

Find it on youtube. https://youtu.be/EHWqx8r0f2M
