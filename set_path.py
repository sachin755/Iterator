import sys
import os
import inspect
# inserting paths into python paths

if getattr(sys, 'frozen', False):
	#It will give the path of main executable file for the program
	BIN_DIR = os.path.dirname(sys.executable)	
else:
	# It will give this file's absolute path
	BIN_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

if(BIN_DIR not in sys.path):
	# It will insert Application's Bin folder's path in the python's sys.path variable
	sys.path.insert(0, BIN_DIR)

# ROOT_DIR will take to the main executable file
ROOT_DIR = os.path.abspath(os.path.join(BIN_DIR, "./"))
if(ROOT_DIR not in sys.path):
	# It will insert Application's Root folder's path in the python's sys.path variable
	sys.path.insert(0, ROOT_DIR)

LIB_DIR = os.path.abspath(os.path.join(ROOT_DIR, "lib"))
if(LIB_DIR not in sys.path):
	# It will insert Application's Lib folder's path in the python's sys.path variable
	sys.path.insert(0, LIB_DIR)


CONF_DIR = os.path.abspath(os.path.join(ROOT_DIR, "config"))
if(CONF_DIR not in sys.path):
	# It will insert Application's conf folder's path in the python's sys.path variable
	sys.path.insert(0, CONF_DIR)

COMMON_DIR = os.path.abspath(os.path.join(ROOT_DIR, "common"))
if(COMMON_DIR not in sys.path):
	# It will insert Application's common folder's path in the python's sys.path variable
	sys.path.insert(0, COMMON_DIR)

LIB_DIR = os.path.abspath(os.path.join(ROOT_DIR, "bin"))
if(LIB_DIR not in sys.path):
        # It will insert Application's bin folder's path in the python's sys.path variable
        sys.path.insert(0, LIB_DIR)

BASE_DIR = os.path.abspath(os.path.join(ROOT_DIR, "base"))
if(BASE_DIR not in sys.path):
        # It will insert Application's bin folder's path in the python's sys.path variable
        sys.path.insert(0, BASE_DIR)
