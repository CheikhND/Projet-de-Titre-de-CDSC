from Atelier2.scraper.lesparticuliersClass import Lesparticuliers

url1="https://www.lesparticuliers.fr/vehicules/voitures/"


p= Lesparticuliers(url1)
p.get_annonces(" ",104)
p.toJsonFile("data_lesparticuliers.json")
p.toCsvFile("data_lesparticuliers.csv")


