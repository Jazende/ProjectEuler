from datetime import date
count = 0
for month in range(1,13):
    for year in range(1901, 2001):
        try:
            if date(year, month, 1).weekday() == 6:
                count += 1
        except ValueError as e:
            pass
print(count)
