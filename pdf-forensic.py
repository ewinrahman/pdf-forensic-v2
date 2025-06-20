#!/usr/bin/env python
import argparse
import PyPDF2

def printMeta(filename):
	with open(filename, 'rb') as f:
		pdfFile = PyPDF2.PdfReader(f)
		docInfo = pdfFile.metadata
		print('[*] PDF MetaData for: ' + str(filename))
		for metaItem in docInfo:
		    print('[+] ' + metaItem + ': ' + docInfo[metaItem])

def getUrl(filename):
	with open(filename, 'rb') as f:
		reader = PyPDF2.PdfReader(filename)
		for page_num, page in enumerate(reader.pages):
			if "/Annots" in page:
				annotations = page["/Annots"]
				for annot in annotations:
					annot_obj = annot.get_object()
					if "/A" in annot_obj:
						action = annot_obj["/A"]
						if "/URI" in action:
							print(f"Page {page_num + 1}: {action['/URI']}")
	

def main():
	parser = argparse.ArgumentParser('usage program: -F <PDF file name>')
	parser.add_argument('-F', '--file', dest='fileName', required=True, help='Please specify the PDF File name')
	args = parser.parse_args()
	printMeta(args.fileName)
	getUrl(args.fileName)

if __name__ == '__main__':
	main()
