import base64
import json
import os
import numpy as np
from pprint import pprint
import time
# import sounddevice as sd
# from google.cloud import speech
import speech_recognition as sr
import soundfile as sf


SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
GOOGLE_KEY = 'AIzaSyDrsRthQWFeg4pk7w4NzQNImUB5ADGH8_Y'
hints = ['um','er','uh','huh','well','hmm','hm','like']
BING_KEY = 'd0d082f772c640a9bf00f3d425f22c2a'


def read_data():

	with open(os.path.join(SITE_ROOT,'../rawAud.txt'), 'r') as f:
		bytes = json.load(f)


	array = np.zeros(len(bytes),dtype=float)
	for k,v in bytes.items():
		array[int(k)] = float(v)


	sf.write(os.path.join(SITE_ROOT,'../test.flac'), array, 16000)

	return array


def parse_request(data):

	# # data = request.json
	# with open(os.path.join(SITE_ROOT,'../sampleData.txt'), 'r') as f:
	# 	data = json.load(f)
	# print(data)
	id = data['id']
	audio = data['audio']
	array = np.zeros(len(audio),dtype=float)
	for k,v in audio.items():
		array[int(k)] = float(v)


	sf.write(os.path.join(SITE_ROOT,'../test2.flac'), array, 44100)
	# print(array)

def transcribe(json):
	parse_request(json)
	# speech_client = speech.Client()
	# with open(os.path.join(SITE_ROOT,'../test2.flac'), 'rb') as f:
	# 	content = f.read()
	# 	audio_sample = speech_client.sample(
	# 		content=content,
	# 		encoding='FLAC',
	# 		sample_rate_hertz=44100)
	# try:
	# 	alternatives = audio_sample.recognize(
	# 		language_code='en-US',
	# 		max_alternatives=1,
	# 		speech_contexts=hints)

	# 	for alternative in alternatives:
	# 		print('Transcript: {}'.format(alternative.transcript))
	# 		print('Confidence: {}'.format(alternative.confidence))

	# 	return alternative.transcript,alternative.confidence

	# except ValueError:
	# 	print('No results returned from the Speech API.')
	AUDIO_FILE = os.path.join(SITE_ROOT,'../test2.flac')
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source)

	# recognize speech using Google Speech Recognition
	try:
		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		# instead of `r.recognize_google(audio)`
		# print("Google: " + r.recognize_google(audio))
		# print("Sphinx: " + r.recognize_sphinx(audio))
		# print("Google Cloud: " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_KEY))
		response = r.recognize_bing(audio, key=BING_KEY, show_all=True)
		if 'results' in response:
			transcript = response['results'][0]['name']
			confidence = response['results'][0]['confidence']
			print('Transcript: ', transcript)
			print('Confidence: ', confidence)
			
			return 'yes'

	except sr.UnknownValueError:
		print("could not understand audio")
	
	except sr.RequestError as e:
		print("Could not request results peech Recognition service; {0}".format(e))    

	return 'None'






