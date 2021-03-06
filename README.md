# TimesheetLogger
This is an app to log activity on your pc
To successfully read project numbers, create a file named: projectsList.csv
The first column should the be project number and the rest should be project synonyms

## Vision - Funtionality
* This app should work like this:
* you install it on you pc.
* it prompts you for a folder location where you want to save the outputs.
* once installed it starts logging the name of the open window your working on + a start-time, finish-time and duration.
* if you've got something open, but your not active on it, it should not log it.
* if you've not been active it should simply log "AFK"
* it should log the timestamp every 60 seconds
* (You should be able to view the logs, organise them as you want - assign them to a project and then export to .csv file.)
* it should save everyday.
* it should save a new .csv file everyday.
* the data being stored should look like this: filename; timestamp

## Actual MVP- Funtionality
* You run the exe file in linux (windows, currently still running a script)
* It automatically saves the .csv file where the exe file is saved.
* it logs the start / finish / duration times. It also logs the active window.
* you select the time interval you want to log.
* press start and it automatically starts logging.
* it saves a new csv everyday (if you've stopped it the day before, otherwise it just continues... must fix this)

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

## install tkinter for python 2.7
* sudo apt-get install python-tk
* `pyinstaller --onefile --windowed main.py`
* `pyinstaller --onedir --name=a_friendly_app_name_here   your_script.py`

## installing winpy32
# Windows to install win32gui
* website: https://stackoverflow.com/questions/20113456/installing-win32gui-python-module
* note - use 36 if you have python 3.6 etc.
* pip install C:\Users\Amvos\Downloads\pywin32-221-cp36-cp36m-win32.whl
* C:\Windows\py.exe C:\Users\Amvos\AppData\Local\Programs\Python\Python36-32\Scripts\pywin32_postinstall.py -install
