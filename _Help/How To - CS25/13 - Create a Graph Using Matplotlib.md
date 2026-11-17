# How To Create a Graph Using Matplotlib

### The basic parts

A line graph pairs each x value with a corresponding y value. Use days on the x-axis and population counts on the y-axis. Each list of counts must match the day list in length and order. Call plot() once per series. Use color and linestyle to distinguish lines. Use legend() to show their labels and show() to open the graph. In this project, graph the results after the Pygame loop finishes.

Install Matplotlib with pip install matplotlib. Give every series its own list. Each series needs one value for each day. The color and linestyle arguments control how the lines look. Use labels with legend() to identify them.

```python
import matplotlib.pyplot as plt

days = [1, 2, 3]
group_a = [12, 9, 7]
group_b = [3, 6, 8]

# Plot each count list against the same days.
plt.plot(days, group_a, color="blue", linestyle="-", label="Group A")
plt.plot(days, group_b, color="orange", linestyle="--", label="Group B")
plt.xlabel("Day")
plt.ylabel("Count")
# Match the lines to the labels supplied in plot().
plt.legend()
plt.show()
```

**Documentation:** [Installation](https://matplotlib.org/stable/install/) · [plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html) · [show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)
