# First create a virual environment. Type python -m venv env in terminal. "env" is the folder name in which your virtual environment will be created. You can name it anything.
# Then install two libraries, "requests" and "typing". For example Type pip install typing in terminal.
# Now type the code.

from typing import Final
import requests

API_KEY: Final[str] = 'YOUR_KEY'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'

def shorten_link(full_link: str):
    payload: dict = {'key': API_KEY, 'short': full_link, }
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()
    url_auth:bool = data.get('auth')

    if url_auth == False:
        print('message: ', data.get('message'))
    else:
        url_data:any = data.get('url')
        if url_data and 'status' in url_data:
            if url_data['status'] == 7:
                short_link: str = url_data['shortLink']
                print('Link:', short_link)
            else:
                print('Error status:', url_data['status'])

def main():
    link: str = input('Enter a link: ')

    shorten_link(link)

if __name__ == '__main__':
    main()
