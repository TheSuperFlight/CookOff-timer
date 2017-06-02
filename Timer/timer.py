#Timer script voor de Cook-off 2017, dit is een timer die in 60 minuten naar 0 loopt. te onderbreken met ctrl c.
import time
import sys

time_start = time.time()
seconds = 5
#raw_input("Please enter the amount of seconds: ")
minutes = 1
#raw_input("Please enter the amount of minutes: ")
hours = 0
#raw_input("please enter the amount of hours: ")

print "%s : %s : %s" % (hours, minutes, seconds)

time_left = (hours * 3600) + (minutes * 60) + seconds

while time_left > 0:
    try:
        time_left = int (time_left) - 1
        if seconds > 0:
            seconds = seconds - 1
            time.sleep(1)
            print ("%s : %s : %s") % (hours, minutes, seconds)
        elif minutes > 0:
            minutes = minutes - 1
            seconds = 59
            print ("%s : %s : %s") % (hours, minutes, seconds)
        elif hours > 0:
            hours = hours - 1
            minutes = 59
            seconds = 59
            print ("%s : %s : %s") % (hours, minutes, seconds)
    except KeyboardInterrupt, e:
        print ("Timer Stopped by user!")
print("Timer Finished")
