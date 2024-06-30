"""
DOWNLOAD FILE WIHT PYTHON 

"""
import os
import requests

URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path = os.path.join(os.getcwd(), "exemple.txt")
r = requests.get(URL)
if r.status_code == 200:
    with open(path, 'wb') as f:
        f.write(r.content)
else:
    print("Error: {}".format(r.status_code))
