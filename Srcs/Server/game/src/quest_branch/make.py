#!/usr/local/bin/python
import os
os.system('rm -rf object')
for line in file('questlist'):
	if os.system('./qc ' + line):
		print 'Error occured on compile ' + line
		import sys
		sys.exit(-1)
