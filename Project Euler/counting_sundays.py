from datetime import date

if __name__ == '__main__':
    sundays_count = 0

    for year in range(1901, 2001):
        for month in range(1, 13):
            if date(year, month, 1).weekday() == 6:
                sundays_count += 1

    print(sundays_count)