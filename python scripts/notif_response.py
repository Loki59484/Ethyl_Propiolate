import pygetwindow as gw
from pywinauto import Application 
import re,time
print("Notification automation initiated...")
while True:
    try:
        windows = gw.getAllTitles()
        for title in windows:
            if re.match(r"Gaussian.*", title) and title != "Gaussian 09 Revision-D.01-SMP":
                notif = title
        app = Application().connect(title = notif)
        dlg = app.window(title = notif)
        des = dlg.descendants()

        for item in des:
            if "Yes" in item.window_text():
                dlg.set_focus()
                item.click_input()

    except:
        pass
    time.sleep(15)