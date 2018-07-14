import requests

r = requests.get('http://iguanaapplication-env.2tmqpmveaf.us-east-2.elasticbeanstalk.com/api/greeting/3879a137-004d-45b8-95d9-0094d22bb5f7')
print(r.json())

#r = requests.get('http://localhost:8090/api/mariko')
#print(r.json())