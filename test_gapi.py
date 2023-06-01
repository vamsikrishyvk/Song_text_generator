import requests
docker_url = 'http://0.0.0.0:8000/song_generator'

response = requests.get(docker_url)

# Check the response status code
if response.status_code == 200:
    # Successful API call
    data = response.json()
    print('API response:', data)
else:
    # Error in API call
    print('API call failed with status code:', response.status_code)
