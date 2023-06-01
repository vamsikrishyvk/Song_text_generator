import requests
import json
#from keras import backend as K
#K.clear_session()

headers = {'Content-Type': 'application/json'}
url = 'http://127.0.0.1:8000/song_generator'
data = {'prefix':"You’re Not Sorry (Taylor’s Version) Lyrics[Verse 1]\nAll this time I was wasting hoping you would come around\n"}
data = json.dumps(data)
response = requests.post(url,data=data,headers=headers)
print(response.json())
