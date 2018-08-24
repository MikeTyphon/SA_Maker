#! python3

# this is a python program for Hi5 Access to aid in our service agreement workflow

from __future__ import print_function
from mailmerge import MailMerge
from datetime import date

template = "TypeWell-Cart-Service-Agreement(template).docx"

templatepath = r'C:\Users\Owner\Dropbox'

document = MailMerge(template)
print(document.get_merge_fields())
