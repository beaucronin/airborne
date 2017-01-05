import time

from chalice import Chalice
import boto3

app = Chalice(app_name='provider')
app.debug = True

STATES_TABLE = 'OpenSky_States'
dynamo = boto3.client('dynamodb')

MAX_AGE = 1200

@app.route('/', cors=True)
def index():
    def f(item):
        # transform from Dynamo-style items to plain dict
        x = {}
        for k, v in item.items():
            if 'NULL' in v:
                x[k] = None
            elif 'N' in v:
                x[k] = float(v['N'])
            elif 'S' in v:
                x[k] = v['S']
            elif 'BOOL' in v:
                x[k] = v['BOOL']
        return x

    t = int(time.time()) - MAX_AGE
    # Find all states whose position has been updated recently
    result = dynamo.scan(
        TableName=STATES_TABLE,
        Select='ALL_ATTRIBUTES',
        FilterExpression='time_position > :t',
        ExpressionAttributeValues={ ':t': { 'N': str(t) }}
    )
    return { 'states': [f(item) for item in result['Items']] }

