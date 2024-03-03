import salat
import datetime
import pytz
import tabulate

# Prayer time calculation setup
prayerTime = salat.PrayerTimes(salat.CalculationMethod.ISNA, salat.AsrMethod.STANDARD)

# Input and set calendar date
fullDate = input("Enter date as YYYY/MM/DD: \n")
dateArray = fullDate.split("/")
calendarDate = datetime.date(int(dateArray[0]), int(dateArray[1]), int(dateArray[2]))

# Columbus, OH direction measurements
longitude = -82.983330
latitude = 39.983334
zone = pytz.timezone('US/Eastern')

# Prayer time calculation
prayerTimes = prayerTime.calc_times(calendarDate, zone, longitude, latitude)

# Print in terminal table
table = [['Prayer', "Date", "Time"]]
for prayer, time in prayerTimes.items():
    dateFormat = time.strftime("%m/%d/%Y,")
    timeFormat = time.strftime("%I:%M:%S %p %Z")
    table.append([prayer.title(), dateFormat, timeFormat])

# Result
print(tabulate.tabulate(table, headers='firstrow'))

