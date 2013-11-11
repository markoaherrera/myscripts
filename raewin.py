import urllib2

#termino = droid.dialogGetInput('Buscar', 'Ingrese palabra').result

if termino is not None and len(termino) > 0:
    searchUrl = 'http://lema.rae.es/drae/srv/search?val=' + termino
    response = urllib2.urlopen(searchUrl)
    html = response.read()
    raeFileName = './raewin.html'
    fhtml = open(raeFileName, w)
    fhtml.write(html)
    fhtml.close()
#	droid.webViewShow(searchUrl)

else:
#	droid.makeToast('Cancelado')
