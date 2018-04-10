import urllib2, csv
from bs4 import BeautifulSoup

outfile = open('accidents.csv', 'w')
writer = csv.writer(outfile)

url = 'https://www.mshp.dps.missouri.gov/HP71/SearchAction?searchDate=04/03/2018'
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', {'class': 'accidentOutput'})
rows = table.find_all('tr')

for row in rows[1:]:
    cells = row.find_all('td')
    data = []
    for cell in cells:
        data.append(cell.text.encode('utf-8'))
    writer.writerow(data)
