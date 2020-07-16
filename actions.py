from __future__ import absolute_import      # __future enables new language features
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
import sys
import logging
import json
import os
import yaml
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset


## You only have to replace XXXX in the url in your action file with your own api which you can get for free at http://www.wheatherstack.com
class Actionweatherapi(Action):
	def name(self):
		return "actions.weatherapi"

	def run(self, dispatcher, tracker, domain):
		import requests
		location = tracker.get_slot('location')
		if location == 'None':
			location = 'fetch:ip'
		api_result = requests.get('http://api.weatherstack.com/current?access_key=XXXX&query={}'.format(location))
		api_response = api_result.json()
		country = api_response['request']['query']
		condition = api_response['current']['weather_descriptions']
		temperature_c = api_response['current']['temperature']
		humidity = api_response['current']['humidity']
		wind_mph = api_response['current']['wind_speed']
		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} Kilometers/Hour.""".format(condition, country, temperature_c, humidity, wind_mph)
		dispatcher.utter_message(response)
		return [AllSlotsReset()]
