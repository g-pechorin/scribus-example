#
# run me like this ...
#   > scribus -ns -g -py script-final.py
# ... probably.
# I only tested it on Windows7/x64 with the "stock" portable Scribus 1.5.7

import scribus

scribus.openDoc('Document-1.sla')

# open our file to get the pile-of-scrawlings we want to make into stuff
for index, line in enumerate(open('script-final.txt').readlines()):
	# need to select the object, then, change the text
	scribus.selectObject('Text1')	
	scribus.setText(line)

	# save the PDF as we have been told
	pdf = scribus.PDFfile()
	pdf.file = ('file'+str(index)+'.pdf')
	pdf.save()
