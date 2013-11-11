import sys
import urllib
import webbrowser

def busca_rae(termino):
    searchUrl = 'http://lema.rae.es/drae/srv/search?val=' \
		    + urllib.quote_plus(termino)
    webbrowser.open_new_tab(searchUrl)

ter = sys.argv[1]

if ter is not None and len(ter) > 0:
    busca_rae(ter) 
