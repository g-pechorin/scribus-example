

log = open('log.txt', 'w')

def out(line):
	log.write(';' + str(line) + '\n')
	log.flush()

def err(line):
	log.write('!' + str(line) + '\n')
	log.flush()

try:

	import scribus

	# ==
	# list all in scribus
	for item in dir(scribus):
		out("\tscribus: " + str(item))
	out('listed scribus')
	#
	# --


	# > scribus -ns -g -py script-logs.py

	out('starting up')

	scribus.openDoc('Document-1.sla')

	out('document open')

	pdf = scribus.PDFfile()
	pdf.file = ('as-is.pdf')
	pdf.save()

	out('saved as-is')

	# for item in scribus.getPageItems():
	# 	out("\titem: " + str(item))

	# out('items listed')

	# # ==
	# # setActiveLayer
	# scribus.setActiveLayer('Background')
	# out('set the layer')
	# #
	# # --

	
	# ==
	# selectObject
	scribus.selectObject('Text1')
	out('set the selectObject')
	#
	# --

	# ==
	# set the text
	out('trying with noting')
	scribus.setText('hello world')

	#out('trying with scribus')
	#scribus.setText('Text1', 'hello world')

	# out('trying with no scribus')
	# setText('Text1', 'hello world')
	
	out('hello set')
	#
	# --

	pdf.file = ('hello.pdf')
	pdf.save()

	out('hello saved')
except BaseException as e:
	err("fail because ...")
	err(e)
	err(dir(e))

log.close()
