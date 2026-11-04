# How To Create a Graph Using Matplotlib

Matplotlib is a Python library for graphs. Install it in your project's terminal:

```sh
pip install matplotlib
```

### The basic parts

A **line graph** shows how values change over time. The horizontal **x-axis** holds time values. The vertical **y-axis** holds the measured values. Each point pairs one time with one measurement.

Each data series represents one group, such as infected people. Its list must have the same length as the time list. Values at the same index belong together. Calling `plot()` again adds another series to the same graph. A **legend** identifies each series by its label. Markers show the individual data points.

### Example: compare groups over several days

This is a separate Python script rather than a `run_sim` example. The lists represent recorded results from a simulation. Replace them with your own results. In Pygame, collect results during the simulation and show the graph after the main loop ends. `plt.show()` normally waits for the graph window to close.

```python
import matplotlib.pyplot as plt

days = [0, 1, 2, 3, 4]
susceptible = [99, 94, 82, 65, 50]
infected = [1, 6, 15, 25, 30]
recovered = [0, 0, 3, 10, 20]

# Each call adds one labelled series to the graph.
plt.plot(days, susceptible, marker="o", label="Susceptible")
plt.plot(days, infected, marker="o", label="Infected")
plt.plot(days, recovered, marker="o", label="Recovered")

plt.title("Disease Spread Over Time")
plt.xlabel("Simulation day")
plt.ylabel("Number of people")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

**Documentation:** [Installation](https://matplotlib.org/stable/install/) · [plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html) · [show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)
