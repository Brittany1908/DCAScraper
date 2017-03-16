'''
Program Name: DCA Scraper
Created: March 12, 2017
Modified: March 15, 2017
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

#-----------------------------------------------------------
# parse the obtained html using beautiful soup. Store in soup.
soup = BeautifulSoup(website, 'html.parser');

#-----------------------------------------------------------
# Print all links as a sting.
for link in soup.findAll('a'):
    print (link.string);

# Currently only written opinions are printed. Not PCAs