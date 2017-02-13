# Aesop87
Fund raise like a career politician ;)

First, download and setup python 2.7:

https://www.python.org/download/releases/2.7/

Second, the following modules for python: requests, urllib2, zipfile, os, StringIO, csv, sys, lxml, html, time, openpyxl, Workbook

In your command prompt/terminal type:

pip install requests

Repeat for all modules.

Third, download the FEC data harvester (2011-2017)

In your command prompt/terminal type:

python fec_data_harvester.py

It's a lot of data, so make sure you have space on your hard drive.

(Tip: If you want to download one year at a time, in line 15 remove the years you don't want, and leave the one you do want)

Clean your spreadsheets so that Column A is Last Name, Column B is First Name, Column F is City, and Column G is State. 

Fourth, download the phone number scraper.

In lines 6, 7, and 25 change the name and workbook name to whatever your spreadsheet is titled (Currently: Ch4llengerTV.xlsx, Ch4llengerTV, Ch4llengerTV.csv -- change to: YourFileName.xlsx, YourWorkbookName, YourFileName.csv)

In your command prompt/terminal type:

python phone_number_scraper.py

A new comma serparated value (.csv) file should appear that will include the phone numbers of individual donors.

Call the donors and ask them for a donation.

Mail or email them a letter and some campaign collateral with a remit envelope to send back donations in.

Wait about a week and the contributions should start rolling in.

Good luck!
