# pdf-forensic

Overview
=========
pdf-forensic is a PDF file investigation tool that extracts the MetaData from the PDF file and prints it on the screen. From the MetaData, it is possible to find out the author name of the PDF file, modification date, creation date, what technology was used to create the file, and more. It's a great tool focused on forensic investigation. This forensic investigation proved useful in the arrest of a member of the hacker group Anonymous in 2010.

Forked from https://github.com/xovim001/pdf-forensic

Requeriments
============
1. Python 3.x
2. Before running the tool, please install the PyPDF2 module and Python. To do that, please follow the command:
  
   `pip/pip3 install PyPDF2`

Compatibility:
============
Tested on Python 3 installed on macOS

Usage
=====
Navigate to the file folder and run the following command:

python pdf-forensic.py -F <File Name>

Examples
========
`python/python3 pdf-forensic.py -F test.pdf`

Bugs & Contact
==============
Feel free to mail me with any problems, bugs, suggestions, or fixes at:

Ewin – rahmanewin@gmail.com
