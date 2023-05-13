import subprocess
import wolframalpha
import pyttsx3
from tkinter import *
import cv2
import tkinter as tk
import screen_brightness_control as sbc
import json
import random
import psutil
import datetime
import wikipedia
import webbrowser
import pyautogui
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import PyPDF3
import requests
from playsound import playsound
import shutil
from twilio.rest import Client
from clint.textui import progress
from urllib.request import urlopen
import pyttsx3
import speech_recognition as sr
import wmi
import platform
import pywhatkit
import sys
import speedtest
from plyer import notification
from googletrans import Translator
from pygame import mixer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = tk.Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("Alfred version 1")
	speak("I am your Assistant")
	speak(assname)
	

def username():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome Mr.", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Sir")



def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

def webCam():
	speak('Opening camera')
	cap = cv2.VideoCapture(0)
	while True:
		ret, img = cap.read()
		cv2.imshow('web camera',img)
		k = cv2.waitKey(50)
		if k == 27:
			break
	cap.release()
	cv2.destroyAllWindows()

def pdf_reader():
	speak("Boss enter the name of the book which you want to read")
	n = input("Enter the book name: ")
	n = n.strip()+".pdf"
	book_n = open(n,'rb')
	pdfReader = PyPDF3.PdfFileReader(book_n)
	pages = pdfReader.numPages
	speak(f"Boss there are total of {pages} in this book")
	speak("plsase enter the page number Which I nedd to read")
	num = int(input("Enter the page number: "))
	page = pdfReader.getPage(num)
	text = page.extractText()
	print(text)
	speak(text)

def news():
	news_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3d7d2570874a4de697f837fc650bb57b"
	news_page = requests.get(news_url).json()
	articles = news_page["articles"]
	headlines = []
	days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
	for a in articles:
		headlines.append(a["title"])
	for i in range(len(days)):
		print(f"Today's {days[i]} news is: {headlines[i]}")
		speak(f"Today's {days[i]} news is: {headlines[i]}")

def game_play():
	speak("Lets Play ROCK PAPER SCISSORS !!")
	print("LETS PLAYYYYYYYYYYYYYY")
	i = 0
	Me_score = 0
	Com_score = 0
	while (i < 5):
		choose = ("rock", "paper", "scissors", "thread")  # Tuple
		com_choose = random.choice(choose)
		query = takeCommand().lower()
		
		if query == "rock":
			if com_choose == "rock":
				speak("ROCK")
				print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")
			
			elif com_choose == "paper":
				speak("paper")
				Com_score += 1
				print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")
			
			elif com_choose == "scissors":
				speak("Scissors")
				Me_score += 1
				print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")
			
			else:
				speak("thread")
				Com_score += 1
				print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")
			
		elif query == "paper":
			if com_choose == "rock":
					speak("ROCK")
					Me_score += 1
					print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")
			
			elif com_choose == "paper":
				speak("paper")
				print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")
			
			elif com_choose == "thread":
				speak("thread")
				Me_score += 1
				print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")
			
			else:
				speak("Scissors")
				Com_score += 1
				print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")
			
		elif query == "scissors" or query == "scissor" or query == "caesar":
			if com_choose == "rock":
				speak("ROCK")
				Com_score += 1
				print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")
				
			elif com_choose == "paper":
				speak("paper")
				Me_score += 1
				print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")
			
			elif com_choose == "thread":
				speak("thread")
				Me_score += 1
				print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")
			else:
				speak("Scissors")
				print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")
		
		i += 1
	print()
	print(f"FINAL SCORE:\nME: {Me_score}\nJARVIS: {Com_score}")
	
	if Me_score > Com_score:
		print("YOU WON THE GAME")
		speak("Congratulation sir, you won the game")
	
	elif Me_score < Com_score:
		print("JARVIS WON THE GAME")
		speak("Hurray!! I won the game")
	
	else:
		print("GAME ENDS IN A DRAW!!!")
		speak("That was a nice game, sir")

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login('your email id', 'your email password')
	server.sendmail('your email id', to, content)
	server.close()

