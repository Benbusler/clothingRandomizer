import requests

enteries = []
# Replace with your Thingspeak API key
api_key = 'RAAVPDMVCSJ9KA5G'

# Replace with the ID of the channel you want to retrieve data from
channel_id = '1964022'

# Set the number of results you want to retrieve (up to a maximum of 8000)
results = 100

# Set the URL for the Thingspeak API
url = 'https://api.thingspeak.com/channels/{}/feeds.json?api_key={}&results={}'.format(channel_id, api_key, results)

# Send a GET request to the Thingspeak API
response = requests.get(url)

# If the request was successful, print the data
if response.status_code == 200:
  data = response.json()
  #for feed in data['feeds']:
    #print(feed['created_at'], feed['field1'])
for feed in data['feeds']:
    enteries.append(feed['field1'])
else:
  print('Failed to retrieve data from Thingspeak')

#print(enteries)
newEnterries = [x for x in enteries if x != None]
#print("\n\n")
temp = newEnterries[len(newEnterries)-1][0:2]
print("temp: " + temp)

#for feed in data['feeds']:
    #print(feed['created_at'], feed['field2'])
for feed in data['feeds']:
    enteries.append(feed['field2'])
else:
  print('Failed to retrieve data from Thingspeak')

#print(enteries)
newEnterries = [x for x in enteries if x != None]
#print("\n\n")
light = newEnterries[len(newEnterries)-1][0:2]
print("Light: " + light)