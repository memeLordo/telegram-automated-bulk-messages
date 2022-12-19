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