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
bt1 =b1.text
bt2 =b2.text

# Calculate if blood types from recipient and donor are a match

if bt1 == bt2: 
    print("Patient F6 and M8 are a match")
else:
    print ("Patient F6 and M8 are not a match")

# Check result with a POST request
# Check your result by making a POST request to URL/match_check. Send a JSON with the following format:
# {"Name": "<name>", "Match": "<answer>"}
# Replace <name> with your Duke Net ID and <answer> with either Yes or No.
# This request will return "Correct" or "Incorrect".