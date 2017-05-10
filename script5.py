#!/usr/bin/env python
import sys
import time
import wnck
import pygtk
import gtk

actual_platform = sys.platform
screen = wnck.screen_get_default()

# screen.force_update()

print(actual_platform)
print(screen)

pygtk.require('2.0')

print(pygtk)

while gtk.events_pending():
    gtk.main_iteration()

windows = screen.get_windows()
print (windows)
