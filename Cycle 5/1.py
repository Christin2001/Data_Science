import requests
from bs4 import BeautifulSoup
print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")
def getdata(url):
    r=requests.get(url)
    return r.content
htmldata = getdata("https://www.toppr.com/guides/essays/globalization-essay/")
soup = BeautifulSoup(htmldata,'html.parser')
data =''
pr = len(soup.find_all('p'))
print("P tag:",pr)
for data in soup.find_all('p'):
    print(data.get_text())