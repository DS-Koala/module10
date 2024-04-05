# Scott Daniel Ellis (sellis37)
# EN.605.206 (81)

import json
import requests
from flask import Flask, Response

# API endpoint URL's and access keys
WMATA_API_KEY = "ffeb0f203129452889f87bd54fca8034"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

################################################################################

app = Flask(__name__)

# get incidents by machine type (elevators/escalators)
# field is called "unit_type" in WMATA API response
@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
    # Create an empty list called 'incidents'
    incidents = []

    # Use 'requests' to do a GET request to the WMATA Incidents API
    response = requests.get(INCIDENTS_URL, headers=headers)

    # Retrieve the JSON from the response
    if response.status_code == 200:
        data = response.json()

        # Iterate through the JSON response and retrieve all incidents matching 'unit_type'
        for incident in data['ElevatorIncidents']:
            
            if incident['UnitType'].lower() in unit_type.lower():
                
                # For each incident, create a dictionary containing the 4 fields from the API schema
                incident_dict = {
                    'StationCode': incident['StationCode'],
                    'StationName': incident['StationName'],
                    'UnitType': incident['UnitType'],
                    'UnitName': incident['UnitName']
                }
                # Add each incident dictionary object to the 'incidents' list
                incidents.append(incident_dict)

    # Return the list of incident dictionaries as a JSON string
    print(incidents)
    return Response(json.dumps(incidents), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)