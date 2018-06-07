from os.path import dirname, basename, isfile
import glob

#local
import ACM_search 
import IEEE_search
import Scidirect_search
import SCOPUS_search
import Springer_search

#automated solution
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

#staric solution
#__all__ = ["ACM_search", "IEEE_search", "Scidirect_search", "SCOPUS_search", "Springer_search"]
