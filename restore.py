#!/usr/bin/python
import os, re 
from datetime import datetime

r = re.compile(r"^(.*?) \((\d{4}_\d{2}_\d{2} \d{2}_\d{2}_\d{2}) UTC\)(?:\.(.*?))?$")
now = datetime.now()

def clean(directory):
	print "called clean on %s" % directory
	entries = dict()
	for item in os.listdir(directory):
		if os.path.isdir("%s/%s" % (directory, item)) == True:
			clean("%s/%s" % (directory, item))
		else:
			if r.match(item):
				m = r.search(item)
				fname = m.group(1)
				date = m.group(2)
				ext = m.group(3)
				if not entries.has_key((fname,ext)):
					entries[(fname,ext)] = []
				entries[(fname,ext)].append((item, datetime.strptime(date,"%Y_%m_%d %H_%M_%S")))
			else:
				print "%s/%s didn't match!" % (directory, item)
	for k in entries:
		target = directory + "/" + k[0] 
		if k[1] != None:
			target += "."+k[1]
		if not os.path.exists(target):
			sel = reduce(lambda x,y: x[1] < now and x[1] > y[1] and x or y,entries[k])
			os.rename("%s/%s" % (directory, sel[0]), target)
			notsel = filter(lambda x: x != sel, entries[k])
			for i in notsel:
				os.remove("%s/%s" % (directory, i[0]))
		else:
			for i in entries[k]:
				os.remove("%s/%s" % (directory, i[0]))

if __name__ == '__main__':
	cwd = os.getcwd()
	clean(cwd)
