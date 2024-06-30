"""
DOWNLOAD IMG FILE WIHT PYTHON 

"""
import os
import requests
from PIL import Image

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
path = os.path.join(os.getcwd(), "image.png")
r = requests.get(url)
if r.status_code == 200:
    with open(path, 'wb') as f:
        f.write(r.content)
        Image.open(path)
else:
    print("Error: {}".format(r.status_code))
