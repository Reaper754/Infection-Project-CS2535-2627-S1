# Infection! (CS35 Edition)

Create a visual simulation of an infection spreading through a population. Users will choose the population and disease settings before each trial. Your program will display people moving through a Pygame window as their infection status changes. It will track the results over simulation days and display those results on a graph.

When the program starts, the user first interacts with a terminal menu. This menu lets them start a new simulation or view previous simulation data. It also provides the options to resume or rerun a saved simulation and exit the program. The Pygame simulation window opens when the user chooses to start, resume, or rerun a simulation.

This project combines object-oriented programming, Pygame, graphing, and file handling. Your objects will represent people, a shared disease, and each person's movement. Build it in manageable stages. Start with the terminal menu and population data. Then add movement, infection rules, saving, and graphing. Test each feature as you add it. Use the [recommended development process](development_process.md) as a suggested order, replacing its dictionary-based people with the object design below. The [How To references](_Help/How%20To) explain useful library features. The BONUS guides cover vectors inside objects and saving vector data.

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

* [ ] The population is stored as a list of `Person` objects, including `ImmunePerson` objects.
* [ ] Each person stores a status: infected, recovered, susceptible, or dead.
* [ ] Each person exposes an immune value as `True` or `False` that matches their person type.
* [ ] Each person owns a movement component that stores position and velocity as `pygame.Vector2` objects.
* [ ] Movement code uses the vectors to update position and reverse direction at window boundaries.
* [ ] The population size matches the user's population count.
* [ ] The starting immune population is determined by the user's immunity percentage.
* [ ] Infection checks use the user's transmissibility distance and infectiousness percentage.
* [ ] Infection checks for immune people use the user's immunity efficacy percentage.
* [ ] Daily death checks for infected people use the user's lethality percentage.
* [ ] Daily recovery checks for infected people use the user's recoverability percentage.

### Object Design and Relationships

**Association means one object uses another independent object.** Create one `Disease` object for a trial. It stores the disease name, infectiousness, transmissibility, lethality, recoverability, and immunity efficacy. People hold references to that same object. Removing one person does not remove the disease. This relationship lets people use the same disease rules without making a separate disease copy for everyone.

**Inheritance means one class is a specialized type of another class.** Define a `Person` base class and an `ImmunePerson` subclass. Both have the same basic movement, status, and drawing behaviour. Override an infection-chance method in `ImmunePerson` to apply immunity efficacy. Both classes can then be processed through the same population loop. Keep infected, recovered, susceptible, and dead as status values rather than subclasses. A person's status changes during the trial.

**Composition means an object owns a component as part of itself.** Each person creates and owns a separate movement component. That component stores position and velocity and provides movement and wall-bounce methods. People delegate movement to their component. Components are not shared between people. Their lifetime belongs to their person.

* [ ] A student-defined `Disease` class stores the disease settings and provides methods used in infection, death, and recovery checks.
* [ ] Each person stores a reference to the trial's shared `Disease` object and uses it when calculating disease outcomes.
* [ ] A student-defined `Person` class provides methods for movement, drawing, and calculating infection chance.
* [ ] `ImmunePerson` inherits from `Person` and overrides the infection-chance method to account for immunity efficacy.
* [ ] The population update calls the same infection-chance method on both person types without using a type check to select their infection formula.
* [ ] Each person creates and owns its own student-defined movement component.
* [ ] The person's movement method calls the component's movement and wall-bounce methods.
* [ ] Drawing and movement use predefined Pygame objects, including a display `Surface`, a `Clock`, and `Vector2` objects.

### Saving and Restoring Objects

JSON stores ordinary data rather than live Python objects. Save each person's attributes and person type. Convert vectors to numeric coordinates when saving. Rebuild the objects when loading. Restore the shared disease reference instead of creating a separate disease for every loaded person.

* [ ] JSON saves include the disease settings, each person's type and status, and each movement component's position and velocity.
* [ ] Loading a save recreates `Person` and `ImmunePerson` instances with their saved attributes.
* [ ] Loading a save recreates a separate movement component for each person and restores its vectors.
* [ ] All loaded people reference the same restored `Disease` object.

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
* [ ] The simulation ends automatically when there are no infected people left.

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

## CSE 3120 - Object Oriented Programming 1

