#import urllib2 library and csv module
import urllib2, csv

#import BeautifulSoup, the libary that the program uses to parse the html
from bs4 import BeautifulSoup

#create variable that will hold a csv file. Use open function to name the file and let python know that you'll be writing to the file
outfile = open('jaildata.csv', 'w')

#create writer object that will html will eventually write to
writer = csv.writer(outfile)

#store url of the website in a variable
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'

#use urllib2 to open and read the html from the url
html = urllib2.urlopen(url).read()

#parse the html from the url and put into a soup object, which has several methods
soup = BeautifulSoup(html, "html.parser")

#use beautiful soup to find the body of the table with the class 'stripe', store it as a string in a variable
tbody = soup.find('tbody', {'class': 'stripe'})

#use beautiful soup again to locate all tr elements from the tbody and store it in the rows variable
rows = tbody.find_all('tr')

#for loop to loop through each row in the table. This loop will run until there are no more rows left
for row in rows:

    #use beautiful soup to locate each individual cell in each table row
    cells = row.find_all('td')

    #create an empty array to store the data
    data = []

    #create a nested for loop to store each cell in the list
    for cell in cells:
        data.append(cell.text)

    #write each array into the csv
    writer.writerow(data)
