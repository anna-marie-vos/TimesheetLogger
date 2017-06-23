import sys

def activeLinuxWindow():
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
            return active_window.get_name()

def activeWindowsWindow():
    # http://stackoverflow.com/a/608814/562769
    import win32gui
    window = win32gui.GetForegroundWindow()
    active_window_name = win32gui.GetWindowText(window)
    return active_window_name
