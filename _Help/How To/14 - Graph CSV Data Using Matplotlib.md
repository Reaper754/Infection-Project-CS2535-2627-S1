# How To Graph CSV Data Using Matplotlib

### The basic parts

`csv.DictReader` reads a CSV row as a dictionary. The header row supplies its keys. CSV values are read as strings. Convert day numbers and counts to integers before plotting them.

Each status needs a list of counts. Each list must match the day list in length and order. Additional columns can store trial settings without being plotted. The column names in your code must match the CSV's headers.

A **figure** is the graph window. **Axes** are the plotting area inside it. `plt.subplots()` creates both. Creating a new figure for each graph keeps previous trials from appearing on the same axes accidentally.

### Example: graph a recorded trial

This separate script expects a CSV called `trial.csv`. Its headers include `day`, `susceptible`, `infected`, `recovered`, and `dead`. Each later row represents one completed day. `csv_path` can instead hold a file selected through your terminal menu. The same plotting code can run after the Pygame loop ends to display the completed trial. `plt.show()` normally waits until the graph window closes.

```python
import csv
import matplotlib.pyplot as plt

csv_path = "trial.csv"
days = []
counts = {"susceptible": [], "infected": [], "recovered": [], "dead": []}
colours = {"susceptible": "tab:blue", "infected": "tab:red",
           "recovered": "tab:green", "dead": "tab:gray"}

with open(csv_path, newline="", encoding="utf-8") as csv_file:
    for row in csv.DictReader(csv_file):
        days.append(int(row["day"]))
        for status in counts:
            counts[status].append(int(row[status]))

# Plot every status on the same axes with its own colour and label.
figure, axes = plt.subplots()
for status, values in counts.items():
    axes.plot(days, values, color=colours[status], label=status.capitalize())

axes.set(title="Simulation Results", xlabel="Simulation day", ylabel="People")
axes.legend()
axes.grid(True)
figure.tight_layout()
plt.show()
```

**Documentation:** [CSV dictionaries](https://docs.python.org/3/library/csv.html#csv.DictReader) · [subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html) · [Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
