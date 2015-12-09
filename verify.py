from base64 import b32encode, b64encode
from hashlib import pbkdf2_hmac
from os import urandom

def generateVerification(rootpass,iterations=100000):
	verifysalt = b32encode(urandom(65))
	verify = b64encode(pbkdf2_hmac('sha256',rootpass,verifysalt,iterations))
	return {'iterations':iterations,'verify':verify, 'verifysalt':verifysalt}

def verify(rootpass,salt,iterations,payload):
	return verify == b64encode(pbkdf2_hmac('sha256',rootpass,verifysalt,iterations))