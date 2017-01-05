import requests
import boto3

STATES_TABLE = 'OpenSky_States'
dynamo = boto3.client('dynamodb')

def main(event, context):
	def maybe_null_number(n):
		if n == None:
			return { 'NULL': True }
		else:
			return { 'N': str(n) }

	def maybe_null_string(s):
		if s == None or s == '':
			return { 'NULL': True }
		else:
			return { 'S': s }			

	# see https://opensky-network.org/apidoc/rest.html
	resp = requests.get('http://opensky-network.org/api/states/all')
	obj = resp.json()
	states = obj['states']
	for state in states:
		dynamo.put_item(
			TableName=STATES_TABLE,
			Item={
				'icao24': { 'S': state[0] },
				'callsign': maybe_null_string(state[1]),
				'country': maybe_null_string(state[2]),
				'time_position': maybe_null_number(state[3]),
				'time_velocity': maybe_null_number(state[4]),
				'longitude': maybe_null_number(state[5]),
				'latitude': maybe_null_number(state[6]),
				'altitude': maybe_null_number(state[7]),
				'on_ground': { 'BOOL': state[8] },
				'velocity': maybe_null_number(state[9]),
				'heading': maybe_null_number(state[10]),
				'vertical_rate': maybe_null_number(state[11])
			})
	return {
		'msg': '{} states updated'.format(len(states))
	}
