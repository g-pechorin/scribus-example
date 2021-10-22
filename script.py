

import scribus

# > scribus -ns -g -py script.py

scribus.openDoc('Document-1.sla')

pdf = scribus.PDFfile()
pdf.file = ('as-is.pdf')
pdf.save()

