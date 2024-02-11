import requests
url = "https://restcountries.com/v3.1/name/india"
r = requests.get(url)
print(r.status_code)

if [ r.status_code == 200 ]:
    print(r.json())
else:
    print("Failed to retrive data")