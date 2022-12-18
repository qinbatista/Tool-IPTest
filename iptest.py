#!/usr/bin/env python3
import os
import sys
if __name__ == "__main__":
	if len(sys.argv)>=2:
		os.system('curl http://us.qinyupeng.com:7031/ip/'+sys.argv[1])
	else:
		os.system('curl http://us.qinyupeng.com:7031/ip/myself')