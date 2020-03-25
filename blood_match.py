import requests

# Get the IDs for two patients

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/nb202")
answer = r.json()
print(answer)
