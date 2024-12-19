import pytz
from datetime import datetime

date = datetime.now(pytz.timezone('Europe/Oslo'))

print(date)