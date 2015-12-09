Intent
======
The intention of these utilities are to allow
recovery of BTSync keys at a later date by making
them deterministic in a (hopefully) cryptographically
secure way and also to create cryptographically secure
directories of shares that could be stored in a
relatively untrusted environment.

Key Generation
==============
Assumptions
-----------
When BTSync generates a 1.4-style read-write key, it just
requires a random, unique set of 20-bytes base32 encoded.
If BTSync's natively generated keys have special mathematical
properties, these utilities would undermine and
potentially completely break the security behind BTSync.
This cannot be easily verified as BTSync is a closed-source
project.

Algorithm for Generating Deterministic Keys
-------------------------------------------
Deterministic r/w keys are generated using the
pbkdf2 algorithm using sha256 over a variable
number of iterations. The root password and share
name (used as a salt) with a desired key length
of 20 bytes generates the bits needed for the key,
which is then base32 encoded. An "A" is prepended
if the share is not to be encrypted; a "D" is prepended
if the share is to be encrypted.

Usage
-----
Use ./btsync-keygen.py and you will be walked thru steps
to generate a key. Preferribly, do this on a Linux or
FreeBSD-based system to have Read-Only keys also retrieved
using the included btsync binaries.

Directories
===========
Directory Contents
----------------
A directory contains shares with the name, iterations,
and a description of shares. In addition, mechanisms for
checking correct key are provided.

Checking Directory Passwords
----------------
Each share's verifysalt is a randomly generated string to 
be used as a pbkdf2 salt against the correct password with
the given iterations. Verify is the base64 encode of the 
payload of the pbkdf2 function.

Generating Random Strings
----------------
It is assumed that base64.b32encode(os.urandom(65)) is 
secure enough when generating random strings for salts
for directory listing password verification.
