'''
Program Name: DCA Scraper
Created: March 12, 2017
Modified: March 16, 2017
Purpose: Obtain information from websites, then parse the
information.
'''
#-----------------------------------------------------------
''' Import urllib and BeautifulSoup 4 for obtaining
website info and then parsing''' 

import urllib.request;
from bs4 import BeautifulSoup;

#-----------------------------------------------------------
# Assigning variables
website = urllib.request.urlopen('http://www.5dca.org/Opinions/Opin2017/030617/filings%20030617.html');
soup = BeautifulSoup (website,"html5lib");
#-----------------------------------------------------------
print(soup.get_text());

