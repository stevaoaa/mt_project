from selenium import webdriver
from ACM_search import ACM
from IEEE_search import IEEE
from Scidirect_search import Scidirect
from SCOPUS_search import Scopus
from Springer_search import Springer

base_dir = '/home/stevao/workspace'
source_dir = base_dir + '/mt_project/scripts/drivers/chromedriver'

driver = webdriver.Chrome(source_dir)

strings_Busca = ["\"Software Testing\"", "\"Oracle\""]

for iCount in range(len(strings_Busca)):
    obj = IEEE(strings_Busca[iCount], driver)
    results = []
    results = obj.test_IEEE()
    print(results)
