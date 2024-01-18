import datetime

print(datetime.date.today())

# Output: 2018-07-31 (or whatever date is today)
from datetime import timedelta 
'''La clase timedelta se utiliza para representar la diferencia entre dos objetos de fecha o tiempo. 
Permite realizar operaciones aritméticas con fechas y tiempos.'''

def add_days(start, days):
    """Adds a number of days to the start date and returns the resulting date"""
    return start + timedelta(days=days)
print(add_days(datetime.date.today(), 5)) # Add 5


