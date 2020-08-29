from bs4 import BeautifulSoup
from os import popen, system, environ
import requests

GH_TOKEN = environ['GH_TOKEN']
GIST_ID = environ['GIST_ID']

def findTd2(classname):
    return classname is not None and classname == 'td-02'
def updateGist(fileName, content):
    header = {'Authorization': f'token {GH_TOKEN}'}
    jsonContent = {
        "files": {
            fileName: {
                "content": content,
                "filename": fileName
            }
        }
    }
    url = f"https://api.github.com/gists/{GIST_ID}"
    responseTab = requests.patch(url = url, headers = header, json = jsonContent)

if __name__ == '__main__':
    topHot = ""
    html = popen("curl https://s.weibo.com/top/summary?Refer=top_hot").read()
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(class_=findTd2)
    # soup.find_all("a", class_ = "td-02")
    index = 0
    for item in items:
        text = item.find('a').get_text()
        if index == 0:
            topHot += f"Pin {text}"
        else:
            topHot += f"{index} {text}"
        topHot += '\n'
        index += 1
    topHot = topHot[:-1]
    updateGist('SinaTopHot.txt', topHot)
    



