import requests

def extract_data():
    url = "https://api.example.com/data"
    response = requests.get(url)
    data = response.json()
    print("Data extracted:", data)
    return data
#added a dev comment

if __name__ == "__main__":
    extract_data()
