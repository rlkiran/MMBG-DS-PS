from datetime import datetime
import time
fmt = '%H:%M:%S'

first_time = datetime.now()
first_time = str(first_time.hour)+":"+str(first_time.minute)+":"+str(first_time.second)

time.sleep(5)
second_time = datetime.now()
second_time = str(second_time.hour)+":"+str(second_time.minute)+":"+str(second_time.second)
print(second_time)

tstamp1 = datetime.strptime(first_time, fmt)
tstamp2 = datetime.strptime(second_time, fmt)

td_mins = int(round(abs((tstamp1 - tstamp2).total_seconds()) / 60))
td_sec = int(abs((tstamp1 - tstamp2).total_seconds()))
print('The time difference is %s minutes' % td_mins,' and %s seconds' % td_sec)