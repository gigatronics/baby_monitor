#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import subprocess
import sys
import re
import time

def main(args=None):

    #todo offset,root via param
    #root = "/mnt/flash/capture/"
	root="/home/pi/python-noise-detection/"
	offset = 0.12 # user defined
	counter = 0

	try:
		while True:
			filedate = time.strftime("%Y%m%d-%H%M%S")
            		filename = root + filedate + ".wav"
            		#if not root current then uncomment
			#filename = filedate + ".wav"
			#print(filename)
			proc = subprocess.Popen(['/bin/bash',root+'sox.sh', filename, '3' ], stdout=subprocess.PIPE)
			result,errors = proc.communicate()
			amplitude = float(result)
			print(amplitude)
			if amplitude >= offset:
				os.remove(filename)

                		print 'Sound detected - amplitude was ' + str(amplitude)
            			counter=counter+1
				if counter==3:
					proc2 = subprocess.Popen(['/bin/bash',root+'ssmtp.sh'], stdout=subprocess.PIPE)
					results2, errors2 = proc2.communicate()
					print('Notification sent')
					counter = 0
			else:
                		os.remove(filename)
	#todo other except handler
	except KeyboardInterrupt:
        	print('')
	finally:
        	print('')

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]) or 0)
