from selenium import webdriver
from ACM_search import ACM
from IEEE_search import IEEE
from Scidirect_search import Scidirect
from SCOPUS_search import Scopus
from Springer_search import Springer

driver = webdriver.Firefox()

strings_Busca = ["\"Software Testing\""]

for iCount in range(len(strings_Busca)):
    obj = ACM(strings_Busca[iCount], driver)
    results = []
    results = obj.test_ACM()
    print(results)

    obj = IEEE(strings_Busca[iCount], driver)
    results = []
    results = obj.test_IEEE()
    print(results)

    obj = Scidirect(strings_Busca[iCount], driver)
    results = []
    results = obj.test_scidirect()
    print(results)

    obj = Scopus(strings_Busca[iCount], driver)
    results = []
    results = obj.test_Scopus()
    print(results)

    obj = Springer(strings_Busca[iCount], driver)
    results = []
    results = obj.test_springer()
    print(results)