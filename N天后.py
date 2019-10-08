from datetime import date, datetime, timedelta
print(datetime)
day = date.today()
day1 = datetime.today()
print(day)
print(day1)
now = datetime.now()
now1 = date.weekday(now)

print(now)
print(now1)
delta = timedelta(days=10)
a = timedelta()
print(timedelta)
print(delta)
print(delta.__str__())
print(a)
n_days_after = now + delta
n_days_after1 = day + delta
print(type(n_days_after))
print(type(n_days_after1))
print(n_days_after)
print(n_days_after1)

n_days_forward = now - delta
print("向后推迟5天的日期：{}".format(n_days_after.strftime('%Y%m%d%A')))
print("向前推5天的日期：{}".format(n_days_forward.strftime('%Y-%m-%d')))