| Outcome | Excellent | Proficient | Developing | Emerging |
| --- | --- | --- | --- | --- |
| Using Predefined Objects | Predefined Pygame objects are used deliberately through their methods and attributes, with clear ownership and reliable integration throughout the simulation. | Predefined Pygame objects, including surfaces, clocks, and vectors, are created and used correctly through their methods and attributes. | Predefined objects are used, but creation, method calls, attribute access, or integration is sometimes incorrect or inconsistent. | Predefined objects are rarely used or are used incorrectly, preventing required simulation features from working. |
| Using Student Defined Objects | Student-defined classes have clear responsibilities and coordinate through focused methods, with instance attributes that reliably preserve each object's state. | Student-defined classes create disease, person, and movement objects with appropriate instance attributes and methods used by the simulation. | Student-defined objects represent some simulation information, but responsibilities, instance state, or methods are incomplete or inconsistent. | Student-defined objects are missing or do not effectively represent and control simulation behaviour. |
| Python Best Practices | Code consistently follows Python best practices. Classes and methods have clear responsibilities, accurate type hints and docstrings, and consistent naming and formatting. | Code follows Python best practices. Classes and methods use appropriate names, type hints, docstrings, and formatting. | Code follows some Python conventions, but naming, type hints, documentation, or formatting are inconsistent. | Code frequently does not follow Python conventions and has little or missing documentation, type hints, or consistent formatting. |
| Assignment Requirements | All assignment requirements are successfully implemented, with features developed beyond the minimum requirements in ways that meaningfully improve the simulation. | All requirements outlined in the assignment are successfully implemented. | Most assignment requirements are present, but one or more requirements are incomplete or implemented inconsistently. | Several major assignment requirements are missing or incomplete. |

## CSE 3130 - Object Oriented Programming 2

| Outcome | Excellent | Proficient | Developing | Emerging |
| --- | --- | --- | --- | --- |
| Use of Associative Relationships in Objects | People consistently use one shared disease through clear object references, with independent lifetimes and correctly restored associations after loading. | People reference and use the trial's shared Disease object, and loading restores that shared association. | An association is present, but disease references, shared use, or restoration after loading are inconsistent. | An association is missing or each person uses an unrelated disease copy instead of the shared object. |
| Use of Inheritance Relationships in Objects | The Person hierarchy reuses common behaviour and overrides infection chance clearly, allowing both person types to work consistently through the same interface after creation and loading. | ImmunePerson inherits from Person, overrides infection chance for immunity efficacy, and works through the same population interface. | Inheritance is present, but inherited behaviour, overriding, or use through a common interface is incomplete or inconsistent. | Inheritance is missing or the subclass does not reuse and specialize the base class's behaviour. |
| Use of Composition Relationships in Objects | Each person consistently owns a distinct movement component with focused methods, clear delegation, and correctly reconstructed ownership after loading. | Each person creates and owns a separate movement component and delegates movement and wall bouncing to it. Loading recreates that ownership. | Composition is present, but component ownership, delegation, or reconstruction after loading is unclear or inconsistent. | Composition is missing or movement components are not owned and used as parts of individual people. |
| Python Best Practices | Code consistently follows Python best practices. Classes and methods have clear responsibilities, accurate type hints and docstrings, and consistent naming and formatting. | Code follows Python best practices. Classes and methods use appropriate names, type hints, docstrings, and formatting. | Code follows some Python conventions, but naming, type hints, documentation, or formatting are inconsistent. | Code frequently does not follow Python conventions and has little or missing documentation, type hints, or consistent formatting. |
| Assignment Requirements | All assignment requirements are successfully implemented, with features developed beyond the minimum requirements in ways that meaningfully improve the simulation. | All requirements outlined in the assignment are successfully implemented. | Most assignment requirements are present, but one or more requirements are incomplete or implemented inconsistently. | Several major assignment requirements are missing or incomplete. |

## CSE 2130 - Files and File Structures 1

| Outcome | Excellent | Proficient | Developing | Emerging |
| --- | --- | --- | --- | --- |
| Use of CSV Files | CSV records are consistently organized and accurately preserve settings and daily counts across new, resumed, and repeated runs, supporting reliable graphing without overwriting previous results. | CSV files append daily counts automatically, preserve trial settings, and can be read for graphing. Resumed runs use the recorded CSV, and new runs use unique files. | CSV files record some trial data, but daily appending, file selection, preservation of previous results, or reading for graphing is inconsistent. | CSV files are missing or file operations do not successfully record and retrieve trial data. |
| Use of JSON Files | JSON saves consistently preserve state, time, settings, and the active CSV reference in a clear structure that supports reliable resuming and rerunning. | Pressing `s` saves simulation state, time, input settings, and the active CSV reference. Saved data supports resuming a run and rerunning its starting settings. | JSON saves are present, but saved information, resuming, or rerunning is incomplete or inconsistent. | JSON saves are missing or file operations do not successfully preserve and restore simulation data. |
| Python Best Practices and Documentation | Code consistently follows Python best practices and is exceptionally clear and maintainable. Type hints, docstrings, naming, formatting, and other documentation are accurate and useful throughout. | Code follows appropriate Python best practices. Functions use appropriate type hints and docstrings, and names and comments make the program easy to understand. | Code follows some Python conventions and includes some useful documentation, but documentation, type hints, docstrings, or naming may be inconsistent. | Code frequently does not follow Python conventions and has little or missing documentation. Type hints and/or docstrings are missing from functions. |
| Project Requirements | All project requirements are successfully implemented, with features developed beyond the minimum requirements in ways that meaningfully improve the simulation. | All requirements outlined in the project description are successfully implemented. | Most project requirements are present, but one or more requirements are incomplete or implemented inconsistently. | Several major requirements from the project description are missing or incomplete. |
