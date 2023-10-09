import requests

def get_supported_languages(api_url='https://libretranslate.de'):
    url = f'{api_url}/languages'

    response = requests.get(url)

    if response.status_code == 200:
        languages = response.json()
        return languages
    else:
        print(f"Failed to retrieve language list with status code {response.status_code}")
        return None




def translate_function(api_url='https://libretranslate.de'): #Defining the function 
    url = f'{api_url}/translate'
    df = get_supported_languages()
    print("The supported languages are : ")
    for i in range(len(df)) :
        print(df[i]['code'] + " : " + df[i]['name'])
    code = input("Enter the code of the language to translate to : ")
    headers = {'Content-Type': 'application/json'}
    text = input("Enter the text to translate: ")
    payload = {                                                     #Payload is the data that is sent to the server to get the response
        'q': text,
        'source' : 'auto',
        'target': code  
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        translation = response.json()['translatedText']
        print(f"Translation: {translation}")
    else:
        print(f"Translation request failed with status code {response.status_code}")
        print(f"Response content: {response.text}")


translate_function()

