import os
import set_path
from configurator import configurator
from system import system

configurator = configurator()
signature = configurator.register()

system = system()
system.setup(signature)
