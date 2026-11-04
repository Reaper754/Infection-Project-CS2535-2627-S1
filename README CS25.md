# Infection! (CS25 Edition)

Create a visual simulation of an infection spreading through a population. Users will choose the population and disease settings before each trial. Your program will display people moving through a Pygame window as their infection status changes. It will track the results over simulation days and display those results on a graph.

When the program starts, the user first interacts with a terminal menu. This menu lets them start a new simulation or view previous simulation data. It also provides the options to resume or rerun a saved simulation and exit the program. The Pygame simulation window opens when the user chooses to start, resume, or rerun a simulation.

This project combines functions, modules, lists, dictionaries, and file handling. Build it in manageable stages. Start with the terminal menu and population data. Then add movement, infection rules, saving, and graphing. Test each feature as you add it. The [recommended development process](development_process.md) provides a suggested order, and the [How To references](_Help/How%20To) explain useful library features.

## Project Requirements Checklist

### Main Menu (Terminal)

* [ ] The program displays the terminal menu as its first user interaction, before opening a Pygame simulation window.
* [ ] The terminal menu includes an option to run a new simulation.
* [ ] The terminal menu includes an option to view previous simulation data.
* [ ] Selecting previous simulation data displays an indexed list of saved trials.
* [ ] The user can select a trial from that list to view its data on a graph.
* [ ] The terminal menu includes an option to select a saved simulation and resume it from its JSON save.
* [ ] The terminal menu includes an option to rerun a saved simulation from the beginning using its saved starting input values.
* [ ] The terminal menu includes an option to exit the program.

### Pre-Simulation User Inputs

* [ ] The user can enter a population count as an integer.
* [ ] The user can enter infectiousness as a percentage chance of infection.
* [ ] The user can enter transmissibility as the distance infection can travel in pixels.
* [ ] The user can enter lethality as the percentage chance that an infected person dies on a given day.
* [ ] The user can enter recoverability as the percentage chance that an infected person recovers on a given day.
* [ ] The user can enter immunity as the percentage of the population that is immune.
* [ ] The user can enter immunity efficacy as the percentage chance that immunity prevents infection.
* [ ] The user can enter a disease name as a string that uniquely identifies the trial.

### Population and Disease Behaviour

* [ ] The population is stored as a list of dictionaries.
* [ ] Each person's dictionary stores an x position, y position, x speed, and y speed.
* [ ] Each person's dictionary stores a status: infected, recovered, susceptible, or dead.
* [ ] Each person's dictionary stores an immune value as `True` or `False`.
* [ ] The population size matches the user's population count.
* [ ] The starting immune population is determined by the user's immunity percentage.
* [ ] Infection checks use the user's transmissibility distance and infectiousness percentage.
* [ ] Infection checks for immune people use the user's immunity efficacy percentage.
* [ ] Daily death checks for infected people use the user's lethality percentage.
* [ ] Daily recovery checks for infected people use the user's recoverability percentage.

### Simulation Visualization and Controls

* [ ] People are displayed visually in a Pygame window.
* [ ] People start at randomly selected positions.
* [ ] People move in randomly selected directions rather than all moving in the same direction.
* [ ] Dead people do not move.
* [ ] Infected, recovered, susceptible, and dead people each have a different display colour.
* [ ] The population count for each status remains visible on screen during the simulation.
* [ ] The simulation day count remains visible on screen during the simulation.
* [ ] Pressing `s` saves the simulation's state and input settings to a JSON file.
* [ ] The JSON save includes the filename or path of the CSV currently recording the simulation's data.
* [ ] Resuming a simulation restores its saved population state, simulation time, and input settings.
* [ ] Resuming a simulation uses the CSV identified in its JSON save for subsequent daily records.
* [ ] Pressing `q` quits the simulation.
* [ ] Pressing Space pauses and unpauses the simulation.
* [ ] Pressing `f` toggles fast-forward mode on and off.
* [ ] The simulation ends automatically when there are no more infected people.

### Recorded Data and Graphs

* [ ] At the end of every simulation day, a new row containing the day number and counts of infected, recovered, susceptible, and dead people is appended to the active CSV file.
* [ ] Daily CSV recording happens automatically without requiring the user to press `s`.
* [ ] Appending daily records preserves the existing rows in the CSV file.
* [ ] The CSV file also records the trial's starting input values.
* [ ] Each new simulation run, including a rerun of a saved simulation, creates a uniquely named CSV file without overwriting an existing run's file.
* [ ] A graph of the simulation's recorded data is displayed automatically when the simulation ends.
* [ ] The graph's x-axis shows time in simulation days.
* [ ] The graph's y-axis shows population counts.
* [ ] The graph includes separate series for infected, recovered, susceptible, and dead people.
* [ ] Each status series uses a different colour.

## CSE 2110 - Procedural Programming 1

