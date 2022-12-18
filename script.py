import pyautogui
import pyperclip
import pandas
import time
from subprocess import Popen


def paste(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')


telegramPath = 'C:\\Users\\Sima Forest\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe'
telegram = Popen(telegramPath)
while telegram.poll() is None:
    telegram.wait()

excel_data = pandas.read_excel('Recipients data.xlsx', sheet_name='Recipients').fillna('')

print(excel_data)
count = 0

for column in excel_data['Username'].tolist():

    if str(excel_data['Username'][count]) == '':
        print('Empty line on ' + str(count + 1)+' number')
    else:
        pyautogui.press('esc')
        pyautogui.press('esc')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'j')
        time.sleep(1)
        paste(str(excel_data['Username'][count]))
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        paste(excel_data['Message'][0])
        time.sleep(1)
        pyautogui.press('enter')
    count = count + 1

pyautogui.press('esc')
print('The script executed successfully.')
