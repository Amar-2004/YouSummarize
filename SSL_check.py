import requests
from requests.exceptions import SSLError

url="https://tactiq.io/tools/youtube-transcript"
condition= __name__== "__main__"
def check_SSL():
    try:
        response=requests.get(url)
        if condition:
            print(f"Status Code: {response.status_code}")
        return True
    except SSLError as e:
        if condition:
            print("Error occured while connecting")
        return False 
    except Exception as e:
        print("Uncaught Error")
        return False
if condition:
    print(check_SSL())
