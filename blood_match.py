import requests

# Get the IDs for two patients

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/nb202")
answer = r.json()
print(answer)

# Get the blood type of the two patients

b1 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F6")
b2 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M8")
print(b1.text)
print(b2.text)

#