import subprocess
from tkinter import Y
import pyautogui
import time

kakao = subprocess.Popen(['open', '-a', 'kakaotalk'])

time.sleep(3)

pyautogui.click(668, 225)
pyautogui.press('enter')

pyautogui.typewrite('Test message')