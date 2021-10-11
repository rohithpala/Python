import psutil
from plyer import notification
import time

while True:
    battery = psutil.sensors_battery()
    if battery.percent <= 20:
        notification.notify(title="Battery Percentage ",
                            message=f'{battery.percent}% remaining. Connect to Charger',
                            timeout=10)
        time.sleep(600)

    elif battery.percent == 50:
        notification.notify(title="Battery Percentage ",
                            message='Half Charged',
                            timeout=10)
        time.sleep(3000)

    elif battery.percent == 100:
        notification.notify(title="Battery Percentage ",
                            message='Charged. Disconnect the Charger',
                            timeout=10)
        time.sleep(3000)

