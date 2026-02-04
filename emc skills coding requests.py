import bs4
from zenrows import ZenRowsClient
def setup():
    client = ZenRowsClient("03ff11887df69baf7734e5004d31df65ef00fa04")
    url = "https://www.helis.com/database/manufacturer/136/"
    params = {"mode":"auto"}
    response = client.get(url, params=params)
    soup = bs4.BeautifulSoup(response.text,features="html.parser")
    return(client,params,soup)

def findLinks(soup):
    links = soup.select("a")
    linkstrings = []
    for L in links:
        string=L.get("href")
        if string is not None and "model" in string:
            linkstrings.append(string)
    return(linkstrings)

def findChildren(linkstrings,client,params):
    helis = [[]]
    for L in linkstrings:
        L = "https://www.helis.com" + L
        response = client.get(L,params=params)
        soup = bs4.BeautifulSoup(response.text,features="html.parser")
        trs = soup.select("tr")
        for tr in trs:
            if ('trcnmod"' in tr.text):
                tds=tr.findChildren("tds", recursive = False)
                data = tds.findChildren(recursive = False)
                for cell in data:
                    print(cell.text)
                name = L[37:len(L)-1]
                helis.append([name,tr])
    return(helis)

def main():
    client, params, soup = setup()
    linkstrings = findLinks(soup)
    helis = findChildren(linkstrings,client,params)
    print(helis)

main()