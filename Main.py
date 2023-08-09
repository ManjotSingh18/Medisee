import requests
def mainsearch():
    drugname = str(input())
    apicall(drugname)
def apicall(drug):
    api_url= f'https://api.fda.gov/drug/event.json?search=patient.drug.openfda.brand_name:"{drug}"&limit=10'
    response = requests.get(api_url)
    for patients in response.json()['results']:
        for reaction in patients['patient']['reaction']:
            #print(reaction['reactionmeddrapt'])
            pass
def demo():
    mainsearch()
demo()
