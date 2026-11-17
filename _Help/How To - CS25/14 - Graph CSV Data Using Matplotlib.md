# How To Graph CSV Data Using Matplotlib

### The basic parts

A CSV stores rows of values separated by commas. The first row names the columns. DictReader lets you look up values by those column names. The values start as strings, so convert the day and count to integers. Append them in the same loop to keep the lists aligned. For a trial with several count columns, build one list for each column and plot each against the same days.

Save this sample as data.csv beside your Python script. Run the script with that folder as the working directory. DictReader uses the header row as column names. Convert the values to integers before plotting.

```csv
day,count
1,4
2,7
3,5
```

```python
import csv
import matplotlib.pyplot as plt

days = []
counts = []
# Open the sample using the column names from its header.
with open("data.csv", newline="", encoding="utf-8") as file:
    # Convert both values before adding them to the graph data.
    for row in csv.DictReader(file):
        days.append(int(row["day"]))
        counts.append(int(row["count"]))

plt.plot(days, counts)
plt.xlabel("Day")
plt.ylabel("Count")
plt.show()
```

**Documentation:** [CSV dictionaries](https://docs.python.org/3/library/csv.html#csv.DictReader) · [plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
