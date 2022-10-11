import csv
import json

import requests
from bs4 import BeautifulSoup


class Lesparticuliers:
    def __init__(self,url=''):
        self.url = url
        file= open("config.json")
        self.config=json.load(file)
        self.annonces=[]
        print(self.config)

    def get_annonces(self,motcle,n):

        page = 1
        while True:
            if page>n:break
            blocs = self.get_blocs(page,motcle)
            if len(blocs) == 0: break;
            for bloc in blocs:
                self.annonces.append(self.blocToDict(bloc))
            page += 1
        return self.annonces

    def blocToDict(self,bloc):
        dict={}
        dict['Titre'] = bloc.select_one(self.config["Titre"]).text.strip()
        dict['Prix'] = bloc.select_one(self.config["Prix"])
        if dict['Prix']!=None: dict['Prix']=dict['Prix'].text.strip()
        dict['Ville'] = bloc.select_one(self.config["Ville"]).text.strip().split('-')[1].strip()
        dict['Date'] = bloc.select_one(self.config["Date"]).text.strip()
        return dict


    def get_blocs(self,page,motcle):
        contenu = requests.get(self.url, data={'p': page,"motcle":motcle})
        soup = BeautifulSoup(contenu.text, "html.parser")
        # lastPage = soup.select_one("ul.pagination>li:last-of-type").text
        blocs = soup.select("div.white.category-grid-box-1.pave")
        return blocs

    def toJsonFile(self,path):
        jsonString=json.dumps(self.annonces,ensure_ascii=False)
        file= open(path,"w",encoding="UTF-8")
        file.write(jsonString)
        file.close()

    def toCsvFile(self,path):
            fielNames=["Titre","Prix","Ville","Date"]
            file = open(path, "w", encoding="UTF-8")
            writer=csv.DictWriter(file,fieldnames=fielNames)
            writer.writeheader()
            writer.writerows(self.annonces)
            file.close()