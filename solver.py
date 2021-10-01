import speech_recognition as sr
import requests
import random
import string 
import time
import os

class funcapsolver():
	def get_token(host, pkey, proxy=None):
		if proxy == None:
			return requests.post(f'https://client-api.arkoselabs.com/fc/gt2/public_key/{pkey}', data={'bda': '','public_key': pkey,'site': host,'userbrowser': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36','rnd': f'0.{random.choice("12334565789")}'}).json()['token']
		else:
			return requests.post(f'https://client-api.arkoselabs.com/fc/gt2/public_key/{pkey}', proxies={'all://': proxy}, data={'bda': '','public_key': pkey,'site': host,'userbrowser': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36','rnd': f'0.{random.choice("12334565789")}'}).json()['token']

	def recognizeAudio(audiofilename):
		recognize = sr.Recognizer()
		with sr.AudioFile(audiofilename + '.wav') as s:
			data = recognize.record(s)
			raw = recognize.recognize_google(data)
			answer = ''
			for char in raw:
				if char.isdigit():
					answer += char
			return answer

	def solveCaptcha(token, proxy=None):
		session_token = token.split('|')[0]
		if proxy == None:
			getcaptchaAudio = requests.get(f'https://client-api.arkoselabs.com/fc/get_audio/?session_token={session_token}&analytics_tier=40&r=us-east-1&game=1&language=en')
		else:
			getcaptchaAudio = requests.get(f'https://client-api.arkoselabs.com/fc/get_audio/?session_token={session_token}&analytics_tier=40&r=us-east-1&game=1&language=en', proxies={"all://": proxy})
		audiornd = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7)) 
		open(rf"{os.getcwd()}\audios\{audiornd}" + '.wav', 'wb+').write(getcaptchaAudio.content)

		attemptSolve = requests.post('https://client-api.arkoselabs.com/fc/audio/', proxies=proxy,
		headers = {
			'authority': 'client-api.arkoselabs.com',
			'accept': '*/*',
			'cache-control': 'no-cache',
			'x-newrelic-timestamp': str(round(time.time())),
			'x-requested-with': 'XMLHttpRequest',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://client-api.arkoselabs.com',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'cors',
			'sec-fetch-dest': 'empty',
			'accept-language': 'en-US,en;q=0.9'
		},
		data = {
			'session_token': session_token,
			'language': 'en',
			'r': 'us-east-1',
			'audio_type': '2',
			'response': funcapsolver.recognize(rf"{os.getcwd()}\audios\{audiornd}"),
			'analytics_tier': '40'
		})
		try:
			if attemptSolve.json()['response'] == 'correct':
				return attemptSolve.json()
			elif attemptSolve.json()['response'] != 'correct':
				return False
			else:
				return False
		except KeyError as key:
			return key, False
