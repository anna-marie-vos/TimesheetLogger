
#!/usr/bin/env python
import sys
import time

def get_active_window_in_linux():
    import wnck
    import gtk
    screen = wnck.screen_get_default()

    while gtk.events_pending():
        gtk.main_iteration()

    windows = screen.get_windows()
    active_window = screen.get_active_window()
    active_app = screen.get_active_window().get_application()

    for w in windows:
        if w.get_application() == active_app:
            print('active window name', active_window.get_name())
            return active_window.get_name()

def get_active_window_in_windows():
    # http://stackoverflow.com/a/608814/562769
    import win32gui
    window = win32gui.GetForegroundWindow()
    active_window_name = win32gui.GetWindowText(window)
    return active_window_name

while True:
    if sys.platform in ['linux', 'linux2']:
        get_active_window_in_linux()

    elif sys.platform in ['Windows', 'win32', 'cygwin']:
        get_active_window_in_windows()
    time.sleep(5)
