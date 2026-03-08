from datetime import datetime

def get_days_from_today(date):
    return (datetime.today().date() - datetime.strptime(date, "%Y.%m.%d").date()).days

user_date = "2026.04.01"
print(get_days_from_today(user_date)) 