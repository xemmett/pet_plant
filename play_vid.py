# importing libraries
import cv2
import numpy as np
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO

cv2.namedWindow('Frame', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

interrupt = 0

def play_video(emotion):
	# Create a VideoCapture object and read from input file
	cap = cv2.VideoCapture(f'emotion/{emotion}/video.avi')

	# Check if camera opened successfully
	if (cap.isOpened()== False):
		print("Error opening video file")

	# Read until video is completed
	while(cap.isOpened()):
		
	# Capture frame-by-frame
		ret, frame = cap.read()
		if ret == True:
		# Display the resulting frame
			cv2.imshow('Frame', frame)
			
		# Press Q on keyboard to exit
			if cv2.waitKey(25) & 0xFF == ord('q'):
				break
			elif(interrupt):
				break

	# Loop video
		else:
			# cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
			break

	# When everything done, release
	# the video capture object
	cap.release()

def read_temp_humid():
	humidity, temperature = Adafruit_DHT.read_retry(11, 26)
	return humidity, temperature

def read_soil_moisture():
	reading = GPIO.input(6)
	if(reading):
		return 'savory'
	else:
		return 'thirsty'

def init_soil_sensor():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(6, GPIO.IN)

def main():
	init_soil_sensor()
	emotions = ['happy', 'freeze', 'thirsty', 'hot', 'savory', 'sleepy']

	# for emotion in emotions:
	# 	print(emotion)
	emotion = 'happy'
	while(1):
		# _, temperature = read_temp_humid()
		emotion = read_soil_moisture()
		# play_video(emotion)
		# if(50 > temperature > 36):
		# 	emotion = 'happy'
		# elif(temperature > 50):
		# 	emotion = 'hot'
		# elif(36 > temperature):
			# emotion = 'freeze'
		# print(temperature, emotion)
		print(emotion)


	# Closes all the frames
	cv2.destroyAllWindows()

main()