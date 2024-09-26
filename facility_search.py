import json
from IPython.display import display
from ipywidgets import widgets

# Load the facilities from json file
def load_facilities(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def search_facilities(facilities, keyword):
    return [facility for facility in facilities if keyword.lower() in facility['facility'].lower()]

def create_facility_ui(facilities):
    # Create the widgets for keyword input, search button
    keyword_input = widgets.Text(
        value='',
        placeholder='Enter partial facility name',
        description='Search Keyword:',
        disabled=False)

    search_button = widgets.Button(
        description='Search',
        disabled=False,
        button_style='info',
        tooltip='Click to search for facilities',
        icon='search')

    # Populate the dropdown list with facilities
    dropdown_options = [(facility['facility'], facility['Id']) for facility in facilities]

    # Dropdown for selecting facility
    facility_dropdown = widgets.Dropdown(
        options=dropdown_options,
        value=None,
        description='Select Facility:',
        disabled=False)

    select_button = widgets.Button(
        description='Select',
        disabled=False,
        button_style='info',
        tooltip='Click to select the facility',
        icon='check')

    # create the output widgets
    result_text = widgets.Textarea(
        value='',
        placeholder='',
        description='',
        layout=widgets.Layout(width='100%', height='50px'),
        disabled=False)

    result_display = widgets.Textarea(
        value='',
        placeholder='',
        description='Results:',
        layout=widgets.Layout(width='100%', height='200px'),
        disabled=False)

    selected_text = widgets.Textarea(
        value='',
        placeholder='',
        description='Selected:',
        layout=widgets.Layout(width='100%', height='50px'),
        disabled=True)

    def on_search_button_clicked(b):
        keyword = keyword_input.value
        results = search_facilities(facilities, keyword)
        if results:
            result_text.value = f'Search results for "{keyword}" {len(results)} result(s) found\n'
            result_display.value = '\n'.join([f"ID: {result['Id']}, Facility: {result['facility']}" for result in results])
        else:
            result_text.value = f'No results found for "{keyword}"'
            result_display.value = ''


    def on_select_button_clicked(b):
        selected_facility = facility_dropdown.label
        selected_id = facility_dropdown.value
        selected_text.value = f'Selected Facily: {selected_facility}\nID: {selected_id}'

    # link the button to the function
    search_button.on_click(on_search_button_clicked)
    select_button.on_click(on_select_button_clicked)

    # display the widgets
    display(keyword_input, search_button, result_text, result_display, facility_dropdown, select_button, selected_text)
