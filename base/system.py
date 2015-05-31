import handlers
from handlers import handle
class system:

	def setup(self,signature):	
		banner = ("\nIterator 1.0"
                                "\nLicense : GNU GPL"
                                "\nType 'help', 'copyright', 'credits' or 'license' for more information."
                                "\n\nIterator is an open source command line framework for python registered under GNU GPL"
                                "\nWe invite you to improve the system better.\n\n")
		self.prompt(banner)
		self.listener(signature)

	def listener(self,signature):
		user_input = raw_input(signature)
		try:
			if(handlers.vocab[user_input]):
				handler_instance = handle()
				getattr(handler_instance,user_input)()
		except:
			self.prompt("command not found : %s" % user_input)
		self.listener(signature)

	def prompt(self,message):
		print(message)
