import pywhatkit as pwk
import datetime

time = datetime.datetime.now()
hour = time.hour
minute = time.minute

number = str("+" + input("Please enter recipient's number: "))
print(number)
message = str(input("Message: "))

pwk.sendwhatmsg(number, message, wait_time= 3, time_hour= hour, time_min= minute)
