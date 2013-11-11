# Generates an uuid and copies it to the linux clipboard

import pygtk
pygtk.require('2.0')
import gtk
import uuid

ui = str(uuid.uuid4())
uid = ui.split('-')[4]
 
cb = gtk.clipboard_get()
cb.set_text(uid)
cb.store()
print uid 
