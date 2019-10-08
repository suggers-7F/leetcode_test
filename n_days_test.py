import arrow
#计算一个时间N天后/前的日期(N可以为负数即N天前)
def date_n_day(str_day,n):
    day = arrow.get(str_day,"YYYYMMDD")
    finall_day = day.shift(days=n)
    return finall_day.strftime("%Y%m%d")

#计算一个时间N个月后/前的日期(N可以为负数即N天前)
def date_n_mon(str_day,n):
    day = arrow.get(str_day, "YYYYMMDD")
    finall_day = day.shift(months=n)
    return finall_day.strftime("%Y%m%d")

#计算一个时间N个月后/前最后一天日期(N可以为负数即N天前)
import calendar
def date_n_mon_lastday(str_day,n):
    date = arrow.get(str_day,"YYYYMMDD")
    finall_day = date.shift(months=n)
    year = finall_day.year
    mon = finall_day.month
    #获取某年某月总共有多少天
    mon_days = calendar.monthrange(year,mon)[1]
    finall_day_end = finall_day.strftime("%Y%m%d")[0:6] + str(mon_days)
    return finall_day_end


if __name__ == '__main__':
    # 日期，N天，N月
    str_day,n_day,n_mon = "20190322",0,-1
    print(date_n_day(str_day,n_day))
    print(date_n_mon(str_day,n_mon))
    print(date_n_mon_lastday(str_day,n_mon))