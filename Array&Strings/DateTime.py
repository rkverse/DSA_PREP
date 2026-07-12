from datetime import datetime

time = "07:30 PM"

converted = datetime.strptime(time, "%I:%M %p")
print(converted.strftime("%H:%M"))