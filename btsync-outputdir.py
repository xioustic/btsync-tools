import yaml
from getpass import getpass
from base64 import b32encode
from hashlib import pbkdf2_hmac

with open('directory.yaml','r') as f:
	yamltext = f.read()

directory = yaml.load(yamltext)

p = getpass("Type directory password: ")

print directory

getpass("Press any key to continue.")