import requests

#Used to store pateint basics 
class Case():
    def __init__(self, age: int, sex: int) -> None:
        self.age=age
        self.sex=sex
        self.drugs=[]
        self.reactions=[] 

#Takes input for search
def mainsearch():
    drugname = str(input())
    apicall(drugname)
#API call to retrieve adverse effect reports on given search
def apicall(drug: str):
    cases=[]
    api_url= f'https://api.fda.gov/drug/event.json?search=patient.drug.openfda.brand_name:"{drug}"&limit=15'
    response = requests.get(api_url)
    try:
        for patients in response.json()['results']:
                try:
                    currcase=Case(patients['patient']['patientonsetage'], patients['patient']['patientsex'])
                    for drug in patients['patient']['drug']:
                        currcase.drugs.append(drug['medicinalproduct'])
                    for reaction in patients['patient']['reaction']:
                        currcase.reactions.append(reaction['reactionmeddrapt'])
                    cases.append(currcase)
                except:
                    print("Error")
    except:
        print("Invalid")
            
    """
    for c in cases:
        print(c.age)
        print(c.sex)
        print(c.drugs)
        print(c.reactions)
        print('\n')
    """
    return cases 

