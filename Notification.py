# Simple program to send notification, it keeps sending notification until you stop the program


import time
from plyer import notification


def send_notif(title, message, sending_period_in_secs):
    while True:
        notification.notify(title=title, message=message, timeout=10)
        time.sleep(sending_period_in_secs)


send_notif("Reminder", "Send the E-Mail", 3600)
