import json
import os

class configurator:
	
	def __init__(self):
		# system properties are stored here
		self.properties = {
			"configuration":"configuration.json"
		}

		# gives the absolute path to configuration file
		self.absolute_configuration_path = "%s/%s" % (os.path.dirname(os.path.abspath(__file__)),self.properties["configuration"])

		# reads the configuration from the specified configuration file
		self.configuration = json.load(open(self.absolute_configuration_path))

	def register(self):
		return self.configuration["Engine"]["signature"]

