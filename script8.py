
#!/usr/bin/env python
import time
import wnck
import gtk

def get_active_window():
    screen = wnck.screen_get_default()

    while gtk.events_pending():
        gtk.main_iteration()

    windows = screen.get_windows()
    active_window = screen.get_active_window()
    active_app = screen.get_active_window().get_application()


    for w in windows:
        if w.get_application() == active_app:
            print('active window name', active_window.get_name())
            pid = active_app.get_pid()
            # print('active app',pid)
            with open("/proc/{pid}/cmdline".format(pid=pid)) as f:
                active_app_window_name = f.read()
                # print('activeAppName',active_app_window_name)
            # w.minimize()

while True:
    get_active_window()
    time.sleep(5)
