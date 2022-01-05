import pyautogui

pyautogui.click(451,301)

x, y = pyautogui.locateCenterOnScreen('1.png')
x = x/2
y = y/2
pyautogui.click(x, y)

x, y = pyautogui.locateCenterOnScreen('+.png')
x = x/2
y = y/2
pyautogui.click(x, y)

x, y = pyautogui.locateCenterOnScreen('3.png')
x = x/2
y = y/2
pyautogui.click(x, y)

pyautogui.press('enter')