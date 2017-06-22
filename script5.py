#!/usr/bin/env python
import sys
import time
import wnck
import pygtk
import gtk

actual_platform = sys.platform
screen = wnck.screen_get_default()

# screen.force_update()
activeWindow = screen.get_previously_active_window()

print('actual platform',actual_platform)
print('screen',screen)
print('activeWindow',activeWindow)

# pygtk.require('2.0')
#
# print(pygtk)
#
while gtk.events_pending():
    gtk.main_iteration()
#
# windows = screen.get_windows()
# print (windows)
