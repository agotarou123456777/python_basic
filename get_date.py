import datetime

dt = datetime.datetime.now()
s = dt.strftime("%Y-%m-%d_%H:%M:%S")
print(s)

dt = datetime.datetime.now()
s = dt.strftime("%Y%m%d")
print(s)