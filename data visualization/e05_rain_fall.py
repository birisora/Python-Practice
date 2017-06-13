import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_rainfall_2015.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rainfalls = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rainfall = float(row[19])
        except ValueError:
            print(current_date, 'missing data here')
        else: 
            dates.append(current_date)
            rainfalls.append(rainfall)

# Plot data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, rainfalls, c='green', alpha=0.5)
plt.fill_between(dates, rainfalls, facecolor='blue', alpha=0.2)

title = "Daily rainfall 2015 Sitka, AK"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()