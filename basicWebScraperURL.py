'''
Program Name: DCA Scraper
Created: March 12, 2017
Modified: April 25, 2017
Purpose: Obtain information from websites, then parse the
information.
'''
#-----------------------------------------------------------
''' Import csv, urllib, and BeautifulSoup 4 for obtaining
website info and then parsing''' 
import csv;
import urllib.request;
from bs4 import BeautifulSoup;

#-----------------------------------------------------------
#Open File
resultFile = open("output.csv", 'w')

#-----------------------------------------------------------
# Assigning variables
website = urllib.request.urlopen('http://www.5dca.org/Opinions/Opin2017/030617/filings%20030617.html');

#-----------------------------------------------------------
# parse the obtained html using beautiful soup. Store in soup.
soup = BeautifulSoup(website, 'html.parser');

#-----------------------------------------------------------
# Print all links as a string for visual and defines data 
for link in soup.find_all('a'):    
    print(link.string);    
    # write to file    
    results = [link.string];    
    for everyCase in results:        
        resultFile.write(everyCase + "\n")
#-----------------------------------------------------------  
# Close file
resultFile.close()

# Currently only written opinions are printed. Not PCAs
