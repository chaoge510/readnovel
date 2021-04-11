import bs4
import requests

doc = open("/Users/leon/Downloads/novel.txt",'w')

for s in range(868,957):
    xml = 'https://518xs.com/Info/Detail/17561' + str(s) + '.html'

    res = requests.get(xml)
    res.encoding = 'utf-8'
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    m = soup.find('div', class_ = 'InfoContent')
    s = m.get_text()
    doc.write(s)