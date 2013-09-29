import os
import time

#directories to be backed up in a list
source = ['C:\Documents and Settings\Family\Desktop\python\python-adventure']

#backup directory
target_dir = '\backup'

#filename
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr '%s' %s" % (target,' '.join(source))

if os.system(zip_command) == 0:
	print 'Successfully backup to ',target
else:
	print 'Backup Failed'
