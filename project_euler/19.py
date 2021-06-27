# monday 1 jan 1900
week_day = 1
day = 1
month = 1
year = 1900
leap_year = False

ans = 0
while day != 31 or month != 12 or year != 2000:  # to 31 dec 2000
    # sunday first of the month
    if year >= 1901 and day == 1 and week_day == 7:  # century starts in 1901
        ans += 1

    day += 1
    week_day += 1
    if week_day > 7:
        week_day = 1

    if (day > 30 and month in [4, 6, 9, 11]) or \
       (day > 31 and month in [1, 3, 5, 7, 8, 10, 12]) or \
       (day > 28 and month == 2 and not leap_year) or \
       (day > 29 and month == 2 and leap_year):
       day = 1
       month += 1

    if month > 12:
        month = 1
        year += 1
        leap_year = (year % 4 == 0 and (year % 400 == 0 or year % 100 != 0))
    
print(ans)
