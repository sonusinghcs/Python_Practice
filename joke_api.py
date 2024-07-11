import requests
import random

def jokes():
    url="https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        joke_data= data["data"]["data"]
        joke = joke_data[random.randint(0,4)]["content"]
        return joke
    else:
        raise Exception("failed to deliver jokes")
def main():
    try:
        joke=jokes()
        print(f"jokes are:::: -> {joke}")
    except Exception as e:
        print(str(e))
if __name__ == "__main__":
    main()