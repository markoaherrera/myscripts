#!/usr/bin/env python

""" 
Muestra resultado de busqueda en lynx
"""
import sys
import webbrowser as wb
import urllib

lk = wb.get('lynx')
termino = sys.argv[1]
url = 'http://lema.rae.es/drae/srv/search?val=' + urllib.quote_plus(termino)
lk.open(url)

