#!/usr/bin/python3 
import sys 
sys.path.insert(0,"/var/www/deletelater/") 
sys.path.insert(0,"/var/www/deletelater/deletelater/") 
 
import logging
logging.basicConfig(stream=sys.stderr) 
 
from deletelater import app as application
