# Recommended Development Process

To help you complete this project, the development process has been broken down into 12 smaller, manageable steps. These steps are not the only way to succeed in this project, but they are the steps I would personally follow for a project like this.

Each step focuses on a specific part of the program, allowing you to build and test your work as you go. Follow these steps in order to gradually develop your program into a complete, working project.

**Be sure to continuously test as you work through these development steps.**

1. Identify what data you will need from users to start the simulation (what parameters should a user be able to control in the simulation).
2. Set up the terminal menu as the first thing the user interacts with when the program starts. Include options to start a new simulation or view previous data, along with resuming or rerunning a saved simulation and exiting the program.
3. Identify what kinds of data each simulated person will need to keep track of.
4. Create dictionary template for people.
5. Generate a population based on the people dictionary template.
6. Create a window that displays the simulation using Pygame (people can be circles or squares for simplicity).
7. Have people move around in the simulation.
8. Detect proximity between people in simulation.
9. Display people in different states as different colors (infected, susceptible, recovered, dead).
10. Set up a saving system for the game (JSON).
11. Set up a way to record data from one run of the simulation (CSV).
12. Allow a user to view a graph displaying the different values for each group of the population for previously run simulations.