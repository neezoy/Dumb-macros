import time 
from ahk import AHK
from ahk.window import Window
import random
ahk = AHK(executable_path='D:\\ProgramFiles\\AHK\\AutoHotkey.exe')

a = random.randint(2, 5)/2

win1 = Window.from_pid(ahk, '7884')
win2 = Window.from_pid(ahk, '7532')
win3 = Window.from_pid(ahk, '8832')
win4 = Window.from_pid(ahk, '940')
win5 = Window.from_pid(ahk, '4012')
win6 = Window.from_pid(ahk, '5624')
win7 = Window.from_pid(ahk, '1428')
win8 = Window.from_pid(ahk, '6112')

def session():
	ahk.right_click()
	time.sleep(a)
	ahk.key_press('1')  # press and release a key
	time.sleep(a)
	ahk.key_press('1')  # press and release a key
	time.sleep(a)
	ahk.key_press('3')
	time.sleep(a/4)
	ahk.key_press('2')
	ahk.key_press('1')
	time.sleep(a)


while True:
	win1.activate()
	session()
	win2.activate()
	session()
	win3.activate()
	session()
	win4.activate()
	session()
	win5.activate()
	session()
	win6.activate()
	session()
	win7.activate()
	session()
	win8.activate()
	session()
	