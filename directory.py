import os
import json

import yaml

import keys
import verify

from config import DEFAULT_ENCRYPT, DEFAULT_ITERATIONS

class BTSync_Directory:
	def __init__(self, path=None):
		self.path = path

		# default data
		self.data = {"nodes":[],"shares":[]}

		if path is not None:
			# if file exists, load from it
			if os.path.isfile(path):
				self.load()
			# else if path is not none, save
			elif path is not None:
				self.save()

	def load(self, path=None):
		"""Load data from a file.

		If path is provided, the Directory assumes that is
		its new path."""
		if path is not None:
			self.path = path

		path = self.path

		with open(path,'r') as f:
			filedata = f.read()
		
		if path.endswith('.json'):
			self.data = json.loads(filedata)
		else:
			self.data = yaml.load(filedata)

		return True

	def save(self, path=None):
		"""Persist data in a file.

		If path is provided, the Directory assumes that is
		its new path."""
		if path is not None:
			self.path = path

		path = self.path

		with open(path,'w') as f:
			if path.endswith('.json'):
				f.write(self.to_json())
			else:
				f.write(self.to_yaml())

		return True

	def to_yaml(self):
		"""Return YAML representation of Directory data."""
		return yaml.dump(self.data,default_flow_style=False)

	def to_json(self):
		"""Return JSON representation of Directory data."""
		return json.dumps(self.data)

	def to_html(self):
		"""Return HTML representation of Directory data."""
		assert False, "Not yet implemented"

	def display_nodes(self):
		"""Display a list of known nodes with their indexes."""
		return [x for x in enumerate([x['name'] for x in self.data['nodes']])]

	def get_node(self, nodeidx):
		"""Get all information about a node by index."""
		return self.data['nodes'][nodeidx]

	def add_node(self, name, ip, url):
		"""Add a node to the list of known nodes."""
		return self.data['nodes'].append({'name':name,'ip':ip,'url':url})

	def display_shares(self):
		"""Display a list of known shares with their indexes."""
		assert False, "Not yet implemented"

	def get_share(self, shareidx, rootpass=None):
		"""Get all information about a share by index.

		Optionally, provide a rootpass keyword argument to
		attempt to verify and display the RW key for the share.
		"""
		# if rootpass is provided, check it
		# if check passes, also return RW key
		assert False, "Not yet implemented"

	def add_share(self, name, description, iterations=DEFAULT_ITERATIONS, rootpass=None, encrypted=DEFAULT_ENCRYPT):
		"""Add a share to the list of known shares.

		Keyword arguments:
		rootpass -- If provided, a set of verification parameters will be stored.
		encrypted -- If False, will generate a standard RW key instead of an encrypted
		one.
		"""
		# If rootpass is not given, we leave verify and verifysalt blank.
		# Otherwise, calculate a verify and verifysalt

		# TODO: Verify this share doesn't already exist! Check for same name and same iterations, then verify key.
		assert False, "Not yet implemented"

	def swap_share(self, idx1, idx2):
		"""Swap the position of two shares given the index of each."""
		self.data['shares'][idx1], self.data['shares'][idx2] = self.data['shares'][idx2], self.data['shares'][idx1]