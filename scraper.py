import requests_html
import csv
from requests_html import HTMLSession

session = HTMLSession()

url = "https://www.leboncoin.fr/_immobilier_/offres"    # récupère l'url de la rubrique "immobilier"
r = session.get(url)
container = r.html.find(".styles_mainListing__PjWbm", first=True)   # colonne avec toutes les annonces de la page
a = container.absolute_links    # tableau avec les liens des annonces
# print(container.text)

for lien in a :
    r2 = session.get(lien)  # récupère le lien de chaque annonce
    summary = r2.html.find(".styles_Summary__Bcg1X", first=True)    # résumé de l'annonce (titre, prix, date de publication)
    descr = r2.html.find("._1fFkI", first=True)     # description de l'annonce
    # print(summary.text)
    # print(descr.text)
