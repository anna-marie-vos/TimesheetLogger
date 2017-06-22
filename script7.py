import sys
import time
import wnck
import pygtk
import gtk
# from gi.require_version('Gtk', '3.0').repository import Gtk, Wnck

def get_active_window():
    # gtk.init([])  # necessary if not using a Gtk.main() loop
    screen = wnck.screen_get_default()
    screen.force_update()  # recommended per Wnck documentation

    window_list = screen.get_windows()
    active_window = screen.get_active_window()

    if active_window is not None:
        pid = active_window.get_pid()
        with open("/proc/{pid}/cmdline".format(pid=pid)) as f:
            active_window_name = f.read()
            print(active_window_name)

    print('window list',window_list)
    print('activeWindoq',active_window)

while True:
    print("Active window: %s" % str(get_active_window()))
    time.sleep(5)
