
from datetime import datetime # To install : pip install DateTime
from playsound import playsound # To install : pip install playsound

# Lets print current Date and Time
now = datetime.now()
print("Current Time is : ",now.strftime("%H:%M:%S"))
alarm_time = input("Enter the time of alarm to be set:HH:MM:SS: ")
# We are slicing them to seperate hours minutes seconds and period from user input
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")


while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    playsound('alarm.mp3')
                    break


"""
Output : 
Current Time is :  19:41:49
Enter the time of alarm to be set:HH:MM:SS: 07 43 00 pm
Setting up alarm..
Wake Up!
<sound plays when time is matched >

"""