#!/usr/bin/python3
import threading
import winsound 
import time
from tkinter import *

bpm = 10
flag = -1
	
def tick():
	i = 0
	while True:
		pause = round(60 / bpm, 2)
		if flag > 0:
			btn_start['text'] = 'Pause'
			i += 1
			time.sleep(pause)
			winsound.PlaySound('sound/Logic_low.wav', winsound.SND_FILENAME)

thread1 = threading.Thread(target=tick)
thread1.setDaemon(True)
thread1.start()

def tack():
	global flag
	flag *= -1
	btn_start['text'] = 'Start'

def onScale(val):
	#v = val
	global bpm
	bpm = int(val)
	lbl_tack['text'] = bpm


root = Tk()
scale = Scale(orient=VERTICAL, length=300, from_=10,to=240, 
		tickinterval=30, resolution=1, command=onScale)
scale.pack()

lbl_tack = Label(text=bpm, font=('Arial', 24, 'bold'))
lbl_tack.pack()

btn_start = Button(text='Start', command=tack)
btn_start.pack()

root.mainloop()
