from datetime import datetime, timedelta





t = timedelta(days = 280)
h = timedelta(days = 203)
date_dict ={
'day': int(input('enter date: ')),
'month': int(input('enter month: ')),
'year': int(input('enter year: '))
}


date = datetime(day= date_dict['day'], month = date_dict['month'], year= date_dict['year'])





born_day = date + t
hospitality_date = date + h 
print("date of born\t" + born_day.strftime("%d/%m/%Y") + "\ndate of dicret\t" + hospitality_date.strftime("%d/%m/%Y"))