if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
	clear()
	wishMe()
	username()
	
	while True:
		
		query = takeCommand().lower()
		
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 6)
			speak("According to Wikipedia")
			print(results)
			speak(results)
		
		elif 'play game' in query:
			game_play()
	    
		elif 'read pdf' in query:
			pdf_reader()
		
		elif 'camera' in query:
			webCam()
		
		elif "tell me news" in query:
			speak("Just give me a moment fetching some top headlines for you......")
			news()

		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")
				
		elif 'search on youtube' in query: 
			query = query.replace("search on youtube", "") 
			webbrowser.open(f"www.youtube.com/results?search_query={query}") 
			 
		elif 'close youtube' in query: 
			os.system("taskkill /f /im msedge.exe")
		
		elif "memory available" in query:
			psutil.cpu_percent()
			psutil.virtual_memory()
			dict(psutil.virtual_memory()._asdict())
			print(f"Sir your available memory is: {int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)} percentage")
			speak(f"Sir your available memory is: {int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)} percentage")
			

		elif "calculate" in query:
			from calculater import WolfRamAlpha
			from calculater import Calculator
			query = query.replace("calculate", "")
			Calculator(query)
		
		elif "play song in youtube" in query:
			speak("Sir, what song do you want me to play on youtube")
			songcommand = takeCommand().lower()
			pywhatkit.playonyt(f"{songcommand}")
		
		elif "alarm" in query:
			print("input time example: 10:10")
			speak("Tell me the time to set the alarm, sir")
			time = input("Time: ")
			speak(f"Alarm is set at {time}, sir")
			
			while True:
				time_now = datetime.datetime.now().strftime("%H:%M")
				
				if time_now == time:
					speak("Time to wake up, sir")
					playsound(r"C:\\Users\\User\\Desktop\\Alfred Waiter v1\\musics\\alarm.wav")
				  
				elif time_now > time:
					speak("Alarm closed, sir")
					break

		elif 'dictionary' in query:
			speak('What you want to search in your intelligent dictionary?')
			translate(takeCommand())
		
		elif "translate" in query:
			from Translator import translategl
			query = query.replace("Alfred","")
			query = query.replace("translate","")
			translategl(query)
		
		elif 'uzbek news' in query:
			speak('Ofcourse sir..')
			speak('Do you want to read the full news...')
			test = takeCommand()
			if 'yes' in test:
				speak('Ok Sir, Opening browser...')
				webbrowser.open("https://uz.news/")
				speak('You can now read the full news from this website.')
			else:
				speak('No Problem Sir')

		elif "running process" in query:
			f = wmi.WMI()
			speak("Sir your running processes are:")
			for process in f.Win32_Process():
				speak(f"{process.Name:}")
		
		elif "task manager" in query:
			taskmanagerpath = "C:\\Windows\\system32\\Taskmgr.exe"
			os.startfile(taskmanagerpath)
		
		elif "ram usage" in query:
			psutil.cpu_percent()
			psutil.virtual_memory()
			dict(psutil.virtual_memory()._asdict())	
			print(f"Sir you have used {psutil.virtual_memory().percent} percentage of RAM and ")
			speak(f"Sir you have used {psutil.virtual_memory().percent} percentage of RAM and ")			
			
		elif "cpu usage" in query:
			print(f"Sir you have used: {psutil.cpu_percent()} percentage of your cpu")
			speak(f"Sir you have used: {psutil.cpu_percent()} percentage of your cpu")
		
		elif "system information" in query:
			uname = platform.uname()
			print(f"System: {uname.system}")
			print(f"Node Name: {uname.node}")
			print(f"Release: {uname.release}")
			print(f"Version: {uname.version}")
			print(f"Machine: {uname.machine}")
			print(f"Processor: {uname.processor}")
			speak(f"System: {uname.system}")
			speak(f"Node Name: {uname.node}")
			speak(f"Release: {uname.release}")
			speak(f"Version: {uname.version}")
			speak(f"Machine: {uname.machine}")
			speak(f"Processor: {uname.processor}")
		
		elif "cpu information" in query:
			print(f"Physical cores:{psutil.cpu_count(logical=False)}")
			print(f"Total cores:{psutil.cpu_count(logical=True)}")
			print(f"Physical cores:{psutil.cpu_count(logical=False)}")
			print(f"Total cores:{psutil.cpu_count(logical=True)}")

			speak(f"Physical cores:{psutil.cpu_count(logical=False)}")
			speak(f"Total cores:{psutil.cpu_count(logical=True)}")
			speak(f"Physical cores:{psutil.cpu_count(logical=False)}")
			speak(f"Total cores:{psutil.cpu_count(logical=True)}")
			cpufreq = psutil.cpu_freq()
			print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
			print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
			print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
			print("CPU Usage Per Core:")

			speak(f"Max Frequency: {cpufreq.max:.2f}Mhz")
			speak(f"Min Frequency: {cpufreq.min:.2f}Mhz")
			speak(f"Current Frequency: {cpufreq.current:.2f}Mhz")
			speak("CPU Usage Per Core:")
			for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
				print(f"Core {i}: {percentage}%")
				print(f"Total CPU Usage: {psutil.cpu_percent()}%")
				speak(f"Core {i}: {percentage}%")
				speak(f"Total CPU Usage: {psutil.cpu_percent()}%")
		
		elif "disk information" in query:
			hdd = psutil.disk_usage('/')
			print (int("Total: %d GiB" % hdd.total / (2**30)))
			print (int("Used: %d GiB" % hdd.used / (2**30)))
			print (int("Free: %d GiB" % hdd.free / (2**30)))
			print (int("Percentage: %d GiB" % percentage))
			
			speak("Total: %d GiB" % hdd.total / (2**30))
			speak("Used: %d GiB" % hdd.used / (2**30))
			speak("Free: %d GiB" % hdd.free / (2**30))
			speak("Percentage: %d GiB" % percentage)
		
		elif "internet speed" in query:
			import speedtest
			def internet(self,arg):
				wifi  = speedtest.Speedtest()
				print ("Wifi Download Speed is ", wifi.download())
				print ("Wifi Upload Speed is ", wifi.upload())
		
		elif "memory information" in query:
				print("RAM memory % used:", psutil.swap_memory()[2])
				print("RAM Used (GB):", psutil.swap_memory()[3]/1000000000)
				print("RAM Virtual memory % used:", psutil.virtual_memory()[2])
				print("RAM Virtual Used (GB):", psutil.virtual_memory()[3]/1000000000)
	
		
		elif 'voice man' in query:
			if 'female' in query:
				engine.setProperty('voice', voices[1].id)
			else:
				engine.setProperty('voice', voices[0].id)
			speak("Hello Sir, I have switched my voice. How is it?")
		
		elif 'voice woman' in query:
			if 'male' in query:
				engine.setProperty('voice', voices[0].id)
			else:
				engine.setProperty('voice', voices[1].id)
			speak("Hello Sir, I have switched my voice. How is it?")

		elif "what" in query or "who" in query:
			
			client = wolframalpha.Client("EVX5V8-LE8YAKW2UT")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")


		elif "how" in query or "when" in query:
			
			client = wolframalpha.Client("EVX5V8-LE8YAKW2UT")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")
		
		elif "where" in query:
			
			client = wolframalpha.Client("EVX5V8-LE8YAKW2UT")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")

			
		elif 'open google' in query:
			speak("what should I search ?")
			qry = takeCommand().lower()
			webbrowser.open(f"{qry}") 
			results = wikipedia.summary(qry, sentences=2) 
			speak(results)
		
		elif 'google search' in query: 
			query = query.replace("google search", "") 
			pyautogui.hotkey('alt', 'd') 
			pyautogui.write(f"{query}", 0.1) 
			pyautogui.press('enter')
	
		elif 'close google' in query:
			os.system("taskkill /f /im msedge.exe")  
		
		elif 'open new window' in query: 
			pyautogui.hotkey('ctrl', 'n') 
		
		elif 'open incognito window' in query: 
			pyautogui.hotkey('ctrl', 'shift', 'n') 
		
		elif 'open history' in query: 
			pyautogui.hotkey('ctrl', 'h') 
		
		elif 'open downloads' in query: 
			pyautogui.hotkey('ctrl', 'j')
  
		elif 'new tab' in query: 
			pyautogui.hotkey('ctrl','t')

		elif 'previous tab' in query: 
			pyautogui.hotkey('ctrl', 'shift', 'tab') 
		
		elif 'next tab' in query: 
			pyautogui.hotkey('ctrl', 'tab') 
		
		elif 'close tab' in query:
			pyautogui.hotkey('ctrl', 'w') 
		
		elif 'close window' in query: 
			pyautogui.hotkey('ctrl', 'shift', 'w') 
		
		elif 'clear browsing history' in query: 
			pyautogui.hotkey('ctrl', 'shift', 'delete') 
			
		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com")

		
		elif 'play snake' in query:
			speak("Here you go enjoy game Snake\n")
			webbrowser.open("https://poki.com/en/g/snake-cool")
		
		
		elif 'play dino' in query:
			speak("Here you go enjoy game Dino and you can play other game If you want\n")
			webbrowser.open("https://poki.com/en/g/dinosaur-game")
		
        
		elif 'play pac-man' in query:
			speak("Here you go enjoy game packman\n")
			webbrowser.open("https://www.google.com/logos/2010/pacman10-i.html")
			
		elif 'play music' in query:
			music_dir = "C:\\Users\\User\\Music" 
			songs = os.listdir(music_dir)
			os.startfile(os.path.join(music_dir, random.choice(songs)))
		
		elif 'close music' in query: 
			os.system("taskkill /f /im Music.UI.exe")
		
		elif "toss a coin" in query:
			moves=["head", "tails"]
			cmove=random.choice(moves)
			playsound.playsound('C:\\Users\\User\\Desktop\\Alfred Waiter v1\\musics\\quarter spin flac.mp3')
			speak("It's " + cmove)
			print(cmove)
		
		
		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("Hour:%H Minut:%M Second:%S")
			speak(f"Sir, the time is {strTime}") 
			print(f"{strTime}")

		elif 'open firefox' in query:
			codePath = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"
			os.startfile(codePath)
		
		elif 'maximize this window' in query: 
			pyautogui.hotkey('alt', 'space') 
			time.sleep(1) 
			pyautogui.press('x')

		elif 'minimize this window' in query: 
			pyautogui.hotkey('alt', 'space') 
			time.sleep(1) 
			pyautogui.press('n')  
			
		elif 'close firefox' in query:
			os.system("taskkill /f /im firefox.exe") 
		
		#Volume Change
		elif "volume up" in query: 
			pyautogui.press("volumeup") 
			pyautogui.press("volumeup")
			pyautogui.press("volumeup") 
			pyautogui.press("volumeup") 
			pyautogui.press("volumeup") 
			pyautogui.press("volumeup") 
			pyautogui.press("volumeup") 
			pyautogui.press("volumeup") 
			pyautogui.press("volumeup") 
			pyautogui.press("volumeup") 
			pyautogui.press("volumeup") 
			pyautogui.press("volumeup") 
			pyautogui.press("volumeup") 
			pyautogui.press("volumeup")
			pyautogui.press("volumeup") 
        
		elif "volume down" in query: 
			pyautogui.press("volumedown") 
			pyautogui.press("volumedown") 
			pyautogui.press("volumedown") 
			pyautogui.press("volumedown") 
			pyautogui.press("volumedown") 
			pyautogui.press("volumedown") 
			pyautogui.press("volumedown") 
			pyautogui.press("volumedown") 
			pyautogui.press("volumedown") 
			pyautogui.press("volumedown") 
			pyautogui.press("volumedown") 
			pyautogui.press("volumedown") 
			pyautogui.press("volumedown") 
			pyautogui.press("volumedown") 
			pyautogui.press("volumedown") 
		
		elif "mute" in query:
			pyautogui.press("volumemute") 
		
		elif "refresh" in query: 
			pyautogui.moveTo(1551,551, 2) 
			pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right') 
			pyautogui.moveTo(1620,667, 1) 
			pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left') 
		
		elif "scroll down" in query: 
			pyautogui.scroll(1000) 
		
		elif "drag visual studio to the right" in query: 
			pyautogui.moveTo(46, 31, 2) 
			pyautogui.dragRel(1857, 31, 2) 
		
		elif "rectangular spiral" in query: 
			pyautogui.hotkey('win') 
			time.sleep(1) 
			pyautogui.write('paint') 
			time.sleep(1) 
			pyautogui.press('enter') 
			pyautogui.moveTo(100, 193, 1) 
			pyautogui.rightClick 
			pyautogui.click() 
			distance = 300 
			while distance > 0: 
				pyautogui.dragRel(distance, 0, 0.1, button="left") 
				distance = distance - 10 
				pyautogui.dragRel(0, distance, 0.1, button="left") 
				pyautogui.dragRel(-distance, 0, 0.1, button="left") 
				distance = distance - 10 
				pyautogui.dragRel(0, -distance, 0.1, button="left") 
		
		elif 'send a mail' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				speak("whome should i send")
				to = input()
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(assname)
			print("My friends call me", assname)
		
		
		# BRIGHTNESS
		elif "brightness" in query:
			print('J: How much brightness do you want to set it at')
			speak('How much brightness do you want to set it at')
			number = takeCommand()
			sbc.set_brightness(number)
			speak('Brightness has been set')
			print('* J:Brightness has been set')
        
		# BATTERY
		elif "battery" in query:
			battery = psutil.sensors_battery() 
			percent = battery.percent
			batterypercent=str(percent)+"% Battery remaining"
			speak(batterypercent)
			print('J:'+ batterypercent)
			if percent <=10:
				speak('Please plug in the laptop')
		
		elif 'open movies' in query:
			var.set("Opening Movies")
			window.update()
			speak("Opening Movies")
			os.startfile("C:\\Movies")
		
		elif "location of" in query:
			query = query.replace("location", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.nl/maps/place/"+location+"")
		
		elif 'take photo' in query:
			stream = cv2.VideoCapture(0)
			grabbed, frame = stream.read()
			if grabbed:
				cv2.imshow('pic', frame)
				cv2.imwrite('pic.jpg', frame)
				stream.release()
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())
			
		
		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "why you came to world" in query:
			speak("Thanks to Azim. further It's a secret")

		elif 'power point presentation' in query:
			speak("opening Power Point presentation")
			power = r"C:\\Users\\Users\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
			os.startfile(power)

		elif 'is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif 'reason for you' in query:
			speak("I was created as a Minor project by Mister Azim ")

		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20,
													0,
													"C:\Windows\Web\Wallpaper\Theme1",
													0)
			speak("Background changed successfully")
		

		elif 'open bluestack' in query:
			appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
			os.startfile(appli)


		elif "take screenshot" in query:
			speak('tell me a name for the file')
			name = takeCommand().lower()
			time.sleep(3)
			img = pyautogui.screenshot()
			img.save(f"{name}.png")
			speak("screenshot saved")
		
		elif "switch the window" in query or "switch window" in query:
			speak("Okay sir, Switching the window")
			pyautogui.keyDown("alt")
			pyautogui.press("tab")
			time.sleep(1)
			pyautogui.keyUp("alt")
	
		
		elif "hide all files" in query or "hide this folder" in query:
			os.system("attrib +h /s /d")
			speak("Sir, all the files in this folder are now hidden")

        
		elif "visible" in query or "make files visible" in query:
			os.system("attrib -h /s /d")
			speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

			
		
		elif 'lock window' in query:
			speak("locking the device")
			ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
			speak("Hold On a Sec ! Your system is on its way to shut down")
			subprocess.call('shutdown / p /f')
				
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop Alfred from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)
		 
		elif "what is my ip address" in query:
			speak("Checking")
			try:
				ipAdd = requests.get('https://api.ipify.org').text
				print(ipAdd)
				speak("your ip adress is")
				speak(ipAdd)
			except Exception as e:
				speak("network is weak, please try again some time later")

		elif 'weather' in query or 'temperature' in query:
			try:
				speak("Tell me the city name.")
				city = takeCommand()
				api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=eea37893e6d01d234eca31616e48c631"
				w_data = requests.get(api).json()
				weather = w_data['weather'][0]['main']
				temp = int(w_data['main']['temp'] - 273.15)
				temp_min = int(w_data['main']['temp_min'] - 273.15)
				temp_max = int(w_data['main']['temp_max'] - 273.15)
				pressure = w_data['main']['pressure']
				humidity = w_data['main']['humidity']
				visibility = w_data['visibility']
				wind = w_data['wind']['speed']
				sunrise = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunrise'] + 19800))
				sunset = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunset'] + 19800))
				
				all_data1 = f"Condition: {weather} \nTemperature: {str(temp)}°C\n"
				all_data2 = f"Minimum Temperature: {str(temp_min)}°C \nMaximum Temperature: {str(temp_max)}°C \n" \
                            f"Pressure: {str(pressure)} millibar \nHumidity: {str(humidity)}% \n\n" \
                            f"Visibility: {str(visibility)} metres \nWind: {str(wind)} km/hr \nSunrise: {sunrise}  " \
                            f"\nSunset: {sunset}"
				speak(f"Gathering the weather information of {city}...")
				print(f"Gathering the weather information of {city}...")
				print(all_data1)
				speak(all_data1)
				print(all_data2)
				speak(all_data2)
			
			except Exception as e:
				pass

		elif 'month' in query or 'month is going' in query:
			def tell_month():
				month = datetime.datetime.now().strftime("%B")
				speak(month)
			
			tell_month()

		elif 'today' in query:
			def tell_day():
				day = datetime.datetime.now().strftime("%A")
				speak(day)
				
			tell_day()
		
		elif "restart" in query: 
			subprocess.call(["shutdown", "/r"])
	    
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")
		
		elif "schedule my day" in query:
			tasks = []
			speak("Do you want to clear old tasks (Yes or No)")
			query = takeCommand().lower()
			if "yes" in query:
				file = open(r"C:\\Users\\User\\Desktop\\Alfred Waiter v1\\tasks.txt", 'w')
				file.write(f"")
				file.close()
				
				no_tasks = int(input("Enter the number of tasks: "))
				i = 0
				for i in range(no_tasks):
					tasks.append(input(f"Enter task {i}: "))
					file = open(r"C:\\Users\\User\\Desktop\\Alfred Waiter v1\\tasks.txt", 'a')
					file.write(f"{i}. {tasks[i]} \n")
					file.close()
			
			elif "no" in query:
				no_tasks = int(input("Enter the number of tasks: "))
				i = 0
				for i in range(no_tasks):
					tasks.append(input(f"Enter task {i}: "))
					file = open(r"C:\\Users\\User\\Desktop\\Alfred Waiter v1\\tasks.txt", 'a')
					file.write(f"{i}. {tasks[i]} \n")
					file.close()
		
		elif "see my schedule" in query:
			file = open(r"C:\\Users\\User\\Desktop\\Alfred Waiter v1\\tasks.txt", 'r')
			content = file.read()
			file.close()
			mixer.init()
			mixer.music.load(r"C:\\Users\\User\\Desktop\\Alfred Waiter v1\\musics\\notifications.wav")
			mixer.music.play()
			
			notification.notify(
				title="My Schedule:",
				message=content,
				timeout=15
			)

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('alfred.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("% H:% M:% S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("Alfred.txt", "r")
			print(file.read())
			speak(file.read(6))

		elif "update assistant" in query:
			speak("After downloading file please replace this file with the downloaded one")
			url = '# url after uploading file'
			r = requests.get(url, stream = True)
			
			with open("Voice.py", "wb") as Pypdf:
				
				total_length = int(r.headers.get('content-length'))
				
				for ch in progress.bar(r.iter_content(chunk_size = 2391975),
									expected_size =(total_length / 1024) + 1):
					if ch:Pypdf.write(ch)
					
		# NPPR9-FWDCX-D2C8J-H872K-2YT43
		elif "Alfred" in query:
			
			wishMe()
			speak("Alfred Voice Assistant Version 1")
			speak(assname)
		
		elif "send message " in query:
				# You need to create an account on Twilio to use this service
				account_sid = 'Account Sid key'
				auth_token = 'Auth token'
				client = Client(account_sid, auth_token)

				message = client.messages \
								.create(
									body = takeCommand(),
									from_='Sender No',
									to ='Receiver No'
								)

				print(message.sid)


		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(assname)

		# most asked question from google Assistant
		elif "will you be my gf" in query or "will you be my bf" in query:
			speak("I'm not sure about, may be you should give me some time")

		elif "i love you" in query:
			speak("It's hard to understand")

		elif "goodbye" in query or "offline" in query or "bye" in query:
			speak("Alright sir, going offline. It was nice working with you")
			sys.exit()

startExecution = MainThread()

import threading
import sys
from PyQt5.QtWidgets import QWidget,QLabel,QGraphicsDropShadowEffect,QApplication
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer,QTime,Qt

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("main.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:\jarvis\jarvis2.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:\jarvis\jarvis3.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        # timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QTime.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.label_5.setText(label_date)
        self.ui.label_7.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())