import requests

response = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
print(response.json())

question_data = response.json()['results']
