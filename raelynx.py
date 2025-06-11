#!/usr/bin/env python

""" 
Muestra resultado de busqueda en lynx. Gracias
"""
import sys
import webbrowser as wb
import urllib

if len(sys.argv) <= 1:
    print("Usage: raelynx.py <term>")
    sys.exit(1)

lk = wb.get('lynx')
termino = sys.argv[1]
url = 'http://lema.rae.es/drae/srv/search?val=' + urllib.quote_plus(termino)
lk.open(url)

