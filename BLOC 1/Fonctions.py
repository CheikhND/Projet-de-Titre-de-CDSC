import requests
from bs4 import BeautifulSoup


def blocToDict(bloc):
    dict={}
    dict['titre'] = bloc.select_one("h2.cutWords").text.strip()
    dict['prix'] = bloc.select_one("span.ad-price.pricenew")
    if dict["prix"]!=None: dict["prix"]=dict["prix"].text.strip()
    dict['ville'] = bloc.select_one("p.location.MB10.cutWords:nth-of-type(2)").text.strip().split("-")[-1].strip()
    dict['date'] = bloc.select_one("p.location.MB10:nth-of-type(3)").text.strip()
    return dict


def get_bloc(url,page):
    contenu= requests.get(url, data={"p":page})
    soup = BeautifulSoup(contenu.text, "html.parser")
    blocs = soup.select("div.white.category-grid-box-1.pave")
    return blocs