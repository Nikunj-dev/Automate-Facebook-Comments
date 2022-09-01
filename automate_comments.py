import pyautogui
import time

comments = ["Python bot autocomment", "Bot is working", "Bot is wrote this comment"]
time.sleep(2)
for i in range(10):
    pyautogui.typewrite(comments[i%3])
    pyautogui.press("enter")
    time.sleep(2)

