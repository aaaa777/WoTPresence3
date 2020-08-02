import time
from pypresence import Presence
import sys
from presencereader.server import *


def main():
	
	RPC = Presence(737286157456506940)
	RPC.connect()

	reader = Reader()
	
	while True:

		try:
			data = reader.read_json()
		except Exception:
			data = None
		

		if data is None:
			break

		RPC.update(**data)

	RPC.close()


if __name__ == '__main__':
	if '--modname' in sys.argv:
		sys.exit(200)
	else:
		main()

	sys.exit()