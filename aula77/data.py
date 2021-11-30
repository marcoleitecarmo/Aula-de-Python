from datetime import datetime
from calendar import monthrange

ultimos = [monthrange(datetime.now().year, m)[1] for m in range(1, 13)]
print(ultimos) # [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]