| Outcome | Excellent | Proficient | Developing | Emerging |
| --- | --- | --- | --- | --- |
| Focus on Functions | Functions divide the program into clear tasks, use parameters and return values deliberately, and minimize repeated code throughout the simulation. | Functions organize the simulation into manageable tasks and use appropriate parameters and return values. | Functions organize some tasks, but responsibilities, parameters, return values, or repeated code need improvement. | Functions are missing, rarely used, or do not effectively organize the simulation. |
| Distinct Modules | Modules group related tasks with clear responsibilities and deliberate connections that make the program easy to follow and maintain. | The program uses distinct modules to organize related tasks, with imports that allow the modules to work together. | The program uses multiple modules, but their responsibilities overlap or their connections are unclear or inconsistent. | The program is not divided into distinct modules, or module organization prevents parts of the program from working together. |
| Python Best Practices and Documentation | Code consistently follows Python best practices and is exceptionally clear and maintainable. Type hints, docstrings, naming, formatting, and other documentation are accurate and useful throughout. | Code follows appropriate Python best practices. Functions use appropriate type hints and docstrings, and names and comments make the program easy to understand. | Code follows some Python conventions and includes some useful documentation, but documentation, type hints, docstrings, or naming may be inconsistent. | Code frequently does not follow Python conventions and has little or missing documentation. Type hints and/or docstrings are missing from functions. |
| Project Requirements | All project requirements are successfully implemented, with features developed beyond the minimum requirements in ways that meaningfully improve the simulation. | All requirements outlined in the project description are successfully implemented. | Most project requirements are present, but one or more requirements are incomplete or implemented inconsistently. | Several major requirements from the project description are missing or incomplete. |

## CSE 2120 - Data Structures 1

| Outcome | Excellent | Proficient | Developing | Emerging |
| --- | --- | --- | --- | --- |
| Use of Lists | Lists are used deliberately to manage the population and related collections, with clear and efficient access, iteration, and updates. | Lists store and manage the population appropriately, with correct access, iteration, and updates. | Lists store population data, but access, iteration, or updates are sometimes incorrect or unnecessarily repetitive. | Lists are missing or are used incorrectly, preventing effective management of the population. |
| Use of Dictionaries | Dictionaries consistently represent each person with clear keys and appropriate values, and support reliable access and updates throughout the simulation. | Dictionaries store each person's required information and are accessed and updated correctly. | Dictionaries store some person information, but keys, values, access, or updates are incomplete or inconsistent. | Dictionaries are missing or are used incorrectly, preventing effective tracking of each person. |
| Python Best Practices and Documentation | Code consistently follows Python best practices and is exceptionally clear and maintainable. Type hints, docstrings, naming, formatting, and other documentation are accurate and useful throughout. | Code follows appropriate Python best practices. Functions use appropriate type hints and docstrings, and names and comments make the program easy to understand. | Code follows some Python conventions and includes some useful documentation, but documentation, type hints, docstrings, or naming may be inconsistent. | Code frequently does not follow Python conventions and has little or missing documentation. Type hints and/or docstrings are missing from functions. |
| Project Requirements | All project requirements are successfully implemented, with features developed beyond the minimum requirements in ways that meaningfully improve the simulation. | All requirements outlined in the project description are successfully implemented. | Most project requirements are present, but one or more requirements are incomplete or implemented inconsistently. | Several major requirements from the project description are missing or incomplete. |

## CSE 2130 - Files and File Structures 1

| Outcome | Excellent | Proficient | Developing | Emerging |
| --- | --- | --- | --- | --- |
| Use of CSV Files | CSV records are consistently organized and accurately preserve settings and daily counts across new, resumed, and repeated runs, supporting reliable graphing without overwriting previous results. | CSV files append daily counts automatically, preserve trial settings, and can be read for graphing. Resumed runs use the recorded CSV, and new runs use unique files. | CSV files record some trial data, but daily appending, file selection, preservation of previous results, or reading for graphing is inconsistent. | CSV files are missing or file operations do not successfully record and retrieve trial data. |
| Use of JSON Files | JSON saves consistently preserve state, time, settings, and the active CSV reference in a clear structure that supports reliable resuming and rerunning. | Pressing `s` saves simulation state, time, input settings, and the active CSV reference. Saved data supports resuming a run and rerunning its starting settings. | JSON saves are present, but saved information, resuming, or rerunning is incomplete or inconsistent. | JSON saves are missing or file operations do not successfully preserve and restore simulation data. |
| Python Best Practices and Documentation | Code consistently follows Python best practices and is exceptionally clear and maintainable. Type hints, docstrings, naming, formatting, and other documentation are accurate and useful throughout. | Code follows appropriate Python best practices. Functions use appropriate type hints and docstrings, and names and comments make the program easy to understand. | Code follows some Python conventions and includes some useful documentation, but documentation, type hints, docstrings, or naming may be inconsistent. | Code frequently does not follow Python conventions and has little or missing documentation. Type hints and/or docstrings are missing from functions. |
| Project Requirements | All project requirements are successfully implemented, with features developed beyond the minimum requirements in ways that meaningfully improve the simulation. | All requirements outlined in the project description are successfully implemented. | Most project requirements are present, but one or more requirements are incomplete or implemented inconsistently. | Several major requirements from the project description are missing or incomplete. |
