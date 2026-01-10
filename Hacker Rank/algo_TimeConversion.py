from datetime import datetime

def timeConversion(s):
    # Write your code here
    time_12_hour = datetime.strptime(s,'%I:%M:%S%p')
    time_24_hour = time_12_hour.strftime('%H:%M:%S')
    return time_24_hour