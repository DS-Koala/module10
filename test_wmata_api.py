# Scott Daniel Ellis (sellis37)
# EN.605.206 (81)

from wmata_api import app
import json
import unittest


class WMATATest(unittest.TestCase):
    # Ensure both endpoints return a 200 HTTP code
    def test_http_success(self):
        # assert that the response code of 'incidents/escalators returns a 200 code
        escalator_response = app.test_client().get('/incidents/escalators').status_code
        self.assertEqual(escalator_response, 200, "Escalator endpoint did not return HTTP 200")

        # assert that the response code of 'incidents/elevators returns a 200 code
        elevator_response = app.test_client().get('/incidents/elevators').status_code
        self.assertEqual(elevator_response, 200, "Elevator endpoint did not return HTTP 200")

################################################################################

    # Ensure all returned incidents have the 4 required fields
    def test_required_fields(self):
        required_fields = ["StationCode", "StationName", "UnitType", "UnitName"]

        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        for incident in json_response:
            for field in required_fields:
                self.assertIn(field, incident, f"{field} is missing in the incident data")

################################################################################

    # Ensure all entries returned by the /escalators endpoint have a UnitType of "ESCALATOR"
    def test_escalators(self):
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # for each incident in the JSON response, assert that the 'UnitType' is "ESCALATOR"
        for incident in json_response:
            self.assertEqual(incident['UnitType'], "ESCALATOR", "Non-escalator unit found in escalator endpoint")

################################################################################

    # Ensure all entries returned by the /elevators endpoint have a UnitType of "ELEVATOR"
    def test_elevators(self):
        response = app.test_client().get('/incidents/elevators')
        json_response = json.loads(response.data.decode())

        # for each incident in the JSON response, assert that the 'UnitType' is "ELEVATOR"
        for incident in json_response:
            self.assertEqual(incident['UnitType'], "ELEVATOR", "Non-elevator unit found in elevator endpoint")

################################################################################

if __name__ == "__main__":
    unittest.main()