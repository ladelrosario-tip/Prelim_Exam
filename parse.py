import json
import csv

with open('covid_cases.json', 'r') as covid_cases:
    data = json.loads(covid_cases.read())

columns = ['dateRep', 'countriesAndTerritories', 'cases', 'deaths']

with open('covid_cases_parsed.csv', 'w', newline="") as parsed_cases:
    file = csv.writer(parsed_cases)
    file.writerow(columns)
    for i in data["records"]:
        file.writerow([i["dateRep"],
        i["countriesAndTerritories"],
        i["cases"],
        i["deaths"]])