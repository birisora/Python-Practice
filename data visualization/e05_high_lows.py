import csv
# this allows to create a date format
from datetime import datetime

from matplotlib import pyplot as plt

# store filename of file we're working with then open it
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    # then pass file as arg to create reader object associated with file
    reader = csv.reader(f)
    # next() returns the next line in file, in this case only once for header
    header_row = next(reader)
    # print(header_row)

    # get high temperatures from file.
    # create an empty list
    # this is weird format? after adding in dates
    dates, highs = [], []
    # then loop through remaining rows in the file; continues where left off
    # On each pass through loop, append data from index 1, 2nd col, to highs
    for row in reader:
        # convert data contianing date info (row[0]) to a datetime obj
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        # now to convert strings to numbers with int() so matplotlib can read
        high = int(row[1])
        highs.append(high)

    print(highs)

    # To make easier to understand file header data, we print each
    # header and its position in the list
    # enumerate is used to get index of each item and value
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

# plot data
fig = plt.figure(dpi=128, figsize=(10,6))
# pass the list of highs and dates to plot()
plt.plot(dates, highs, c='red')

# Formal plot.
plt.title("Daily high temperatures, July 2014", fontsize=24)
# we would label the dates here.
plt.xlabel('', fontsize=16)
# draws the date labels diagonally to prevent overlapping
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

