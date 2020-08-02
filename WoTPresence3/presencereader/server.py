import sys
import json

class Reader:
		
	def __init__(self):
		self.reader = sys.stdin
	
	def listen_stdout(self):
		
		# blocking io
		return self.reader.readline()
		
	def read_json(self):
		return json.loads(self.listen_stdout())
