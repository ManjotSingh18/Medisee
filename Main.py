import requests
class Case():
    def __init__(self, age: int, sex: int) -> None:
        self.age=age
        self.sex=sex
        self.drugs=[]
        self.reactions=[] 


def mainsearch():
    drugname = str(input())
    apicall(drugname)
def apicall(drug: str):
    cases=[]
    api_url= f'https://api.fda.gov/drug/event.json?search=patient.drug.openfda.brand_name:"{drug}"&limit=10'
    response = requests.get(api_url)
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
            
    for c in cases:
        print(c.age)
        print(c.sex)
        print(c.drugs)
        print(c.reactions)
        print('\n')

def demo():
    mainsearch()
demo()
