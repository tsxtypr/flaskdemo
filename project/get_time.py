import datetime
import calendar

class GetDate(object):
    def __init__(self):
        self.date_list=[]
    def deal_date(self):
        day = datetime.datetime.now()
        year = day.year
        month = day.month
        days = calendar.monthrange(year, month)[1]
        week = datetime.date(year, month, 1).weekday() + 1

        # 将所有天放在一个列表中
        alldays_list = []
        for day in range(1, days + 1):
            alldays_list.append(day)

        line = []
        # 获得第一行
        for i in range(1, week):
            line.append("empty")
        for j in range(7 - week + 1):
            line.append(alldays_list.pop(0))
        self.date_list.append(line)
        # print(result)

        # 获得剩下行：
        for one in range(len(alldays_list) // 7):
            line = []
            for day in range(7):
                line.append(alldays_list.pop(0))
            self.date_list.append(line)

        # 获得最后一行
        line = []
        for k in alldays_list:
            line.append(alldays_list.pop(0))
        for other in range(7 - len(line)):
            line.append("empty")
        self.date_list.append(line)

        return self.date_list
    def print_date(self):
        return self.deal_date()

