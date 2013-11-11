# Generates a uuid and copies it to the windows clipboard.

from Tkinter import Tk
import uuid

ui = str(uuid.uuid4())
lui = ui.split('-')[4]

r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(lui)
r.destroy()
print lui
