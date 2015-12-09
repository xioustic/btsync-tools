from base64 import b32encode
from hashlib import pbkdf2_hmac
from getpass import getpass
from sys import exit
from commands import getstatusoutput

passroot = getpass("Please enter the password root for the share: ")

if passroot != "":
	passroot2 = getpass("Please enter password again (or blank to skip): ")
	if passroot2 != "" and passroot != passroot2:
		getpass("Invalid password, please relaunch and try again.")
		exit()

	salt = raw_input("Please enter the share name (default \"index\"): ")
	iterations = raw_input("Please insert number of iterations (default 100000): ")

	salt = salt if salt != "" else "index"
	iterations = int(iterations) if iterations != "" else 100000

	rw = b32encode(pbkdf2_hmac('sha256',passroot,salt,iterations,20))
	rwreg = "A"+rw
	rwenc = "D"+rw

	print ""
	print "Regular r/w key: "+rwreg
	print "Encrypted r/w key: "+rwenc
	print ""

	# try to use command line to get the ro secret automatically
	roreg = ""
	roenc = ""
	for exe_name in ['./bin/btsync_arm', './bin/btsync_freebsd_i386', './bin/btsync_i386', 
	                 './bin/btsync_glibc23_i386', './bin/btsync_x64', 
	                 './bin/btsync_freebsd_x64',  './bin/btsync_glibc23_x64']:

		status, output = getstatusoutput(exe_name+' --get-ro-secret '+rwreg)
		if status == 0:
			roreg = output
			_, roenc = getstatusoutput(exe_name+' --get-ro-secret '+rwenc)
			# print 'success on '+exe_name
			# don't bother with other binaries once we got a success
			break

	if roreg != "":
		print "Regular r/o key: "+roreg
		print "Encrypted r/o key: "+roenc

if roenc == "":
	roenc = raw_input("Paste encrypted r/o key to generate r/o encrypted store: ")	

if roenc != "":
	if not (roenc.startswith("E") or len(roenc) != 59):
		print "Malformed r/o key."
	else:
		rostore = 'F'+roenc[1:33]
		print "Encrypted-Store r/o key: "+rostore
		
	print ""
	raw_input("Press any key to continue.")

exit()