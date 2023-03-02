import datetime
import time
# creating an alarm app
print("Welcome to the alarm app")
time_for_alarm = input("Enter The time you wanna stop the alarm: ")
reason = input("Reason for the timer: ")
time_for_alarm_as_list = time_for_alarm.split(":")
# waiting until its that time
not_yet_time = True
while not_yet_time:
    # check the time now
    time_now = datetime.datetime.now()
    hour = time_now.strftime("%H")
    minute = time_now.strftime("%M")
    if hour == time_for_alarm_as_list[0] and minute == time_for_alarm_as_list[1]:
        # stop the waiting
        not_yet_time = False
        print(f"Its time for \"{reason}\"")
    # waiting one minute before the repeat of the while loop
    time.sleep(1)