from datetime import datetime

def get_days_from_today(date):
    try:
        return (datetime.today().date() - datetime.strptime(date, "%Y-%m-%d").date()).days
    except ValueError:
        return 'time data does not match right format' 


user_date = "2016-04-03"
print(get_days_from_today(user_date)) 