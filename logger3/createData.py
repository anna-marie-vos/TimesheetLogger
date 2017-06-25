import sys

def activeLinuxWindow():
    import gi
    gi.require_version('Wnck', '3.0')
    from gi.repository import Wnck as wnck
    from gi.repository import Gtk as gtk
    screen = wnck.Screen.get_default()

    while gtk.events_pending():
        gtk.main_iteration()

    windows = screen.get_windows()
    active_window = screen.get_active_window()
    active_app = screen.get_active_window().get_application()

    for w in windows:
        if w.get_application() == active_app:
            name = active_window.get_name()
            return name

# def activeWindowsWindow():
#     # http://stackoverflow.com/a/608814/562769
#     import win32gui
#     window = win32gui.GetForegroundWindow()
#     active_window_name = win32gui.GetWindowText(window)
#     return active_window_name

activeLinuxWindow()
