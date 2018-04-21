import json
import requests

API_KEY = 'OylOqGPorg2UjpgDMgoGnVtRBKDhcNn7q6XF0rVb'
committees = []

def format_url(cycle, committee_id):
    url = "https://api.propublica.org/campaign-finance/v1/%s/committees/%s.json" % (cycle, committee_id)
    return url

response = requests.get(url, headers={"X-API-Key": API_KEY}).content

data = json.loads(response)
results = data['results'][0]['total_receipts']

print results

data['results'][0]['end_cash']
