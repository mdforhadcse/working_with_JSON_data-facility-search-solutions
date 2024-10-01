# Solution 2: Flask Web Application
from flask import Flask, render_template, request
import json

# Load facilities data from the JSON file
file = 'facilities.json'
with open(file, 'r') as f:
    facilities = json.load(f)

# Initialize the Flask application
app = Flask(__name__)

# Function to search facilities by keyword
def search_facilities(facilities, keyword):
    return [facility for facility in facilities if keyword.lower() in facility['facility'].lower()]

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        if keyword:
            results = search_facilities(facilities, keyword)
            return render_template('index.html', results=results, keyword=keyword)
    return render_template('index.html', results=None)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)