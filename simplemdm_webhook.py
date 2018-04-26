import os
import json
from botocore.vendored import requests


# Slack Payload Info
slack_webhook = os.getenv("SLACK_URL")
slack_headers = {'Content-Type': 'application/json'}
slack_message = {}

def slack_payload(swebhook, my_data, my_headers ):
    response = requests.post(swebhook, data = json.dumps(my_data), headers = my_headers)
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )

def build_message(ploadin):

    event_type = ploadin["type"]
    event_time = ploadin["at"]
    event_data = ploadin["data"]

    if event_type == "device.enrolled":
        message = {
            'text': 'Device ' + event_data['device']['serial_number'] + ' has enrolled at ' + event_time
        }
        return message

    elif event_type == "device.unenrolled":
        message = {
            'text': 'Device ' + event_data['device']['serial_number'] + ' has unenrolled at ' + event_time
        }
        return message
    elif event_type == "test_event":
        message = {
            'text': 'Test event from SimpleMDM'
        }
        return message

def handler(event, context):
    payload_message = build_message(event)
    slack_payload(slack_webhook, payload_message, slack_headers)


