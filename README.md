<p align="center">
  <img src="img/logo.png" width="55%" height="150" margin-left="auto" margin-right="auto">
</p>

# About
Medisee is a program intended to improve transparency and accessibility of medicine and its adverse effects via the visualization of anonymous cases that may be difficult to obtain by users as they are stored in the Federal Drug Administration API.

# Features 
* Visualizes FDA API into a readable format
* Up to 1000 Drug/Reaction cases available per query
* Filter available to narrow cases down
* Simplistic GUI for seamless analysis of data 

# Requirements
* Python (See Requirements.txt)
* Python Interpreter
* Network Connection
* Command Prompt

# Installation and Usage
1. Download the repository and extract it to the desired location
2. Launch a command prompt and navigate to the repository by entering "cd Path/to/folder"
3. To execute the program enter "python gui.py"
4. The user will be prompted by a medical disclaimer where they can agree and continue or disagree and terminate the program
<p align="center">
  <img src="img/disc.png" width="75%" height="50%" margin-left="auto" margin-right="auto">
</p>

5. Enter a medicinal query and utilize the filter button if required, once ready click the search button
6. Within a few seconds hundreds of cases will be available below, to navigate use the next and previous buttons, to search specific pages use the page finder entry

<p align="center">
  <img src="img/search.png" width="75%" height="500" margin-left="auto" margin-right="auto">
</p>



# Technology
## Python (Tkinter)
* Used to capture the data from FDA API and visualized using Tkinter GUI

# Contributions
Medisee is open source and welcomes contributions and features from developers to further dismantle the blocks between patients and medicinal data.

# Future
A feature in development is the ability to scan medicine and query by NDC code. A secondary feature being discussed is a text enlarger for prescription medicine as elderly people may have a difficult time reading small text on medicinal products. 
