# Working With JSON File (facility search solutions)
A collection of three different approaches to search and display facility data from a JSON file. Solutions include Jupyter Notebook, Flask, and ipywidgets with IPython.display.

# Facility Search Solutions

This repository contains three different solutions for searching and displaying facility data from a `facilities.json` file. Each approach offers a unique method for interacting with the data, ranging from simple terminal-based solutions to more advanced interactive user interfaces.

## Table of Contents

- [Solutions](#solutions)
  - [Solution 1: Jupyter Notebook](#solution-1-jupyter-notebook)
  - [Solution 2: Flask Web Application](#solution-2-flask-web-application)
  - [Solution 3: IPython.display and ipywidgets](#solution-3-ipython-display-and-ipywidgets)
- [Installation and Usage](#installation-and-usage)
- [Facility Data](#facility-data)
- [Contributing](#contributing)
- [License](#license)

---

## Solutions

### Solution 1: Jupyter Notebook

This is the simplest implementation where we directly search the facility list using Python in a Jupyter Notebook. The solution allows the user to enter a keyword and search the facility names, printing the results (ID and facility name) directly to the console.

#### Code:
```python
import json

# Load the facilities data from the json file
file = 'facilities.json'
with open(file, 'r') as f:
    facilities = json.load(f)

# function to search for facilities by keyword or search term
def search_facilities(facilities, keyword):
    results = [facility for facility in facilities if keyword.lower() in facility['facility'].lower()]
    if not results:
        print("No results found")
    else:
        print(f"Found {len(results)} results\n")
        for result in results:
            print(f"ID: {result['Id']}\nFacility: {result['facility']}\n")

# Example search for facilities
keyword = 'Peterborough'
search_facilities(facilities, keyword)




### Solution 2: Flask Web Application

The second solution is a more advanced web-based application built using Flask. It includes a web interface where users can search for facilities using a keyword. The results are displayed dynamically on the webpage. The user can also select a facility from a dropdown and display its ID.

#### Features:
- Web UI for searching facilities
- Search results displayed dynamically on the webpage
- Dropdown for selecting facilities and displaying the ID

#### Installation and Running the Flask App:
1. Install Flask: `pip install Flask`
2. Run the Flask app:
   ```bash
   python app.py
