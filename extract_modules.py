import gi
gi.require_version("Gimp", "3.0")
gi.require_version("GimpUi", "3.0")
gi.require_version("Gtk", "3.0")

# The generator3 module can be downloaded from this repository:
# https://github.com/JetBrains/intellij-community/tree/master/python/helpers/generator3

import sys
from generator3.module_redeclarator import ModuleRedeclarator

def stub(module_name):
    mod = sys.modules.get(module_name)
    r = ModuleRedeclarator(mod, module_name, None, cache_dir='c:\\Temp\\output\\', doing_builtins=False)
    r.redo(module_name, True)
    r.flush()
    
stub('gi.repository.GLib')
stub('gi.repository.Gimp')
stub('gi.repository.GimpUi')
stub('gi.repository.Gtk')
stub('gi.repository.Gdk')
stub('gi.repository.GdkPixbuf')
stub('gi.repository.GExiv2')
stub('gi.repository.Gio')
stub('gi.repository.GObject')
stub('gi.repository.Pango')
stub('gi.repository.Gegl')
stub('gi.repository.freetype2')
stub('gi.repository.cairo')
stub('gi.repository.Babl')
stub('gi.repository.GModule')
stub('gi.repository.fontconfig')
stub('gi.repository.Atk')


