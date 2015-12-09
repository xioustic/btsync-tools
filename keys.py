from hashlib import pbkdf2_hmac
from base64 import b32encode, b64encode
from os import urandom
import unittest
from config import DEFAULT_ITERATIONS

def generateBaseKey(rootpass,sharename="index",iterations=DEFAULT_ITERATIONS):
	return b32encode(pbkdf2_hmac('sha256',rootpass,sharename,iterations))

def generateRWkeys(rootpass,sharename="index",iterations=DEFAULT_ITERATIONS):
	base = generateBaseKey(rootpass,sharename,iterations)
	rw = 'A'+base
	rwcrypt = 'D'+base
	return {'rw':rw,'rwcrypt':rwcrypt}

def generateRWkey(rootpass,sharename="index",iterations=DEFAULT_ITERATIONS):
	return generateRWkeys(rootpass,sharename,iterations)['rw']

def generateRWcryptkey(rootpass,sharename="index",iterations=DEFAULT_ITERATIONS):
	return generateRWkeys(rootpass,sharename,iterations)['rwcrypt']

def getSTOkeyFromROkey(rokey):
	assert rokey.startswith("E"), "Read-only Encrypted Keys start with E."
	assert len(rokey) == 59, "Read-only Encrypted Keys are 59 characters long."
	return 'F'+rokey[1:33]