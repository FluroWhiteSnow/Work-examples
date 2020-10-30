import csv
from datetime import datetime
import matplotlib.pyplot as plt 

filename = 'Data/melbourne_weather.csv'

with open(filename) as f:
	reader = csv.reader(f)
	averages = []
	for i, l in enumerate(reader):
		if i==12:
			try:
				for v in l[1:14]:
					averages.append(float(v))	
			except IndexError:
				pass

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(averages)

ax.set_title("Melbourne Average temps 1855-2015", fontsize=24)
ax.set_xlabel("Months", fontsize=16)
ax.set_ylabel("Temps (c)", fontsize =16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()