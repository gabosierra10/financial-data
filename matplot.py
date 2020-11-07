import csv
from matplotlib import pyplot as plt

#Open file
file = open('fdata.csv')

#Initialize table columns
dates = []
financial_open = []
high = []
low = []
financial_close = []

#Read the data in the file
reader = csv.reader(file)
for row in reader:
    dates.append(row[0])
    financial_open.append(float(row[1]))
    high.append(float(row[2]))
    low.append(float(row[3]))
    financial_close.append(float(row[4]))

#Obtain month
month_string = 'JanFebMarAprMayJunJulAugSepOctNovDec'
month = []
for element in dates:
    month.append(int(element[0:2]))

#Replace numerical month values for string abbreviation.
for x in range(len(month)):
    month[x] = month_string[3 * month[x] - 3:3 * month[x]]

#Modify dates in order to make abundantly clear the exact date.
for x in range(len(dates)):
    dates[x] = dates[x][3:5]+'\n'+month[x]+'\n20'+dates[x][6:8]

#Begin plotting with the dates as our x axis.
plt.plot(dates, financial_open, label = 'Open')
plt.plot(dates, financial_close, label = 'Close')
plt.plot(dates, high, label = 'High')
plt.plot(dates, low, label = 'Low')

#Set Title
plt.title('Stock Values for Hypothetical Company')

#Style
plt.style.use('dark_background')

#Set necessary labels
plt.ylabel('Stock Price in USD')

#Set grid
plt.grid(True)

#Set legend
plt.legend()

#Display
plt.show()

