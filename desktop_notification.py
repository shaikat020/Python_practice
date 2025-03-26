import time
from plyer import notification

while True:
    notification.notify(
        title = "Reminder",
        message = "Time to take a break",
        timeout = 10
    )
    time.sleep(15*60) 