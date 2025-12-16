import base64
import json

import requests

CLIENT='ffa1d09e53ae4057bb5907ff6110b62c'
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
            for album in albums:
            
                    info = {
                        'album_name': album['name'],
                        'artist_name': album['artists'][0]['name'],
                        'release_date': album['release_date'],
                        'album_type': album['album_type'],
                        'total_tracks': album['total_tracks'],
                        'spotify_url': album['external_urls']['spotify'],
                        'album_image': album['images'][0]['url'] if album['images'] else None
                    }
                    print(json.dumps(info, indent=2))

    except Exception as e:
     print("ERROR in latest release data fetching...",e)
get_new_release()