import subprocess
import os
import inspect 

vocab = {"help":"true","copyright":"true","credits":"true","license":"true","generate_app":"true"}

class handle:
	def help(self):
		print("preparing help prompt")
		
	def credits(self):
		print("author : sachin kumbhojkar")

	def copyright(self):
		print("Copyright (c) 2015-2016 Clevershell Software Foundation.\nAll Rights Reserved.")

	def generate_app(self):
		app_name = raw_input("App name : ")
		print("Generating app %s " % app_name)
		system_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))), "../"))
		subprocess.call("mkdir %s/%s" % (system_path,app_name),shell=True)		
