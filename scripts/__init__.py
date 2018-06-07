from os.path import dirname, basename, isfile
import glob

#local
from scripts.ACM_search import ACM
from scripts.IEEE_search import IEEE
from scripts.Springer_search import Springer
from scripts.SCOPUS_search import Scopus
from scripts.Scidirect_search import Scidirect

#automated solution
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

#staric solution
#__all__ = ["ACM_search", "IEEE_search", "Scidirect_search", "SCOPUS_search", "Springer_search"]
