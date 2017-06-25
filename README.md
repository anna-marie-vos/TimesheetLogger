# TimesheetLogger
This is an app to log activity on your pc

## Funtionality
* This app should work like this:
* you install it on you pc.
* it prompts you for a folder location where you want to save the outputs.
* once installed it starts logging the name of the file your working on and a timestamp.
* if you've got something open, but your not active on it, it should not log it.
* if you've not been active it should simply log "AFK"
* it should log the timestamp every 5 seconds
* it should write it to a .csv file.
* it should save everyday.
* it should save a new .csv file everyday.
* the data being stored should look like this: filename; timestamp
* if nothing's logged: AFK; timestamp

### Learning
* sudo apt-get install python-wnck
* install psutil to crossplatform data: sudo pip3 install psutil
* install pynput to monitor control mouse and keyboard
* terminal commands that show the current files memories being used:
* top
* ps
* ps aux
* /proc/[pid]/cwd
* This is a symbolic link to the current working directory of the process.
* To find out the current working directory of process 20, for instance, you can do this:
* $ cd /proc/20/cwd; /bin/pwd
* Note that the pwd command is often a shell built-in, and might not work properly.  
* In bash(1), you may use pwd -P.
* In a multithreaded process, the contents of this symbolic link are not available if the main thread has already terminated (typically by calling pthread_exit(3)).
* Permission to dereference or read (readlink(2)) this symbolic link is governed by a ptrace access mode PTRACE_MODE_READ_FSCREDS check; see ptrace(2).
### Related articles
* http://stackoverflow.com/questions/115868/how-do-i-get-the-title-of-the-current-active-window-using-c
* http://stackoverflow.com/questions/608809/getting-the-name-of-the-active-window
* https://superuser.com/questions/382616/detecting-currently-active-window
* http://stackoverflow.com/questions/10266281/obtain-active-window-using-python
* https://developer.gnome.org/libwnck/stable/WnckWindow.html

## Selenium is another webwindow library
* https://stackoverflow.com/questions/10629815/handle-multiple-window-in-python
* https://stackoverflow.com/questions/4746688/detecting-active-windows-in-python-with-kde
* https://stackoverflow.com/questions/38529064/how-can-i-bring-a-window-to-the-foreground-using-win32gui-in-python-even-if-the
* https://stackoverflow.com/questions/35684815/how-to-get-application-name-and-version-relating-to-the-foreground-window-in-pyt
* https://lazka.github.io/pgi-docs/Wnck-3.0/classes/Screen.html
* install: `sudo apt-get install libwnck-3-* gir1.2-wnck-3.0`

# this worked:
* https://gist.github.com/nthrnth/f77465b56fb21dbd3698ea493822dab7
* https://unix.stackexchange.com/questions/159334/focusing-the-current-window-minimizing-all-of-the-others

## creating exe
* http://python-guide-pt-br.readthedocs.io/en/latest/shipping/freezing/
* pyinstaller does not work on windows 8 or windows 10. 
