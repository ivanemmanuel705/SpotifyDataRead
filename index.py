import base64
import os
from dotenv import load_dotenv
import requests
load_dotenv('.env')
CLIENT=os.getenv('CLIENT')
CLIENT_SECRET='65c355ca1df048f0955a5bf5f83252c3'

# creating a token for spotify
def access_token():
    try:
        # combine client id and client_secret
        credentials=f"{CLIENT}:{CLIENT_SECRET}"
        encoded_credential=base64.b64encode(credentials.encode()).decode()
        response = requests.post('https://accounts.spotify.com/api/token',
            headers={"Authorization":f'Basic {encoded_credential}'},
            data={'grant_type': 'client_credentials'})
        print("Token Generated Successfully...")
        return response.json()['access_token']
    except Exception as e:
        print("Error in token Generation..",e)

print(access_token())

# latest release in spotify
def get_new_release():
    try:
        token=access_token()
        header={'Authorization':f'Bearer {token}'}
        params={'limit':50}
        response=requests.get('https://api.spotify.com/v1/browse/new-releases',
                           headers=header,params=params)
        if response.status_code==200:
            # print(response.json())
            data=response.json()
            albums=data['albums']['items']
            for i in albums:
                a={
                    'albums_name':i['name'],
                    'Release_date':i['release_date']
                }
                print(a)
    except Exception as e:
     print("ERROR in latest release data fetching...",e)
get_new_release()