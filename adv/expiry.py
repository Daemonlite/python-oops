import datetime
from dateutil.relativedelta import relativedelta
import arrow
    
class ExpirationChecker:
    def __init__(self,month,year):
        self.month = month
        self.year = year
    
    
    def check_expiration(self):
        current_date = datetime.datetime.now().date()
        six_months_from_now = current_date + relativedelta(months=6)
        three_months_from_now = current_date + relativedelta(months=3)
        
       
        expiry_date = datetime.datetime(self.year,self.month, 1)
        
        if current_date <= expiry_date.date() <= six_months_from_now:
            arr = arrow.get(expiry_date).humanize()
            print(f"Item expiring : {arr}")
        
        if current_date <= expiry_date.date() <= three_months_from_now:
            print(f"Item expiring: {arr}")
        
        if current_date > expiry_date.date():
            print(f"Item expired: {arr}")
    

checker = ExpirationChecker(3, 2024)
exp = checker.check_expiration()
