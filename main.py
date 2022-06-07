from datetime import datetime, timedelta





t = timedelta(days = 280)
date_dict ={
'day': int(input('enter date: ')),
'month': int(input('enter month: ')),
'year': int(input('enter year: '))
}


date = datetime(day= date_dict['day'], month = date_dict['month'], year= date_dict['year'])


born_day = date + t

print(born_day.strftime("%d/%m/%Y"))
